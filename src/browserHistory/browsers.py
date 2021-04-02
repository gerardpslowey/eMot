# Functions to define all supported browsers and their functionality.
import datetime, os, sys
from .generic import Browser, ChromiumBasedBrowser

# Google Chrome on Windows, Linux and Mac
class Chrome(ChromiumBasedBrowser):
    name = "Chrome"

    windows_path = "AppData/Local/Google/Chrome/User Data"
    mac_path = "Library/Application Support/Google/Chrome/"
    linux_path = ".config/google-chrome"

    profile_support = True

# Firefox on Windows, Linux and Mac
class Firefox(Browser):
    name = "Firefox"

    windows_path = "AppData/Roaming/Mozilla/Firefox/Profiles"
    linux_path = ".mozilla/firefox"
    mac_path = "Library/Application Support/Firefox/Profiles/"

    profile_support = True

    history_file = "places.sqlite"

    history_SQL = """
        SELECT 
            datetime(visit_date/1000000, 'unixepoch', 'localtime') AS 'visit_time', 
            url
        FROM 
            moz_historyvisits
        INNER JOIN 
            moz_places
        ON 
            moz_historyvisits.place_id = moz_places.id
        WHERE 
            visit_date IS NOT NULL AND url LIKE 'http%' AND title IS NOT NULL
    """

# Safari on MAC
class Safari(Browser):
    name = "Safari"

    mac_path = "Library/Safari"
    history_file = "History.db"
    profile_support = False

    history_SQL = """
        SELECT 
            datetime(visit_time + 978307200, 'unixepoch', 'localtime') as visit_time, 
            url
        FROM 
            history_visits
        INNER JOIN 
            history_items
        ON 
            history_items.id = history_visits.history_item
        ORDER BY 
            visit_time DESC
    """

# Edge on Windows and Mac
class Edge(ChromiumBasedBrowser):
    name = "Edge"

    windows_path = "AppData/Local/Microsoft/Edge/User Data"
    mac_path = "Library/Application Support/Microsoft Edge"

    profile_support = True

# Opera on Linux, Windows and Mac
class Opera(ChromiumBasedBrowser):
    name = "Opera"

    linux_path = ".config/opera"
    windows_path = "AppData/Roaming/Opera Software/Opera Stable"
    mac_path = "Library/Application Support/com.operasoftware.Opera"

    profile_support = False

# Brave on Linux, Windows and Mac
class Brave(ChromiumBasedBrowser):
    name = "Brave"

    linux_path = ".config/BraveSoftware/Brave-Browser"
    mac_path = "Library/Application Support/BraveSoftware/Brave-Browser"
    windows_path = "AppData/Local/BraveSoftware/Brave-Browser/User Data"

    profile_support = True
