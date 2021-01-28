# This module defines the generic base class and the functionality.
from abc import ABC, abstractmethod
import datetime
import os
import shutil
import sqlite3
import tempfile
import typing
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple
from urllib.parse import urlparse
import utils

HistoryVar = List[Tuple[datetime.datetime, str]]

# A generic class to support all major browsers with minimal configuration.
# Currently, only browsers which save the history in SQLite files are supported.
class Browser(ABC):

    # Boolean indicating whether the browser supports multiple profiles.
    profile_support = False

    # List of possible prefixes for the profile directories.
    # Keep empty to check all subdirectories in the browser path.
    # profile_dir_prefixes: typing.Optional[typing.List[typing.Any]] = None


    def __init__(self, plat = None):
        self.profile_dir_prefixes = []
        
        if plat is None:
            plat = utils.get_platform()
        homedir = Path.home()

        error_string = self.name + " browser is not supported on {}"
        
        if plat == utils.Platform.WINDOWS:
            assert self.windows_path is not None, error_string.format("windows")
            self.history_dir = homedir / self.windows_path
        
        elif plat == utils.Platform.MAC:
            assert self.mac_path is not None, error_string.format("Mac OS")
            self.history_dir = homedir / self.mac_path
        
        elif plat == utils.Platform.LINUX:
            assert self.linux_path is not None, error_string.format("Linux")
            self.history_dir = homedir / self.linux_path
        
        else:
            raise NotImplementedError()

        if self.profile_support and not self.profile_dir_prefixes:
            self.profile_dir_prefixes.append("*")

    # Returns a list of profile directories. 
    # If the browser is supported on the current platform but is not installed an empty list will be returned
    def profiles(self, profile_file):
        # profile_file: file to search for in the profile directories.
        # This should be history_file.
        # profile_file is a string
        # return type list(str)

        if not os.path.exists(self.history_dir):
            utils.logger.info("%s browser is not installed", self.name)
            return []
        
        if not self.profile_support:
            return ["."]
        profile_dirs = []
        
        for files in os.walk(str(self.history_dir)):
            for item in files[2]:
                if os.path.split(os.path.join(files[0], item))[-1] == profile_file:
                    path = str(files[0]).split(str(self.history_dir), maxsplit=1)[-1]
                    if path.startswith(os.sep):
                        path = path[1:]
                    
                    if path.endswith(os.sep):
                        path = path[:-1]
                    
                    profile_dirs.append(path)
        
        return profile_dirs

    # Returns path of the history file for the given profile_dir
    def history_path_profile(self, profile_dir):
        # The profile_dir should be one of the outputs from profiles method
        # profile_dir: Profile directory (should be a single name, relative to history_dir)
        # returns path to history file of the profile
        if self.history_file is None:
            return None

        return self.history_dir / profile_dir / self.history_file

    # Returns a list of file paths, for all profiles
    def paths(self, profile_file):
        return [self.history_dir / profile_dir / profile_file for profile_dir in self.profiles(profile_file)]

    # Returns history of profiles given by `profile_dirs`
    def history_profiles(self, profile_dirs):
        history_paths = [self.history_path_profile(profile_dir) for profile_dir in profile_dirs]
        return self.fetch_history(history_paths)

    # Returns history of all available profiles stored in SQL
    def fetch_history(self, history_paths=None, sort=True, desc=False):
        """
        The returned datetimes are timezone-aware with the local timezone set by default.

        The history files are first copied to a temporary location and then queried
        This might lead to some additional overhead and results returned might not be the latest if the browser is in use
        This is done because the SQlite files are locked by the browser when in use.

        history_paths: optional list of history files.

        sort: optional boolean flag to specify if the output should be sorted. 
        -> Default value set to True.
        
        desc: optional boolean flag to specify asc/desc
        Applicable if sort is True 
        -> Default value set to False.
        """
        # Path to history database
        if history_paths is None:
            history_paths = self.paths(self.history_file)
        
        # Fetch history
        output_object = Outputs("history")
        
        # Make temporary directory
        with tempfile.TemporaryDirectory() as tmpdirname:
            for history_path in history_paths:
                # Copy the file while preserving metadata
                copied_history_path = shutil.copy2(history_path.absolute(), tmpdirname)
                conn = sqlite3.connect(f"file:{copied_history_path}?mode=ro", uri=True)
                cursor = conn.cursor()

                # Execute sql command
                cursor.execute(self.history_SQL)
                # Format datetime to custom
                date_histories = [(datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S"), url) for d, url in cursor.fetchall()]
                output_object.histories.extend(date_histories)
                
                # Sorting
                if sort:
                    output_object.histories.sort(reverse=desc)
                conn.close()

        return output_object

# A generic class to encapsulate history outputs
class Outputs:

    # List of tuples of timestamp & URL
    histories: List[Tuple[datetime.datetime, str]]

    # Dictionary which maps fetch_type to the respective variables and formatting fields.
    field_map: Dict[str, Dict[str, Any]]

    # fetch_type: string argument to select history output
    def __init__(self, fetch_type):
        self.fetch_type = fetch_type
        self.histories = []
        self.field_map = {
            "history": {"var": self.histories, "fields": ("Timestamp", "URL")},
        }

    # Returns the history sorted according to the domain-name.
    def sort_domain(self):
        domain_histories: typing.DefaultDict[typing.Any, List[Any]] = defaultdict(list)
        for entry in self.field_map[self.fetch_type]["var"]:
            domain_histories[urlparse(entry[1]).netloc].append(entry)
        return domain_histories


# A generic class to support Chromium based browsers.
class ChromiumBasedBrowser(Browser, ABC):
    profile_dir_prefixes = ["Default*", "Profile*"]

    history_file = "History"
    bookmarks_file = "Bookmarks"

    history_SQL = """
        SELECT 
            datetime(visits.visit_time/1000000-11644473600, 'unixepoch', 'localtime') as 'visit_time', 
            urls.url
        FROM 
            visits INNER JOIN urls ON visits.url = urls.id
        WHERE 
            visits.visit_duration > 0
        ORDER BY 
            visit_time DESC
        """
