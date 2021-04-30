import os
import platform
import sys
from os import path
from pathlib import Path

import pytest


@pytest.fixture()
# Use pytest monkeypatch
def change_homedir(monkeypatch):
    # Change home directory for all tests

    # Safe approach to locating 'tests/' dir (always the dir of this module)
    test_dir = path.dirname(path.abspath(__file__))
    monkeypatch.setattr(
        Path, "home", lambda: Path(
            f"{test_dir}/test_homedirs/{platform.system()}")
    )
    return platform.system()


@pytest.fixture()
def become_windows(monkeypatch):
    # Changes platform.system to return Windows
    monkeypatch.setattr(platform, "system", lambda: "Windows")
    return platform.system()


@pytest.fixture()
def become_mac(monkeypatch):
    # Changes platform.system to return Darwin (codename for Mac OS)
    monkeypatch.setattr(platform, "system", lambda: "Darwin")
    return platform.system()


@pytest.fixture()
def become_linux(monkeypatch):
    # Changes platform.system to return Linux
    monkeypatch.setattr(platform, "system", lambda: "Linux")
    return platform.system()


def test_dir():
    # get the curent directory
    test_dir = path.dirname(path.abspath(__file__))
    assert test_dir == "C:\\Users\\micha\\2021-ca400-gslowey-msavage\\src\\tests"


def test_set_path():
    # Should set path to parent class. This should be src.
    sys.path.append(str(Path(__file__).parent.parent.absolute()))
    assert os.getcwd() == "C:\\Users\\micha\\2021-ca400-gslowey-msavage\\src"
