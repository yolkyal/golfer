def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def is_line_intersection(pt1, pt2, pt3, pt4):
    return ccw(pt1, pt3, pt4) != ccw(pt2, pt3, pt4) and ccw(pt1, pt2, pt3) != ccw(pt1, pt2, pt4)
	
def get_line_intersection_pt(pt1, pt2, pt3, pt4):
    xdiff = (pt1[0] - pt2[0], pt3[0] - pt4[0])
    ydiff = (pt1[1] - pt2[1], pt3[1] - pt4[1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(pt1, pt2), det(pt3, pt4))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (x, y)