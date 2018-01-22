
import json

# python 字典类型转换为JSON对象

data = {
    'no':1,
    'name':'runoob',
    'url':'www.runoob.com'
}

# print(data)
#
json_str = json.dumps(data)  # str转json兑现
#
json_python = json.loads(json_str)

print(json_python['no'])

# print(repr(data))
#
# print(json_str)

