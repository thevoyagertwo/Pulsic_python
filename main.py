# Written by Michael Lee contact: mgdlee98@gmail.com
# Using Ray casting method to find if point is within a polygon
# so works by shooting out line from the point and counting intersections odd = in, even = out
# ran with command line with : <main.py> <text file> <x> <y>
# or my manually inputting values
#



import numpy as np
import sys





def data_extract(filename):

    #Opens file to be read and splits into a list of each line content. example below
    file = open(filename, "r")
    # raw_data form: ['OUTLINE 8', '2100 19640', '29255 19640', '29255 1125', '20450 1125', '20450 8345', ..]
    raw_data = file.read().splitlines()

    i = 0 # used to keep count of what row is being searched
    cut_count = 0 # counts number of cuts in the file
    while i < len(raw_data):
        temp_row = raw_data[i].split(" ")  # Splits 'Outline NO_outline' where NO_outline is number of points in Outline
        if temp_row[0].lower() == 'outline': # makes string data lower case and checks if it is 'outline'
            print(str(i) + ' ' + temp_row[0]+ ' ' + temp_row[1])
            temp_row = raw_data[0].split(" ")  # Splits 'Outline NO_outline' where NO_outline is number of points in Outline
            NO_outline = int(temp_row[1])  # stores (int)number of points in Outline

            outline_data = np.zeros((NO_outline + 1, 2),dtype=int)  # Creates zeros numpy array to store (int)coordinates. Note + 1 is to store the first point twice for easier looping later

            # Stores all outline (int)points coordinates including the first point as the 0th and NO_outline row
            for j in range(i, i + NO_outline):
                temp_row = raw_data[j + 1].split(" ")  # [i+1] required to skip initial 'Outline X' row
                outline_data[j, 0] = int(temp_row[0])
                outline_data[j, 1] = int(temp_row[1])
                if j == 0:  # could move this outside loop so not checked everytime
                    outline_data[NO_outline, 0] = int(temp_row[0])
                    outline_data[NO_outline, 1] = int(temp_row[1])

            i = i + int(temp_row[1]) + 1
        elif temp_row[0].lower() == 'cut': # makes string data lower case and checks if it is 'cut'
            print(str(i) + ' ' + temp_row[0]+ ' ' + temp_row[1])
            i = i + int(temp_row[1]) + 1
        else:
            print('Please input data in correct format. With either cut or outline as the first value ')
            break
        # i = i + 1

    output_data = outline_data




    # below works for getting outline data but working on a smarter system above that will check the string to make sure outline is correct
    #
    # temp_row = raw_data[0].split(" ") # Splits 'Outline NO_outline' where NO_outline is number of points in Outline
    # NO_outline = int(temp_row[1]) # stores (int)number of points in Outline
    #
    # outline_data = np.zeros((NO_outline + 1,2) , dtype=int) # Creates zeros numpy array to store (int)coordinates. Note + 1 is to store the first point twice for easier looping later
    #
    # # Stores all outline (int)points coordinates including the first point as the 0th and NO_outline row
    # for i in range(0,NO_outline):
    #     temp_row = raw_data[i+1].split(" ") # [i+1] required to skip initial 'Outline X' row
    #     outline_data[i,0] = int(temp_row[0])
    #     outline_data[i,1] = int(temp_row[1])
    #     if i == 0: # could move this outside loop so not checked everytime
    #         outline_data[NO_outline, 0] = int(temp_row[0])
    #         outline_data[NO_outline, 1] = int(temp_row[1])


    # full_data(0,0) = 10


    # for row in file:
    #     file_data = row.split(" ")
    #
    #
    #     print(file_data[0])
    #     print(file_data[1])

    file.close()


    return output_data




if __name__ == '__main__':

    ## uncomment for manual input
    # filename = 'data.txt'
    # x_point = 250
    # y_point = 500


    # <main.py> <text file> <x> <y>
    filename = sys.argv[1]
    x_point = int(sys.argv[2])
    y_point = int(sys.argv[3])

    print(sys.argv[1])

    file_data = data_extract(filename)
    print(file_data)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
