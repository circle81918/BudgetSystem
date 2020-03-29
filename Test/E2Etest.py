from selenium import webdriver
import unittest

class BudgetSystemTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://127.0.0.1:5000/')
    def testCreateABudgetAndReturnSuccess(self):
        date_text = self.browser.find_element_by_id('date').send_keys(202002)
        budget_text = self.browser.find_element_by_id('budget').send_keys(20000)
        submit_btn = self.browser.find_element_by_id('submit').click()
        result_text = self.browser.find_element_by_id("messageBox").text
        self.assertEqual(result_text, "Create Budget Success")
    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()
