import json
# importing the requests library
import requests
import itertools


class DatasetValue:
    def __init__(self, labels, value):
        self.labels = labels
        self.value = value

    def __str__(self):
        return str(self.labels) + " value: " + str(self.value)

    def get_labels(self):
        return self.labels

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
        self.save_values()

    def __str__(self):
        return "Dataset name = " + self.data['label'] + "\n" + "Dataset url = " + self.url

    def export_json(self, filename):
        print("exporting dataset to file", filename, "...")
        f = open(filename, "w", encoding='utf8')
        f.write(json.dumps(self.data, ensure_ascii=False, indent=4))
        f.close()
        print("file", filename, "saved")

    def export_values(self, filename):
        print("exporting values to file", filename, "...")
        f = open(filename, "w", encoding='utf8')
        for item in self.valuesList:
            my_string = str(item) + '\n'
            f.write(my_string)
        f.close()
        print("file", filename, "saved")

    def add_value(self, value):
        self.valuesList.append(value)

    def print_values_list(self):
        for item in self.valuesList:
            print(item)

    def get_value(self, **kwargs):
        result_list = []
        for value in self.valuesList:
            if exist_label(value, kwargs):
                result_list.append(value)
        if len(result_list) > 0:
            return result_list
        else:
            print('No values found for labels ' + str(kwargs))
            return []

    def print_values(self):
        print("________print_results call__________")
        j = 0
        if len(self.labels) < 3:
            for i in range(len(self.dict[self.labels[0]]) - 1):
                print("**", self.dict[self.labels[0]][i], '**')
                for item in self.dict[self.labels[1]]:
                    print("    ", item, 'value:', self.data['value'][j])
                    j += 1
        else:
            for item in self.dict[self.labels[0]]:
                print("**", item, '**')
                for item1 in self.dict[self.labels[1]]:
                    print("  ", item1)
                    for item2 in self.dict[self.labels[2]]:
                        print("    ", item2)
                        for item3 in self.dict[self.labels[3]]:
                            print("        ", item3, 'value:', self.data['value'][j])
                            j += 1

    def save_values(self):
        all_list = []
        for i in range(len(self.labels)):
            all_list.append(self.dict[self.labels[i]])

        res = list(itertools.product(*all_list))

        for item, value in zip(res, self.data['value']):
            my_labels = list(item)
            if value.is_integer():
                my_value = DatasetValue(my_labels, int(value))
            else:
                my_value = DatasetValue(my_labels, value)
            self.add_value(my_value)


def exist_label(value: DatasetValue, label):
    flag = False
    for item in value.get_labels():
        if item == label[0]:
            flag = True
    return flag
    # set1 = set(value.get_labels())
    # set2 = set(label)


def exist_label(value: DatasetValue, args):
    every_label_found = [False] * len(args)
    counter = 0
    final_flag = True
    for item in value.get_labels():
        for label in args.values():
            if item == label:
                every_label_found[counter] = True
                counter += 1
    for flag in every_label_found:
        if flag is False:
            final_flag = False
    return final_flag
    # set1 = set(value.get_labels())
    # set2 = set(label)
