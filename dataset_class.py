import json
# importing the requests library
import requests


class DatasetINE:
    def __init__(self, url):
        self.url = url
        self.data = requests.get(url).json()
        self.values = self.data['value']

        new_dict = {}
        my_labels = []
        for key, value in self.data['dimension'].items():
            new_dict[value['label']] = {}
            my_labels.append(value['label'])
            aux_list = []
            for key2, value1 in value['category']['label'].items():
                aux_list.append(value1)
            new_dict[value['label']] = aux_list
        self.labels = my_labels
        self.dict = new_dict

    def __str__(self):
        return "Dataset name = " + self.data['label'] + "\n" + "Dataset url = " + self.url

    def export_json(self, filename):
        print("exporting dataset to file", filename, "...")
        f = open(filename, "w", encoding='utf8')
        f.write(json.dumps(self.data, indent=4, ensure_ascii=False))
        f.close()
        print("file", filename, "saved")

    def print_values(self):
        print("________print_results call__________")
        j = 0
        if len(self.labels) < 3:
            for i in range(len(self.labels[0]) - 1):
                print("**", self.dict[self.labels[0]][i], '**')
                y = 0
                for item in self.dict[self.labels[1]]:
                    print("    ", self.dict[self.labels[1]][y], 'value:', self.data['value'][j])
                    y += 1
                    j += 1
        else:
            for i in range(len(self.labels)):
                print("**", self.dict[self.labels[0]][i], '**')
                y = 0
                for item in self.dict[self.labels[1]]:
                    print("  ", self.dict[self.labels[1]][y])
                    y += 1
                    l = 0
                    for item in self.dict[self.labels[2]]:
                        print("    ", self.dict[self.labels[2]][l], 'value:', self.data['value'][j])
                        l += 1
                        j += 1


#my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=4"
my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/22254?nult=3"
my_dataset = DatasetINE(my_url)

print(my_dataset.labels)
print('---------------')
print(my_dataset.dict)

print(my_dataset)

# counter = 1
# for value in my_dataset.values:
#     print("Value number ", counter, " : ", value)
#     counter += 1
#
# print(my_dataset.values)

# my_dataset.print_values()
