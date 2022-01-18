from ineware.dataset_class import DatasetINE

if __name__ == '__main__':
    my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=4"
    # my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/22254?nult=3"
    # my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2065"
    # my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2074?nult=1"
    # my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2074?"

    my_dataset = DatasetINE(my_url)
    # print(my_dataset.print_values_list())
    for item in my_dataset.datasetValues:
        print(item)

    """
    my_dataset = DatasetINE(my_url)
    formatted_dict = json.dumps(my_dataset.dict, indent=4, ensure_ascii=False)
    my_dataset.print_values_list()
    print(my_dataset.notes)
    print("\n------- Dataset labels types --------")
    print(my_dataset.labels)
    print('---------------------------------')
    print("\n------- Dataset labels --------")
    print(formatted_dict)
    print('--------------------------------------------')
    print("\n------- Dataset values --------")
    my_dataset.print_values_list()
    print('--------------------------------------------')
    for item in my_dataset.get_value(Sexo="Hombres", Edad="20 años", Periodo="2021S1"):
        print(item)
    print('--------------')
    for item in my_dataset.get_value(Sexo="Hombres", Edad="21 años"):
        print(item)
    """

