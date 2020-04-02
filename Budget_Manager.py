import sqlite3

class Budget_Manager(object):
    def __init__(self, db_path="budget.db"):
        self._db_path = db_path
        self.init_DB()
    def init_DB(self):
        with sqlite3.connect(self._db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS BUDGET_TABLE
                (DATE TEXT PRIMARY KEY     NOT NULL,
                BUDGET           INT    NOT NULL
                    );''')

    def createBudget(self, date, budget):
        with sqlite3.connect(self._db_path) as conn:
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO BUDGET_TABLE (DATE, BUDGET) VALUES (?,?)", (date, budget))
                conn.commit()
                return "Create Budget Success"
            except conn.Error:
                return "Create Budget Fail"

