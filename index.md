# INEware

INEware is a lightweight Python library that works as a middleware between the client and the API json-stat that [INE](https://www.ine.es/) 
(Instituto Nacional de Estadística) offers to its users.

This library is designed to facilitate the handling of data from INE datasets, as well as integrating them into a 
programmatic environment where we can get the most out of this valuable information.

## Installation

INEware package is available as an open source library published at [PyPI](https://pypi.org/project/ineware/).
You can install INEware by simply executing this command:
```bash
pip install ineware
```
If you already have installed ineware, you can upgrade it using:
```bash
pip install ineware --upgrade
```

## Kick off

The first step to use INEware is creating our DatasetINE object. Simply pass the url of the dataset you 
want to use as argument and you will have your dataset object ready!

```python
from ineware.dataset_class import DatasetINE

# Initialize a DatasetINE object using its url.
my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387"
my_dataset = DatasetINE(my_url)
```

### Show Dataset info

Thanks to INEware library you can get any info you need from INE datasets in a really simple way.
Just access the different attributes of the DatasetINE object and use them as you need!

```python
from ineware.dataset_class import DatasetINE
import json

if __name__ == '__main__':
    # Initialize a DatasetINE object using its url.
    my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387"
    my_dataset = DatasetINE(my_url)

    # Show dataset info by just printing it!
    print(my_dataset)

    # Show dataset notes.
    print(my_dataset.notes)

    # Show dataset dimensions or attributes.
    print(my_dataset.dimensions)

    # Show dataset dimensions and labels for each one.
    # We reformat this dictionary by simply applying some indentation and removing ascii characters.
    formatted_dict = json.dumps(my_dataset.dimLabels, indent=4, ensure_ascii=False)
    print(formatted_dict)
```

### Work with Dataset values

INEware also lets you work with the dataset values as you want. As they are stored as a simple list,
where each element is uniquely identified by its labels, the effort to get specific values is 
reduced by far.

```python
from ineware.dataset_class import DatasetINE

if __name__ == '__main__':
    # Initialize the DatasetINE object using its url.
    # This url can be modified with a "date" parameter. In this case year 2020 (since 1st January to 31th December).
    # For more information on how to define urls, visit https://www.ine.es/dyngs/DataLab/manual.html?cid=1259945947375
    my_url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/2074?date=20200101:20201231"
    my_dataset = DatasetINE(my_url)

    # Print name of the dataset and unit of measure just to know what we are working with.
    print(my_dataset)
    print(my_dataset.notes)

    # Suppose we want to get only the number of Almería foreign travelers in each month of 2020.
    # As method get_value() returns a list, we can iterate over each value in a simple way to show them.
    for item in my_dataset.get_value(Provincia="Almería", ViajerosPernoctaciones="Viajero",
                                     Residencia="Residentes en el Extranjero"):
        print(item)
```
### Looking for more examples?

Get the source code in my [github repo](https://github.com/rgameroe/ineware).
There are more examples at /examples directory
## Links

You can get more info about how INE API works, URLs Definitions or how to get table identifiers,
in the [INE official page](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945948443)

## License

MIT License

Copyright (c) 2022 Roberto Gamero
