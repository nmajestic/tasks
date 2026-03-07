"""Tests for platform utility functions."""

import sys

from app.util.platform_utils import get_platform


def test_get_platform():
    """Verify that get_platform returns the current system platform string."""
    assert get_platform() == sys.platform
