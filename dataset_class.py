import json
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
        if request_error_handler(url):
            self.data = requests.get(url).json()
            self.values = self.data['value']
            self.notes = str(self.data['note'])
            self.valuesList = []
            self.labels, self.dict = self.create_dict()
            self.save_values()

    def __str__(self):
        return "------- Dataset info --------\n" + \
               "Name = " + self.data['label'] + "\n" +\
               "url = " + self.url + "\n" +\
               "-----------------------------\n"

    def create_dict(self):
        new_dict = {}
        my_labels = []
        for key, value in self.data['dimension'].items():
            new_dict[value['label']] = {}
            my_labels.append(value['label'])
            aux_list = []
            for key1, value1 in value['category']['label'].items():
                aux_list.append(value1)
            new_dict[value['label']] = aux_list
        return my_labels, new_dict

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


def exist_label(value: DatasetValue, args):
    label_found = [False] * len(args)
    counter = 0
    final_flag = True
    for item in value.get_labels():
        for label in args.values():
            if item == label:
                label_found[counter] = True
                counter += 1
    for flag in label_found:
        if flag is False:
            final_flag = False
    return final_flag


def request_error_handler(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return True
    except requests.exceptions.HTTPError as err_h:
        print("Http Error:", err_h)
    except requests.exceptions.ConnectionError as err_c:
        print("Error Connecting:", err_c)
    except requests.exceptions.Timeout as err_t:
        print("Timeout Error:", err_t)
    except requests.exceptions.RequestException as err:
        print("Oops: Something happened!", err)
