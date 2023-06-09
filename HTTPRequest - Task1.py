import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'

resp = requests.get(url)
heroes_json_data = resp.json()

heroes_dict = {}
for data in heroes_json_data:
    if data['name'] == 'Hulk' or data['name'] == 'Captain America' or data['name'] == 'Thanos':
        heroes_dict[data['name']]=data["powerstats"]["intelligence"]

heroes_dict_sort = sorted(heroes_dict.items(), key=lambda x: x[1], reverse=True)

print(f'Из трёх обозначенных супергероев самый умный - {heroes_dict_sort[0][0]} c уровнем интеллекта - {heroes_dict_sort[0][1]},\n'
      f'следом - {heroes_dict_sort[1][0]} c уровнем интеллекта - {heroes_dict_sort[1][1]},\n'
      f'последний - {heroes_dict_sort[2][0]} c уровнем интеллекта - {heroes_dict_sort[2][1]}!')
