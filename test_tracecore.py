# test_tracecore.py
"""
Tests for TraceCore module.
"""

import unittest
from tracecore import TraceCore

class TestTraceCore(unittest.TestCase):
    """Test cases for TraceCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TraceCore()
        self.assertIsInstance(instance, TraceCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TraceCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
