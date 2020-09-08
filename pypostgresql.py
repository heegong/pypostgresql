import psycopg2

class postgresql:
    """
    postgresql use in python
    """
    def __init__(self,host,dbname,user,password=''):
        string = f"host='{host}' dbname ='{dbname}' user='{user}' password='{password}'"
        self.conn = psycopg2.connect(string)
        self.cur = self.conn.cursor()

    def query_execute(self,string):
        self.cur.execute(string)
        self.conn.commit()
    
    def select(self,column,table):
        column_string = ', '.join(column)
        self.cur.execute(f"SELECT {column_string} FROM {table}")
        result = self.cur.fetchall()
        return result

    def insert(self,column,values,table):
        which = ', '.join(column)
        len_s_string = ("%s, "*len(values)).strip()[:-1]
        query = f'INSERT INTO {table} ({which}) VALUES ({len_s_string})'
        self.cur.execute(query,values)
        self.conn.commit()
        
    def create_table(self,make,table):
        if isinstance(make,str):
            make_string = make
        else:
            make_string = ', '.join(make)
        query = f"CREATE TABLE {table} ({make_string});"
        
        self.cur.execute(query)
        self.conn.commit()

    def return_query(self,string,ls=''):
        if ls=='':
            self.cur.execute(string)
        else:
            self.cur.execute(string,ls)
        result = self.cur.fetchall()
        return result


    def where_select(self,column,where_query,table):
        """
        where_query : use "query" plz
        """
        column_string = ', '.join(column)
        self.cur.execute(f"SELECT {column_string} FROM {table} WHERE {where_query}")
        result = self.cur.fetchall()
        return result
