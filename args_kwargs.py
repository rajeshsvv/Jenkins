def person(name,*data):

    print(name)             # Navin
    print(data)             # (28, 'Mumbai', 8151958650)
    # print(*data)          # 28 Mumbai 8151958650


person("Navin",28,"Mumbai",8151958650)


def person(name,**data):

    print(name)                # Navin
    # print(data)              # {'age': 28, 'city': 'Mumbai', 'mob': 8151958650}
    # print(*data)             # age city mob
    # print(**data)            # TypeError: 'age' is an invalid keyword argument for print()

    for i,j in data.items():
        print(i,j)


person("Navin",age=28,city="Mumbai",mob=8151958650)

'''
age 28
city Mumbai
mob 8151958650
'''