import psycopg2
from config import db_pass


class db_connection:
    """ Connection to postgres db  """

    conn = psycopg2.connect(
        database = 'hh',
        user     = 'phz',
        password = db_pass,
        host     =  'localhost',
        port     =   '5432'
    )

    print('Connection successfully!')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 20, 'Computer Science', 'ICT')"
    )
    conn.commit()
    print("insert success")
    conn.close()
