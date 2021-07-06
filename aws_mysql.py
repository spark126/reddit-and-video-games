import pymysql


class MySqlConn:
    """
    Provides mysql connection to AWS rds.
    :param endpoint: string, endpoint of rds.
    :param user: string, username.
    :param password: string, password for database user.
    :param dbname: string, name of database.
    :return: Object.
    """

    def __init__(self, endpoint, user, password, dbname):
        # not the proper way to connect to rds
        self.endpoint = endpoint
        self.user = user
        self.password = password
        self.dbname = dbname
        self.conn = None

    def connect(self):
        """
        Connect to AWS rds server and set self.conn to connection.
        :return: None
        """
        conn = pymysql.connect(host=self.endpoint,
                               user=self.user,
                               password=self.password,
                               database=self.dbname)
        self.conn = conn

    def get(self, sql_query):
        """
        Opens connection to rds server and executes a get sql query. Closes connection.
        :param sql_query: SQL to get data from database.
        :return: Results of sql query.
        """
        self.connect()
        conn = self.conn
        cur = conn.cursor()
        cur.execute(sql_query)
        query_results = cur.fetchall()
        self.close()
        return query_results

    def batch_insert(self, sql, results):
        """
        Opens connection to rds server and executes a batch insert. Closes connection.
        :param sql: SQL for batch insert using mypysql executemany().
        :param results: List of tuple of values.
        :return: None
        """
        self.connect()
        conn = self.conn
        cur = conn.cursor()
        cur.executemany(sql, results)
        conn.commit()
        print(f'Batch insert into {self.dbname} database.')
        self.close()

    def close(self):
        """
        Closes open connection.
        :return: None
        """
        if self.conn:
            self.conn.close()
