#author: LM (AMDG) 1/25/22
from ast import Return


def adding_sums(number):
    number_rangelst = list(range(0, number + 1))
    for index, value in enumerate(number_rangelst):
        new_value = value + value[index + 1]
        del value[index]
        return new_value
       
    
print(adding_sums(10))
    