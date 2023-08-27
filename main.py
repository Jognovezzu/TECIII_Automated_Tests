import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from references import amazon_endpoints as variables
import time
from loginCase import TestLogin
from storeCase import TestStore
import os

print("To start the Test, check: login and password in `references.py`")
time.sleep(3)
print("Starting the Test....")
time.sleep(3)
os.system('cls')


test_cases = [TestLogin, TestStore]

test_loader = unittest.TestLoader()

suites_list = [test_loader.loadTestsFromTestCase(test_case) for test_case in test_cases]
combined_test_suite = unittest.TestSuite(suites_list)


unittest.TextTestRunner(verbosity=2).run(combined_test_suite)

    