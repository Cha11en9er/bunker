import random

def read_file(path):
    file_data = []
    with open(path) as f:
        for line in f:
            file_data.append(line[0:-1])
    return file_data

good_count = 0
bad_count = 0
theme_count = 0
good_attributes = read_file(r'C:\repos\python_django\bunker\game\good.txt')
bad_attributes = read_file(r'C:\repos\python_django\bunker\game\bad.txt')
all_attributes = []

for i in range(6):
    choise = random.randint(0, 1)
    if choise == 1 and good_count != 3:
        # print(good_attributes[1])
        all_attributes.append(good_attributes[(random.randint(theme_count, theme_count+2))])
        good_count += 1
    else:
        # print(bad_attributes)
        all_attributes.append(bad_attributes[(random.randint(theme_count, theme_count+2))])
        bad_count += 1

    theme_count += 2

    # print(all_attributes)

# print(all_attributes)

card = [
    {
        "attribute_1":str(all_attributes[0]),
        "attribute_2":str(all_attributes[1]),
        "attribute_3":str(all_attributes[2]),
        "attribute_4":str(all_attributes[3]),
        "attribute_5":str(all_attributes[4]),
        "attribute_6":str(all_attributes[5])
    }
]

print(card)