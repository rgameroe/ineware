# INEware

INEware is a lightweight Python library that works as a middleware between the client and the API json-stat that INE 
(Instituto Nacional de Estadística) offers to its users.

This library is designed to facilitate the handling of data from INE datasets, as well as integrating them into a 
programmatic environment where we can get the most out of this valuable information.

## Installation


## Kick off

A full set of examples can be found the ****

To get started****

### Title3

```python
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
```
## Links

You can get more info about:
- How INE API works 
- URLs Definitions
- How to get table identifiers

And much more in the [INE official page](https://www.ine.es/dyngs/DataLab/es/manual.html?cid=1259945948443)



