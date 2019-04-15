import sqlite3
from TableDictionaries import TableDictionaries

class TableBuilder():
    """"""
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()

    def create_tables(self):
        with self.conn:
            for dict in TableDictionaries.dictionary_list:
                self.c.execute(dict["CREATE"])
