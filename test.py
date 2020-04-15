from selenium import webdriver
import subprocess
import threading
import unittest
import os

from Budget_App import FlaskAppWrapper
from Budget_Manager import Budget_Manager

class BudgetSystemE2ETest(unittest.TestCase):
    def setUp(self):
        self.app_process = subprocess.Popen(['python3', './main.py', 'test.db'], stdin=subprocess.PIPE)
        self.browser = webdriver.Chrome()
        self.browser.get('http://127.0.0.1:5000/')
    def testCreateABudgetAndReturnSuccess(self):
        date_text = self.browser.find_element_by_id('date').send_keys(202002)
        budget_text = self.browser.find_element_by_id('budget').send_keys(20000)
        submit_btn = self.browser.find_element_by_id('submit').click()
        result_text = self.browser.find_element_by_id("messageBox").text
        self.assertEqual(result_text, "Create Budget Success")
    def testUpdateAExistBudgetAndReturnSuccess(self):
        #Arrange
        date_text = self.browser.find_element_by_id('date').send_keys(202003)
        budget_text = self.browser.find_element_by_id('budget').send_keys(30000)
        submit_btn = self.browser.find_element_by_id('submit').click()
        self.browser.find_element_by_id('date').clear()
        self.browser.find_element_by_id('budget').clear()
        #Act
        date_text = self.browser.find_element_by_id('date').send_keys(202003)
        budget_text = self.browser.find_element_by_id('budget').send_keys(40000)
        submit_btn = self.browser.find_element_by_id('submit').click()
        #Assert
        result_text = self.browser.find_element_by_id("messageBox").text
        self.assertEqual(result_text, "Update Budget Success")

    def tearDown(self):
        self.browser.close()
        self.app_process.kill()
        os.remove('test.db')


class BudgetSystemUnitTest(unittest.TestCase):
    def setUp(self):
        self.budget_manager = Budget_Manager("test.db")
    def testCreateABudgetAndReturnSuccess(self):
        response = self.budget_manager.createBudget("202002", 30000)
        self.assertEqual(response, "Create Budget Success")
    def tearDown(self):
        os.remove('test.db')

if __name__ == '__main__':
    unittest.main()

