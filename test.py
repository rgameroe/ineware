from dataset_class import DatasetINE

if __name__ == '__main__':
    # my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=4"
    # my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/22254?nult=3"
    # my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2065?nult=6"
    my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2074?nult=5"

    my_dataset = DatasetINE(my_url)
    # print(my_dataset)
    # print(my_dataset.notes)
    # my_dataset.export_values('pruebaValores')
    for item in my_dataset.get_value('Cácerfes'):
        print(item)

    # print(my_dataset.labels)
    # print('---------------')
    # print(my_dataset.dict)
    # print('---------------')
    # print(my_dataset)
    # print('---------------')
    # print(my_dataset.notes)
    # print('---VALUES---')
    # my_dataset.final_loop()
    # print(my_dataset.dict)

    # print('---get value---')
    # my_dataset.save_values()
    # print(my_dataset.get_value('Cáceres', '2021M06'))
    # print('---more than one---')
    # for item in my_dataset.get_value('', '2021M06'):
    #     print(item)

    # my_dataset.export_json("estancia_media_turismo.json")

    # counter = 1
    # for value in my_dataset.values:
    #     print("Value number ", counter, " : ", value)
    #     counter += 1
    #
    # print(my_dataset.values)

    # my_dataset.print_values()
