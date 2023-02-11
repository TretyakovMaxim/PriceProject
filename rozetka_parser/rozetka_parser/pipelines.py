import sqlite3


class RozetkaParserPipeline:
    def __init__(self):
        ## Create/Connect to database
        self.con = sqlite3.connect('phones.db')

        ## Create cursor, used to execute commands
        self.cur = self.con.cursor()

        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS rozetka(
            model TEXT,
            price INTEGER,
            url TEXT
        )
        """)

    def process_item(self, item, spider):
        ## Define insert statement
        self.cur.execute("""
                    INSERT INTO rozetka (model, price, url) VALUES (?, ?, ?)
                """,
                         (
                             item['model'],
                             item['price'],
                             item['url']
                         ))

        ## Execute insert of data into database
        self.con.commit()
        return item
