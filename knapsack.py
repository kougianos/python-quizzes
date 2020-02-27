# Knapsack
# Quiz URL:
# 	https://edabit.com/challenge/oFwoAA62gRvX5agEN
# Quiz description:
# 	Given a knapsack with a certain weight capacity, fill it with loot from a list of items to achieve the highest value possible.
import pprint

items = [
	{'name':"desk lamp",		'weight':2,	'value':12},
	{'name':"beach towel",		'weight':1,	'value':10},
	{'name':"textbook",		'weight':3,	'value':20},
	{'name':"wall clock",		'weight':2,	'value':15},
	{'name':"frozen dinners",	'weight':10,	'value':50},
	{'name':"tablet",		'weight':7,	'value':1400},
	{'name':"smartphone",		'weight':1,	'value':200},
	{'name':"paper",		'weight':2,	'value':5},
	{'name':"laser printer",	'weight':25,	'value':400},
	{'name':"shoes",		'weight':1,	'value':79},
	{'name':"medicine",		'weight':1,	'value':17},
	{'name':"decorative cushion",	'weight':1,	'value':11},
	{'name':"gold necklace",	'weight':1,	'value':2500},
	{'name':"toaster oven",		'weight':5,	'value':129}
]

items2 = [
	{'name':"desk lamp",'weight':2,'value':12},
	{'name':"textbook",'weight':3,'value':20},
	{'name':"wall clock",'weight':2,'value':15},
	{'name':"frozen dinners",'weight':10,'value':50},
	{'name':"tablet",'weight':7,'value':1400},
	{'name':"smartphone",'weight':1,'value':200},
	{'name':"paper",'weight':2,'value':5},
	{'name':"laser printer",'weight':25,'value':400},
	{'name':"shoes",'weight':1,'value':79},
	{'name':"medicine",'weight':1,'value':17},
	{'name':"toaster oven",'weight':5,'value':129}
]

items3 = [
	{'name':"desk lamp",'weight':1,'value':1000},
	{'name':"beach towel",'weight':29,'value':900},
	{'name':"textbook",'weight':1,'value':899},
	{'name':"wall clock",'weight':1,'value':850},
]

def knapsack(capacity, items):
	pp = pprint.PrettyPrinter(indent=2)
	for key, item in enumerate(items):
		items[key]['realValue'] = item['value'] / item['weight']

	items = sorted(items, key = lambda k: (-k['value'], -k['realValue']))

	dictToReturn = {
		'capacity': capacity,
		'items': [],
		'weight': 0,
		'value': 0
	}

	for item in items:
		if(item['weight'] <= capacity):
			del item['realValue']
			dictToReturn['items'].append(item)
			dictToReturn['weight'] += item['weight']
			dictToReturn['value'] += item['value']
			capacity -= item['weight']

	pp.pprint(dictToReturn)
	return dictToReturn

# Test first dataset
knapsack(0, items)
knapsack(1, items)
knapsack(5, items)
knapsack(14, items)

# Test second dataset
knapsack(31, items2)
knapsack(36, items2)
knapsack(100, items2)

# Test third dataset - FAILS
knapsack(30, items3)
