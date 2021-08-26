def line_eq(px1,py1,px2,py2) : # need a check to see if gradient is +- inf
    m = (py1-py2)/(px1-px2)
    c = py1-m*px1
    return m , c


    # special case where between y bounds and x bounds of polygon line
    # shouldn't have any /0 issues as vertical lines should not lead to a mid_intersection
def mid_intersection(lx,ly,px1,py1,px2,py2):
    m, c = line_eq(px1, py1, px2, py2)  # finds line of the equation
    py_at_xmin = round(m * lx + c)  # calculated polygon line y value at lx
    pxmax = max(px1, px2)
    py_at_xmax = round(m * pxmax + c)
    print(py_at_xmin, pxmax, py_at_xmax, ly)

    y_bounds = ly < py_at_xmin and ly >= py_at_xmax

    if y_bounds:
        intersection = True
    else:
        intersection = False

    return intersection




lx = 25000
ly = 7000
px1 =15000
py1 =19640
px2 =29255
py2 =1125
intersection = False

while not intersection:
    px1 = px1 + 1
    print(px1)
    intersection = mid_intersection(lx,ly,px1,py1,px2,py2)



