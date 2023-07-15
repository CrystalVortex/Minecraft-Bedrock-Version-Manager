import pytest
import urllib3

from bedrock.versions import Version, Versions


def setup():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def test_invalid_version_is_none():
    assert(Versions.get_by_version("Invalid") is None)


def test_deprectated_version():
    version = Versions.get_by_version("0.13.0.0")
    assert(version.version == "0.13.0.0")
    assert(version.is_deprecated is True)
    assert(version.uri is None)


def test_valid_version():
    version = Versions.get_by_version("1.8.0.24")
    assert(version.version == "1.8.0.24")
    assert(version.update_id is not None)
    assert(version.is_beta is False)
    assert(version.is_deprecated is False)
    assert(version.uri is not None)


def test_valid_version_beta():
    version = Versions.get_by_version("1.11.0.3")
    assert(version.version == "1.11.0.3")
    assert(version.update_id is not None)
    assert(version.is_beta is True)
    assert(version.is_deprecated is False)
    assert(version.uri is None)
