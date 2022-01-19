from ineware.dataset_class import DatasetINE

"""
    INEware library potential can be better tested working with the dataset values. 
    We can send a heavy values list to a new file we can work with later on.
"""

if __name__ == '__main__':

    # Initialize a DatasetINE object using its url
    my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/22254"
    my_dataset = DatasetINE(my_url)

    # First let's see what this dataset is about by showing its name and notes
    print(my_dataset)

    print("------- Dataset notes --------")
    print(my_dataset.notes)
    print('---------------------------------')

    # We can print all the dataset values as a simple an intuitive list
    print("\n------- Dataset values --------")
    my_dataset.print_values_list()
    print('--------------------------------------------')

    # But maybe it is better to send this heavy list to a file. INEware does this using export_values()
    my_dataset.export_values("immigrants_homes.txt")
