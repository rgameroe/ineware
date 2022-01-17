import unittest
import requests
import pathlib as pl
import os
from dataset_class import DatasetINE, DatasetValue


class TestDatasetINEClass(unittest.TestCase):

    def test_init(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=2"
        my_dataset = DatasetINE(my_url)
        data = requests.get(my_url).json()

        self.assertEqual(my_url, my_dataset.url)
        self.assertEqual(data, my_dataset.data)
        self.assertEqual(data['value'], my_dataset.values)
        self.assertEqual(str(data['note']), my_dataset.notes)
        self.assertTrue(my_dataset.valuesList)

    def test_create_dict(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=2"
        my_dataset = DatasetINE(my_url)
        new_dict = {}
        my_labels = []
        my_labels, new_dict = my_dataset.create_dict()
        self.assertEqual(new_dict, my_dataset.dict)
        self.assertTrue(my_labels, my_dataset.labels)

    def test_add_value(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2065?nult=2"
        my_dataset = DatasetINE(my_url)

        my_value = DatasetValue(['Melilla', '2021M12'], 2.33)
        my_dataset.add_value(my_value)
        self.assertIn(my_value, my_dataset.valuesList)

    def test_export_json(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2065?nult=2"
        my_dataset = DatasetINE(my_url)
        my_path = pl.Path("test_file.json")
        my_dataset.export_json(my_path)
        self.assertTrue(my_path.is_file())
        os.remove(my_path)

    def test_export_values(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2065?nult=2"
        my_dataset = DatasetINE(my_url)
        my_path = pl.Path("test_file.json")
        my_dataset.export_values(my_path)
        self.assertTrue(my_path.is_file())
        os.remove(my_path)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
