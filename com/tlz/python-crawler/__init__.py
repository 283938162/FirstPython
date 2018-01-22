import requests
import json

url = 'http://music.163.com/api/song/lyric?'+ 'id=' + str(27566765)+ '&lv=1&kv=1&tv=-1'
r = requests.get(url)
json_obj = r.text

j = json.loads(json_obj)
print(j['lrc']['lyric'])
