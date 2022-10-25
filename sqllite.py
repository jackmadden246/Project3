import sqlite3
from time import time_ns
import threading


def db_establish(num_row):
    conn = sqlite3.connect('multithread.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEES(
                         EMPLOYEE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         EMPLOYEE_NAME VARCHAR(45),
                         EMPLOYEE_REGNO INTEGER);
                         """)
    start_time = time_ns()
    for i in range(num_row):
        cur.execute("""INSERT INTO EMPLOYEES 
                            (EMPLOYEE_NAME, EMPLOYEE_REGNO)
                            VALUES ("John", 123);
        """)
    finish_time = time_ns()
    print(finish_time - start_time)
    return finish_time - start_time


threads = []
thread_connection_1 = threading.Thread(target=db_establish, args=[50])
thread_connection_2 = threading.Thread(target=db_establish, args=[50])

thread_connection_1.start()
thread_connection_2.start()
thread_connection_1.join()
thread_connection_2.join()
print('Threads have now completed')
