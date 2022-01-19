from ineware.dataset_class import DatasetINE

"""
    INEware also lets you work with the dataset values as you want. As they are stored as a simple list,
    where each element is uniquely identified by its labels, the effort to get specific values is 
    reduced by far.
"""

if __name__ == '__main__':

    # Initialize the DatasetINE object using its url
    # This url can be modified with a "date" parameter. In this case year 2020 (since 1st January to 31th December)
    # For more information on how to define urls, visit https://www.ine.es/dyngs/DataLab/manual.html?cid=1259945947375
    my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2074?date=20200101:20201231"
    my_dataset = DatasetINE(my_url)

    # Print name of the dataset and unit of measure just to know what we are working with
    print(my_dataset)
    print("------- Dataset notes --------")
    print(my_dataset.notes)
    print('---------------------------------')

    # Suppose we want to get only the number of Almería foreign travelers in each month of 2020
    # As method get_value() returns a list, we can iterate over each value in a simple way to show them
    print("\n------- Almería foreign travelers 2020 --------")
    for item in my_dataset.get_value(Provincia="Almería", ViajerosPernoctaciones="Viajero", Residencia="Residentes en el Extranjero"):
        print(item)
    print("-------------------------------------------------")

    # If we look for a label that does not exists, INEware will show a warning message
    print("------- No values found example ----------")
    for item in my_dataset.get_value(Provincia="AÑMERIA", Residencia="Residentes en España"):
        print(item)
    print("------------------------------------------")

    # If we do not remember what are the names of the labels in this dataset we can call my_dataset.dimLabels
    print("\n------- Dataset dimensions and labels --------")
    print(my_dataset.dimLabels)
    print("----------------------------------------------")

    # Imagine now we want to know the average number of Almería foreign travelers during year 2020
    total = 0
    for item in my_dataset.get_value(Provincia="Almería", ViajerosPernoctaciones="Viajero", Residencia="Residentes en el Extranjero"):
        total += item.get_value()  # We can access the numeric value of each item by get_value() inner method

    print("\n------- Average number per month of Almería foreign travelers 2020 --------")
    print(total/12)
    print("---------------------------------------------------------------------------")



