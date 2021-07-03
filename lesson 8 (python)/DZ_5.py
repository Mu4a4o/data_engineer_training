import requests
import json
def dict_url(ssilka):
 json_obj = json.loads(requests.get(ssilka).text)
 #print(type(json_obj), json_obj)
 return json_obj

#dict_url("https://jsonplaceholder.typicode.com/users/7")

def join_dict(*slovari):
 new_slow = {}
 for i in range(len(slovari)):
  for key, value in slovari[i].items():
   new_slow[key] = slovari[i][key]
 #print(type(new_slow), new_slow)
 return new_slow

#join_dict({5: 3, 6: 'a'}, {1: 8, 2: 'k'})

def save_file_json(slovar, json_file):
 with open(json_file, "w") as write_file:
  json.dump(slovar, write_file)

#save_file_json({5: 8, 6: 'a', 7: 'o'}, 'C:/Users/SoVYakovleva/Desktop/Python_lessons/json_file.json')

p = dict_url("https://jsonplaceholder.typicode.com/users/7")
s = dict_url("https://jsonplaceholder.typicode.com/albums/1")
l = dict_url("https://jsonplaceholder.typicode.com/comments/5")
save_file_json(join_dict(p, s, l), 'C:/Users/SoVYakovleva/Desktop/Python_lessons/json_file.json')


