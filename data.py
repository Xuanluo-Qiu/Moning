import json


# list转json
def list_tran_json(list):
    str_json = json.dumps(list, ensure_ascii=False, indent=2)
    return str_json

# json转list
def json_tran_list(str_json):
    list = json.loads(str_json)
    return list

# 写入数据
def change_data(file_name, data):
    fond = open(f"{file_name}", "a", encoding='utf-8')
    fond.write(f"{data}")
    fond.close()

# 读取数据
def read_data(file_name):
    fond = open(f"{file_name}", "r", encoding='utf-8')
    data = fond.read()  # 一次性读全部成一个字符串
    return data