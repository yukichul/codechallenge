import json
#from pprint import pprint

"""
Get full path on an element from the provided JSON.
"""

"""
Input: a string of the file name of the json file. (Store the file in the same
	directory as the find_path.py program.)
"""
def open_json(file_name):
	with open(file_name) as data_file:
		data = json.load(data_file)
	
	return data


"""
Input: a string of the item name, 
	a string of the file name of the json file.

Output: full path on an element in the json file.
"""
def find_path(item_name,file_name):
	json = open_json(file_name)
	path = '/itemList/'
	items = json['itemList']['items']

	for index in range(len(items)):
		if items[index]['id'] == item_name:
			path = path + 'items[' + str(index) + ']/id'
			return path
		elif 'label' in items[index] and items[index]['label'] == item_name:
			path = path + 'items[' + str(index) + ']/label'
			return path
		elif 'subItems' in items[index]:
			if type(items[index]['subItems']) == type([]):
				subItems = items[index]['subItems']
				for index1 in range(len(subItems)):
					if subItems[index1]['id'] == item_name:
						path = path + 'items[' + str(index) + ']/subItems['+str(index1)+']/id'
						return path
					elif 'label' in subItems[index1] and subItems[index1]['label'] == item_name:
						path = path + 'items[' + str(index) + ']/subItems['+str(index1)+']/label'
						return path
			else:
				if items[index]['subItems']['id'] == item_name:
					path = path + 'items[' + str(index) + ']/subItems/id'
					return path
				elif items[index]['subItems']['label'] == item_name:
					path = path + 'items[' + str(index) + ']/subItems/label'
					return path 
	return 'Object not Found'

def test():
	print "Expected: /itemList/items[5]/subItems[0]/id\nActual:   " + find_path('subItem1Item1','data.json')
	print "Expected: /itemList/items[0]/id\nActual:   " + find_path('item1','data.json')
	print "Expected: /itemList/items[1]/id\nActual:   " + find_path('item2','data.json')
	print "Expected: /itemList/items[1]/label\nActual:   " + find_path('Item 2','data.json')
	print "Expected: /itemList/items[5]/id\nActual:   " + find_path('subItem1','data.json')
	print "Expected: /itemList/items[8]/subItems/label\nActual:   " + find_path('SubItem 2 item1','data.json')


# Given json
"""
data = {"itemList": {"items": [
    {"id": "item1"},
    {"id": "item2","label": "Item 2"},
    {"id": "item3"},
    {"id": "item4"},
    {"id": "item5"},
    {"id": "subItem1",
        "subItems": [
            {"id": "subItem1Item1","label": "SubItem 1"},
            {"id": "subItem1Item2","label": "SubItem 2"},
            {"id": "subItem1Item3","label": "SubItem 3"}
        ]
    },
    {"id": "item6"},
    {"id": "item7","label": "Item 7"},
    {"id": "subItem2",
        "subItems": {"id": "item1","label": "SubItem 2 item1"}
    }
]}}
"""
		
#test()
