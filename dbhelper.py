import sqlite3
class DBHelper:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
      # create table with tablename items
        stmt = "CREATE TABLE IF NOT EXISTS items (description text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item_text):
        stmt = "INSERT INTO items VALUES (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text):
        stmt = "DELETE FROM items WHERE description = (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):
        stmt = "SELECT description FROM items"
        # To retrieve data after executing a SELECT statement, treat the cursor as an iterator.refer to docs for other methods.
        # row is returned as a tuple of the column values, hence select the data by using x[0]
        return [x[0] for x in self.conn.execute(stmt)]

    def check_exists(self, item_text):
        stmt = "SELECT description FROM items WHERE description =(?)"
        args = (item_text, )
        return [x[0] for x in self.conn.execute(stmt,args)]
