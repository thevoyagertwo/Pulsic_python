

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

# maybe store the first point as the end point as well to lead to nicer loops when testing
def data_extract(filename):

    #Opens file to be read and splits into a list of each line content. example below
    file = open(filename, "r")
    # raw_data form: ['OUTLINE 8', '2100 19640', '29255 19640', '29255 1125', '20450 1125', '20450 8345', ..]
    raw_data = file.read().splitlines()

    temp_row = raw_data[0].split(" ") # Splits 'Outline NO_outline' where NO_outline is number of points in Outline
    NO_outline = int(temp_row[1]) # stores (int)number of points in Outline
    print(NO_outline)

    outline_data = np.zeros((NO_outline + 1,2) , dtype=int) # Creates zeros numpy array to store (int)coordinates. Note + 1 is to store the first point twice for easier looping later

    # Stores all outline (int)points coordinates including the first point as the 0th and NO_outline row
    for i in range(0,NO_outline):
        temp_row = raw_data[i+1].split(" ") # [i+1] required to skip initial 'Outline X' row
        print(i)
        outline_data[i,0] = int(temp_row[0])
        outline_data[i,1] = int(temp_row[1])
        if i == 0:
            outline_data[NO_outline, 0] = int(temp_row[0])
            outline_data[NO_outline, 1] = int(temp_row[1])



    # works but need to add ranges for the data, as does not handle strings.
    # for i in range(1 , len(raw_data)):
    #
    #     temp_row = raw_data[i].split(" ")
    #     outline_data[i,0] = temp_row[0]
    #     outline_data[i,1] = temp_row[1]

    # while i <






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
