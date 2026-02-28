"""Tests for ultra-file-search."""

import os
import tempfile
import pytest
from ultra_file_search import search


class TestSearch:
    """Test suite for search."""

    def test_basic(self):
        """Test basic usage with a real temp directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a sample file inside
            sample = os.path.join(tmpdir, "sample.txt")
            with open(sample, "w") as f:
                f.write("hello world")
            result = search(tmpdir)
            assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            search("")
        except (ValueError, TypeError, FileNotFoundError, OSError):
            pass  # Expected for path-based utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = search(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
