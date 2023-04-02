import unittest
import HtmlTestRunner
from Automation_Emag import Emag

class TestSuite(unittest.TestCase):
    def test_suite(self):
        running_test = unittest.TestSuite()

        running_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Emag)
            # here we can add more tests
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='My report',
            report_name= 'Test Report'
        )
        runner.run(running_test)
