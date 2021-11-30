import json
# importing the requests library
import requests


class DatasetValue:
    def __init__(self, label1, label2, value):
        self.label1 = label1
        self.label2 = label2
        self.value = value

    def __str__(self):
        return " " + self.label1 + ", " + self.label2 + ", value: " + str(self.value)

    def get_label1(self):
        return str(self.label1)

    def get_label2(self):
        return str(self.label2)

    def get_value(self):
        return self.value


class DatasetINE:
    def __init__(self, url):
        self.url = url
        self.data = requests.get(url).json()
        self.values = self.data['value']
        self.notes = self.data['note']
        self.valuesList = []

        new_dict = {}
        my_labels = []
        for key, value in self.data['dimension'].items():
            new_dict[value['label']] = {}
            my_labels.append(value['label'])
            aux_list = []
            for key, value1 in value['category']['label'].items():
                aux_list.append(value1)
            new_dict[value['label']] = aux_list
        self.labels = my_labels
        self.dict = new_dict

    def __str__(self):
        return "Dataset name = " + self.data['label'] + "\n" + "Dataset url = " + self.url

    def export_json(self, filename):
        print("exporting dataset to file", filename, "...")
        f = open(filename, "w", encoding='utf8')
        f.write(json.dumps(self.data, ensure_ascii=False, indent=4))
        f.close()
        print("file", filename, "saved")

    def add_value(self, value):
        self.valuesList.append(value)

    def print_values_list(self):
        for item in self.valuesList:
            print(item)

    def get_value(self, label1, label2):
        if label2 == '':
            for item in self.valuesList:
                if item.label1 == label1:
                    print(item)
        if label1 == '':
            for item in self.valuesList:
                if item.label2 == label2:
                    print(item)
        else:
            for item in self.valuesList:
                if item.label1 == label1 and item.label2 == label2:
                    return item
            return 'Labels not found'

    def print_values(self):
        print("________print_results call__________")
        j = 0
        if len(self.labels) < 3:
            for i in range(len(self.dict[self.labels[0]]) - 1):
                print("**", self.dict[self.labels[0]][i], '**')
                y = 0
                for item in self.dict[self.labels[1]]:
                    print("    ", self.dict[self.labels[1]][y], 'value:', self.data['value'][j])
                    y += 1
                    j += 1
        else:
            for i in range(len(self.labels[0])):
                print("**", self.dict[self.labels[0]][i], '**')
                y = 0
                for item in self.dict[self.labels[1]]:
                    print("  ", self.dict[self.labels[1]][y])
                    y += 1
                    l = 0
                    for item in self.dict[self.labels[2]]:
                        print("    ", self.dict[self.labels[2]][l])
                        l += 1
                        r = 0
                        for item in self.dict[self.labels[3]]:
                            print("        ", self.dict[self.labels[3]][r], 'value:', self.data['value'][j])
                            j += 1

    def print_values_2(self):
        print("________print_results call__________")
        label_index = 0
        j = 0
        counters = [0] * len(self.labels)
        while True:
            if counters[label_index] >= len(self.dict[self.labels[label_index]]):
                counters[label_index] = 0
                label_index -= 1
                counters[label_index] += 1
            print(self.dict[self.labels[label_index]][counters[label_index]])
            label_index += 1
            if label_index == len(self.labels) - 1:
                y = 0
                for item in self.dict[self.labels[label_index]]:
                    if j < len(self.values):
                        print('    ', self.dict[self.labels[label_index]][y], 'value:', self.data['value'][j])
                        y += 1
                        j += 1
                    else:
                        break
                label_index -= 1
                counters[label_index] += 1
                if counters[0] == len(self.dict[self.labels[0]]):
                    break

    def save_values(self):
        label_index = 0
        j = 0
        counters = [0] * len(self.labels)
        while True:
            if counters[label_index] >= len(self.dict[self.labels[label_index]]):
                counters[label_index] = 0
                label_index -= 1
                counters[label_index] += 1
            label_index += 1
            if label_index == len(self.labels) - 1:
                y = 0
                for item in self.dict[self.labels[label_index]]:
                    if j < len(self.values):
                        label1 = self.dict[self.labels[label_index-1]][counters[label_index-1]]
                        label2 = self.dict[self.labels[label_index]][y]
                        my_value = DatasetValue(label1, label2, self.data['value'][j])
                        self.add_value(my_value)
                        y += 1
                        j += 1
                    else:
                        break
                label_index -= 1
                counters[label_index] += 1
                if counters[0] == len(self.dict[self.labels[0]]):
                    break
