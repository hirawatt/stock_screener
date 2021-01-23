import psycopg2
import psycopg2.extensions
import psycopg2.extras
from io import StringIO
from io import BytesIO
import datetime
from config import config

IntegrityError = psycopg2.IntegrityError

'''
name = None
class sql_cursor_dict(psycopg2.extensions.cursor(conn)):

    def _row_to_python(self, rowdata, desc=None):
        row = super(sql_cursor_dict, self)._row_to_python(rowdata, desc)
        if row:
            return dict(zip(self.column_names, row))
        return None
'''

class database(object):

    def __init__(self, config, pool_name='dbpool'):
        self.config = config
        self.pool_name = pool_name

    def execute_query(self, query, params=None):

        if params is not None and not isinstance(params, tuple) and not isinstance(params, dict):
            params = (params,)
        conn = psycopg2.connect(**self.config)
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        try:
            exec_result = cur.execute(query, params)
        except Exception as e:
            conn.close()
            raise e
        try:
            results = cur.fetchall()
            conn.commit()
        except:
            conn.commit()
            results = {'rows':cur.rowcount, 'lastrowid':cur.lastrowid}
        conn.close()
        return results
