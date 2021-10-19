import json

# importing the requests library
import requests
  
# api-endpoint
URL = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=4"
  
  
# sending get request and saving the response as response object
r = requests.get(URL)
  
# extracting data in json format
data = r.json()

# print(data['dimension'])

dimension = data['dimension'] 
values = data['value']  
labels = data['dimension']['sexo']['category']['label']
print (len(dimension))
for i in range(3):
    print (values[i])

print('labels:')

class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)

values = obj(data)

# i = 0
# for value in values.value:
#     print(value)
#     i+=1
# print('total: ',i) 

# for key in data:
#     print(key)

# for item in data.items():
#     print(item)

newDict = {}
myLabels = []
for key, value in data['dimension'].items():
    # print(key, '->', value)
    newDict[value['label']] = {}
    myLabels.append(value['label'])
    list = []
    for key, value1 in value['category']['label'].items():
        list.append(value1)
    newDict[value['label']] = list

print ("_------------------_")

j = 0
for i in range(len(myLabels)):
    print("**",newDict[myLabels[0]][i],'**')
    y = 0
    for item in newDict[myLabels[1]]:
        print("  ",newDict[myLabels[1]][y])
        y+=1
        l = 0
        for item in newDict[myLabels[2]]:
            print("    ",newDict[myLabels[2]][l], 'value:', data['value'][j])
            l+=1
            j+=1

# for key in dimension:
#     for newkey in dimension[key]['category']['label']:
#         print('***',dimension[key]['category']['label'][newkey],'***')

# f = open("resultsINE.json", "w", encoding='utf8') #wb unicode
# f.write(json.dumps(data, indent=4, ensure_ascii=False))
# f.close()
