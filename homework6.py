my_dict= {"A": 1111, "B": 2222, "C": 3333}
print(my_dict)
print(my_dict["A"])
my_dict["D"] = 4444
print(my_dict["D"])
my_dict.update({"I": 5555, "F": 6666})
num= my_dict.pop("A")
print(num)
print(my_dict.items())
print()

my_set ={21,'a',21,"True",True,'A'}
print(my_set)
my_set.update({22,28})
my_set.discard('a')
print(my_set)