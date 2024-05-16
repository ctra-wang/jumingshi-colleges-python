import mysql.connector
import json


def init():
    #  =============        MYSQL        =============
    DB_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "123@",
        "database": "jumingshi",
        "port": "3306"
    }

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    # 指定JSON文件的路径
    json_file_path = 'temp.json'

    # 打开并读取JSON文件
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    # 解析JSON数据


    # 处理综合课程的数据
    for course in json_data['result'][0]['courses']:
        for college in course['colleges']:
            print(college)
            if college['year'] >= 2019:
                # 构建插入语句
                insert_sql = f"""
                INSERT INTO college_score (college_type, year, college_name, college_source_name, college_name_text, college_enroll_code, batch, enter_num, max_score, min_score, avg_score, min_rank, zj_text, zj_text_explain)
                VALUES ('{course["name"]}', {college['year']}, '{college['collegeName']}', '{college['collegeSourceName']}', '{college['collegeNameText']}', '{college['collegeEnrollCode']}', '{college['batches'][0]['batch']}', {college['batches'][0]['enterNum']}, '{college['batches'][0]['maxScore']}', '{college['batches'][0]['minScore']}', '{college['batches'][0]['avgScore']}', '{college['batches'][0]['minRank']}', '{college['batches'][0]['zjText']}', '{college['batches'][0]['zjTextExplain']}')
                """
                # 执行插入语句
                cursor.execute(insert_sql)
    print("-----------")
    # 处理理科和文科课程的数据
    for course in json_data['result'][1]['courses']:
        for college in course['colleges']:
            if college['year'] >= 2019:
                # 构建插入语句
                insert_sql = f"""
                INSERT INTO college_score (college_type, year, college_name, college_source_name, college_name_text, college_enroll_code, batch, enter_num, max_score, min_score, avg_score, min_rank, zj_text, zj_text_explain)
                VALUES ('{course["name"]}', {college['year']}, '{college['collegeName']}', '{college['collegeSourceName']}', '{college['collegeNameText']}', '{college['collegeEnrollCode']}', '{college['batches'][0]['batch']}', {college['batches'][0]['enterNum']}, '{college['batches'][0]['maxScore']}', '{college['batches'][0]['minScore']}', '{college['batches'][0]['avgScore']}', '{college['batches'][0]['minRank']}', '{college['batches'][0]['zjText']}', '{college['batches'][0]['zjTextExplain']}')
                """
                # 执行插入语句
                cursor.execute(insert_sql)

    # 提交事务
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # lab_id = 'cc9de70b56d046bfa5c7afaeb5080b6c'
    init()
