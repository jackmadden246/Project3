cur_1 = conn_1.cursor()
cur_1.execute("""CREATE TABLE IF NOT EXISTS multi_test_table (

            test_id INTEGER PRIMARY KEY AUTOINCREMENT,

            name VARCHAR(20),

            some_number INTEGER

            );""")

cur_1.execute(''' INSERT INTO multi_test_table 
(name, some_number) 
VALUES ('Chris', 1);''')

start_time = time_ns()
for i in range(100):

    cur_1.execute(''' INSERT INTO multi_test_table 
    (name, some_number) 
    VALUES ('Chris', 1);''')
finish_time = time_ns()
print(f'took {finish_time - start_time}ns')
# 100 lines of data using single connection