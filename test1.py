import mysql.connector
import json


def init():
    #  =============        MYSQL        =============
    DB_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "123@",
        "database": "jumingshi",
        "port": "63736"
    }

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # JSON数据
    # 指定JSON文件的路径
    json_file_path = 'temp.json'

    # 打开并读取JSON文件
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)


    # 遍历items列表，插入数据
    for item in json_data['result']['items']:
        # 构造插入语句
        insert_sql = """
        INSERT INTO college_info (
            belong, categories, city_name, cn_name, code, com_score, edu_level, features, gb_code, platform_id, logo_url, num_id, province_code, province_name, ranking, ranking_edu
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        """
        # 构造参数
        insert_params = (
            item['belong'],
            ','.join(item['categories']),
            item['cityName'],
            item['cnName'],
            item['code'],
            item['comScore'],
            item['eduLevel'],
            ','.join(item['features']),
            item['gbCode'],
            item['id'],  # 假设id字段对应platform_id
            item['logoUrl'],
            item['numId'],
            item['provinceCode'],
            item['provinceName'],
            item['ranking'],
            item['rankingOfEdu']  # 假设rankingOfEdu字段对应ranking_edu
        )
        # 执行插入语句
        cursor.execute(insert_sql, insert_params)

    # 提交事务
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # lab_id = 'cc9de70b56d046bfa5c7afaeb5080b6c'
    init()
