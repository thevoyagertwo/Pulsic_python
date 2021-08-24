

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

# maybe store the first point as the end point as well to lead to nicer loops when testing
def data_extract(filename):


    file = open("data.txt", "r")

        # data output : ['OUTLINE 8', '2100 19640', '29255 19640', '29255 1125', '20450 1125', '20450 8345',
    raw_data = file.read().splitlines()
    print(raw_data[18].split(" "))


    outline_data = np.zeros((len(raw_data),2))

    # works but need to add ranges for the data, as does not handle strings.
    for i in range(1 , len(raw_data)):

        temp_row = raw_data[i].split(" ")
        outline_data[i,0] = temp_row[0]
        outline_data[i,1] = temp_row[1]






    # full_data(0,0) = 10


    # for row in file:
    #     file_data = row.split(" ")
    #
    #
    #     print(file_data[0])
    #     print(file_data[1])

    file.close()


    return outline_data




if __name__ == '__main__':
    filename = 'data.txt'

    file_data = data_extract(filename)
    print(file_data)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
