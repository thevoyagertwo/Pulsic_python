# Written by Michael Lee contact: mgdlee98@gmail.com
# Using Ray casting method to find if point is within a polygon
# so works by shooting out line from the point and counting intersections odd = in, even = out
# ran with command line with : <main.py> <text file> <x> <y>
# or my manually inputting values
#

# Possible optimisations:
# Make so ray cast from point being tested is in optimal direction by inferring which direction would have least possible intersections
# Can check first if it is outside outline, if so answer is known
# If within outline check cut outs one at a time, if within a cut out end program
# once all cut outs checked we know for certain it is within outline and not inside a cut out



import numpy as np
import sys





def data_extract(filename,i):  # i used to keep count of what row is being searched so this can be called multiple times
                               # till outline and all cuts have been saved
                               # Can change while to be < temp_row[1] from temp_row = raw_data[i].split(" ")

    #Opens file to be read and splits into a list of each line content. example format below
    file = open(filename, "r")
    # raw_data form: ['OUTLINE 8', '2100 19640', '29255 19640', '29255 1125', '20450 1125', '20450 8345', ..]
    raw_data = file.read().splitlines()


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



## moved this to method above so should be good to delete
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


    file.close()


    return output_data

def line_eq(px1,py1,px2,py2) : # need a check to see if gradient is +- inf
    m = (py1-py2)/(px1-px2)
    c = py1-m*px1
    return m , c

    # special case where between y bounds and x bounds of polygon line
    # shouldn't have any /0 issues as vertical lines should not lead to a mid_intersection
  def mid_intersection(lx,ly,px1,py1,px2,py2,accuracy):
        m,c = line_eq(px1,py1,px2,py2) # finds line of the equation



        return px1,py1,px2,py2


def point_in_poly(filename,lx,ly,accuracy): # lx,ly are point coordinates. Line(ray) drawn to infinity in +x direction
    intersection_count = 0 # counter used for number of intersections from point ray cast
    row_count = 0 # used to keep track of what rows of the text file has been extracted

    file_data = data_extract(filename,row_count)
    print(file_data)


    for i in range(len(file_data) - 1): # -1 range as first points coordinates are stored in 0th and ith row
        intersection = None # used to see if intersection is made
        # storing coordinate data
        px1 = file_data[i,0]
        py1 = file_data[i,1]
        px2 = file_data[i+1,0]
        py2 = file_data[i+1,1]
        print(i,px1,py1,px2,py2, lx, ly)

        # rules so point ray is within y bounds of polygon line
        y_bounds = ly > min(py1, py2) and ly <= max(py1, py2)
        x_right_bounds = lx > max(px1, px2) # checks if point is right of both polygon line points if so 100% no intersection
        x_left_bounds = lx <= min(px1, px2) and intersection != False  # check if point is left of both polygon line points.

        if y_bounds: # checks if point is not above/below polygon line
            print('ybounds',str(i))
            if x_right_bounds:
                intersection = False
            if x_left_bounds:  # checks if point is left(-ve x direction) of both polygon line points
                intersection = True
                print('xbounds',str(i))
            if intersection is None: # special case where between y bounds and x bounds of polygon line
                px1,py1,px2,py2 = mid_intersection(lx,ly,px1,py1,px2,py2,accuracy)



        if intersection: # if intersection is True we add onto the counter
            intersection_count = intersection_count + 1  # intersection between point ray and polygon line


    if (intersection_count % 2 ) == 0 : # checks if number of intersections is even
        in_poly = 'outside' # if even point is point is outside polygon
    else:
        in_poly = 'within'  # if odd point is point is inside polygon

    print('Point ray had ' + str(intersection_count) + ' intersections')


    return in_poly

if __name__ == '__main__':
    ## <main.py> <text file> <x> <y>
    try:
        filename = sys.argv[1]
        lx = int(sys.argv[2]) # x point coordinate
        ly = int(sys.argv[3]) # y point coordinate

    except:
    ## manual input:
        filename = 'data.txt'
        lx = 25000 # x point coordinate
        ly = 7000 # y point coordinate
        print('cmd line inputs not read successfully, using defaults which can be changed within file')

    ## The way I have dealt with the case where the point is within the x,y bounds of the polygon line
    ## requires drawing the line +- accuracy around x point value.
    ## Lower accuracy value means better accuracy
    accuracy = 1

    in_poly = point_in_poly(filename, lx, ly,accuracy)


    print('Point (' + str(lx) + ',' + str(ly) + ')' + ' found to be ' + in_poly +' polygon described in: ' + filename )


    # # to test data_extract and grad
    # file_data = data_extract(filename)
    # print(file_data)
    # for k in range(len(file_data)-1):
    #     mc = line_eq(file_data[k,0] , file_data[k,1] , file_data[k+1,0] , file_data[k+1,1] )
    #     print(mc)









