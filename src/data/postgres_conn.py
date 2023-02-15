import psycopg2

class Postegres:
    def __init__(self, host:str, port:int, dbname:str, user:str, password:str):
        self.conn = psycopg2.connect("dbname={} user={} host={} port={} password={}".format(dbname, user, host, port, password))
        
    def execute(self, query:str):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        data = cur.fetchone()
        cur.close()
        return data
        
    def __del__(self):
        self.conn.close()