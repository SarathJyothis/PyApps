import sqlite3
import re

class connectDB:
    conn=None
    curr=None
    def __init__(self,dbloc):
        self.dbloc=dbloc
    def __enter__(self):
        self.conn = sqlite3.connect(self.dbloc)
        self.curr = self.conn.cursor()
        return self
    def __exit__(self,*args):
        self.conn.close()

class queryValidationError(Exception):

    def __init__(self,string):
        pass
def queryChecker(queryType,query):
    pattern = r'\b'+queryType.title()+r'\b'
    if (re.match(pattern,query.title())):
        return True
    return False