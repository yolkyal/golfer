def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def line_intersection(pt1, pt2, pt3, pt4):
    return ccw(pt1, pt3, pt4) != ccw(pt2, pt3, pt4) and ccw(pt1, pt2, pt3) != ccw(pt1, pt2, pt4)