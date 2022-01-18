import unittest
import requests
import pathlib as pl
import os
import logging as log
from ineware.dataset_class import DatasetINE, DatasetValue, exist_label, request_error_handler


class TestDatasetINEClass(unittest.TestCase):

    def test_init(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=2"
        my_dataset = DatasetINE(my_url)
        data = requests.get(my_url).json()

        self.assertEqual(my_url, my_dataset.url)
        self.assertEqual(data, my_dataset.data)
        self.assertEqual(data['value'], my_dataset.values)
        self.assertEqual(str(data['note']), my_dataset.notes)
        self.assertTrue(my_dataset.datasetValues)

    def test_create_dict(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=2"
        my_dataset = DatasetINE(my_url)
        new_dict = {}
        my_labels = []
        my_labels, new_dict = my_dataset.create_dict()
        self.assertEqual(new_dict, my_dataset.dimLabels)
        self.assertTrue(my_labels, my_dataset.dimensions)

    def test_add_value(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2065?nult=2"
        my_dataset = DatasetINE(my_url)

        my_value = DatasetValue(['Melilla', '2021M12'], 2.33)
        my_dataset.add_value(my_value)
        self.assertIn(my_value, my_dataset.datasetValues)

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

    def test_get_value(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=4"
        my_dataset = DatasetINE(my_url)
        expected_result = DatasetValue(['Hombres', '20 años', '2021S1'], 2352)
        actual_result = my_dataset.get_value(Sexo="Hombres", Edad="20 años", Periodo="2021S1")
        self.assertEqual(len(actual_result), 1)
        self.assertEqual(expected_result, actual_result[0])

    def test_exist_label(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=4"
        my_dataset = DatasetINE(my_url)
        test_value = DatasetValue(['20 años', '2020S1'], 2352)
        my_args_correct = {"Edad": "20 años", "Periodo": "2020S1"}
        my_args_incorrect = {"Edad": "35 años"}
        self.assertTrue(exist_label(test_value, my_args_correct))
        self.assertFalse(exist_label(test_value, my_args_incorrect))

    def test_request_error(self):
        invalid_url = "https://ser*ERROR_IN_URL*.ine.es/wstempus/jsstat/ES/DATASET/24387"
        valid_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387"
        self.assertFalse(request_error_handler(invalid_url))
        self.assertTrue(request_error_handler(valid_url))


if __name__ == '__main__':
    unittest.main()
