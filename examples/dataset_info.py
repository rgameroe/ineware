from ineware.dataset_class import DatasetINE
import json

"""
    Thanks to INEware library you can get any info you need from INE datasets in a really simple way.
    Just access the different attributes of the DatasetINE object and use them as you need!
"""

if __name__ == '__main__':

    # Initialize a DatasetINE object using its url
    my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387"
    my_dataset = DatasetINE(my_url)

    # Show dataset info by just printing it!
    print(my_dataset)

    # Show dataset notes
    print("------- Dataset notes --------")
    print(my_dataset.notes)
    print('---------------------------------')

    # Show dataset dimensions or attributes
    print("\n------- Dataset dimensions --------")
    print(my_dataset.dimensions)
    print('---------------------------------')

    # Show dataset dimensions and labels for each one
    # We reformat this dictionary by simply applying some indentation and removing ascii characters
    formatted_dict = json.dumps(my_dataset.dimLabels, indent=4, ensure_ascii=False)
    print("\n------- Dataset dimensions and labels --------")
    print(formatted_dict)
    print("\n----------------------------------------------")
