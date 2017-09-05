import pymysql
conn = pymysql.connect(host='localhost',user = 'root',passwd = '315315',db = 'student')
cursor = conn.cursor()
effect_row = cursor.execute('select * from study_record')
# print(cursor.fetchall())
data = [
    ('3','No',1),
    ('3','Yes',2),
    ('4','Yes',1),
    ('4','YES',2),
]
cursor.executemany('insert into study_record (day,status,stu_id) values (%s,%s,%s)',data)
conn.commit()
conn.close()