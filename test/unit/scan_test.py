import unittest
from src.source.scan import SingleScanResult

class SingleScanResultTestCase(unittest.TestCase):
    def setUp(self):
       self.scan_result = SingleScanResult() 

    def tearDown(self):
        pass

    def test_set_name(self):
        self.assertEqual(self.scan_result.set_name("test"), None)

    def test_get_name(self):
        self.assertEqual(self.scan_result.get_name(), "noname")

    def test___str___(self):
        self.assertMultiLineEqual("Name: noname\nTime: notime\nCoortinates: 0.0, 0.0\nMAC addresses ",
                "{}".format(self.scan_result))

if __name__ == '__main__':
    unittest.main()
