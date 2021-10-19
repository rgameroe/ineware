import json

# importing the requests library
import requests
  
# api-endpoint
#movimientos migratorios: "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=4"
#datos demograficos "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/6566"
#hogares inmigrantes "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/22254?nult=3"
URL = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=4"
  
  
# sending get request and saving the response as response object
r = requests.get(URL)
  
# extracting data in json format
data = r.json()

# f = open("hogares_inmigrantes.json", "w", encoding='utf-8') #wb unicode
# f.write(json.dumps(data, indent=4, ensure_ascii=False))
# f.close()

# print(data['dimension'])

dimension = data['dimension'] 
values = data['value']  
#labels = data['dimension']['sexo']['category']['label']

"""
print (len(dimension))
for i in range(3):
    print (values[i])
"""

# class obj(object):
#     def __init__(self, d):
#         for a, b in d.items():
#             if isinstance(b, (list, tuple)):
#                setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
#             else:
#                setattr(self, a, obj(b) if isinstance(b, dict) else b)

# values = obj(data)

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

def check_labels(dict, myLabels):
    print ("Dict:")
    for key, value in dict.items():
        print(key, '->', value)
    print ("my labels:")
    for label in myLabels:
        print(label)

check_labels(newDict, myLabels)



def export_results(newDict, myLabels):
    f = open("demofile2.txt", "w", encoding='utf-8')
    j = 0
    for i in range(len(myLabels)):
        text = "**"+str(newDict[myLabels[0]][i])+'**'+'\n'
        f.write(text)
        y = 0
        for item in newDict[myLabels[1]]:
            text = "  "+str(newDict[myLabels[1]][y])+'\n'
            f.write(text)
            y+=1
            l = 0
            for item in newDict[myLabels[2]]:
                text = "    "+str(newDict[myLabels[2]][l])+' value: '+ str(data['value'][j])+'\n'
                f.write(text)
                l+=1
                j+=1
    f.close()

"""
print ("Exporting results")
export_results(newDict, myLabels)
print("End of exporting results")
"""
def print_results():
    print("________print_results call__________")
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

def print_results_prueba():
    print("________print_results call__________")
    j = 0
    if(len(myLabels) < 3):
        for i in range(len(myLabels[0]) - 1):
            print("**",newDict[myLabels[0]][i],'**')
            y = 0
            for item in newDict[myLabels[1]]:
                print("    ",newDict[myLabels[1]][y], 'value:', data['value'][j])
                y+=1
                j+=1
    else:
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

print_results_prueba()
# for key in dimension:
#     for newkey in dimension[key]['category']['label']:
#         print('***',dimension[key]['category']['label'][newkey],'***')

# f = open("resultsINE.json", "w", encoding='utf8') #wb unicode
# f.write(json.dumps(data, indent=4, ensure_ascii=False))
# f.close()
