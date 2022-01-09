import unittest
from dataset_class import DatasetINE, DatasetValue


class TestDatasetINEClass(unittest.TestCase):

    def test_add_value(self):
        my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2065?nult=2"
        my_dataset = DatasetINE(my_url)

        my_value = DatasetValue(['Melilla', '2021M12'], 2.33)
        my_dataset.add_value(my_value)
        self.assertIn(my_value, my_dataset.valuesList)

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