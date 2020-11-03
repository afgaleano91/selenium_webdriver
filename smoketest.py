from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertion import AssertionsTest
from searchtest import SearchTests

assertionTest = TestLoader().loadTestsFromTestCase(AssertionsTest)
searchTest = TestLoader().loadTestsFromTestCase(SearchTests)

smokeTest = TestSuite([assertionTest, searchTest])

kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smokeTest)