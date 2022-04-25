"""
Program calculates common part of two given segments on one dimensional plane
"""

def getCommonSection(segmentA, segmentB):
    A1, A2 = segmentA
    B1, B2 = segmentB

    left_boundary = max(A1, B1)
    right_boundary = min(A2, B2)

    if left_boundary > right_boundary:
        return "Common part doesn't exist"
    return (left_boundary, right_boundary)

print(getCommonSection((1, 3), (5, 7)))
print(getCommonSection((1, 10), (5, 7)))
print(getCommonSection((10, 11), (5, 7)))