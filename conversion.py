import os
files = os.listdir("./test/")

values = []
for file in files:
    
    with open("./test/"+ file, "r") as f:
        data = f.readlines()
        one_values = []
        for line in data:
            stripped_line = line.split()
            #print(stripped_line)
            one_values.append(stripped_line[-1])
        values.append(one_values)

with open("test_dataset_final.csv", "a") as ds:
    for value in values:
        ds.write(",".join(value) + "\n")

