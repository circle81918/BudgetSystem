import unittest 
import sys
import os
sys.path.append('../')

from Budget_Manager import Budget_Manager

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