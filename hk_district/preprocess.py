# filter the orginal json with only 3 fields: region, ename and coordinates

import json

fn = "./data/raw/district.full.json"

with open(fn, 'r', encoding='utf-8') as f:
    data = json.load(f)

result = dict()
counter = 0
for i in range(0, len(data)):
	#print(data[i].keys()) # dict_keys(['population', 'GeoJSON', 'electors', 'iconSrc', 'seats', 'region', 'ename', 'exOfficio', 'cname'])
	#print(data[i]['region'])
	#print(data[i]['ename'])
	# check if it is GeometryCollection
	if ("GeometryCollection" == (data[i]['GeoJSON']['geometry']['type'])):
		geometries_list = (data[i]['GeoJSON']['geometry']['geometries'])
		for l in geometries_list:
			coords = l['coordinates'][0]
			counter = counter + 1
			d = dict()
			d['region'] = data[i]['region']
			d['ename']  = data[i]['ename']
			d['coords'] = coords
			result[counter] = d
	else: #Polygon
		coordinates_list = (data[i]['GeoJSON']['geometry']['coordinates'])
		print(coordinates_list)
		for coords in coordinates_list:
			counter = counter + 1
			d = dict()
			d['region'] = data[i]['region']
			d['ename']  = data[i]['ename']
			d['coords'] = coords
			result[counter] = d
			


with open('./data/interim/district.full.json', 'w') as fp:
    json.dump(result, fp)