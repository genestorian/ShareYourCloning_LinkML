"""Data test."""

import os
import glob
import unittest

from linkml_runtime.loaders import json_loader
from shareyourcloning_linkml.datamodel import CloningStrategy

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, "*.json"))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Date test."""
        for path in EXAMPLE_FILES:
            obj = json_loader.load(path, target_class=CloningStrategy)
            assert obj
