"""
Program calculates common part of two given segments on one dimensional plane
"""


def get_common_section(segment_A, segment_B):
    A1, A2 = segment_A
    B1, B2 = segment_B

    left_boundary = max(A1, B1)
    right_boundary = min(A2, B2)

    if left_boundary > right_boundary:
        return "Common part doesn't exist"
    return (left_boundary, right_boundary)

print(get_common_section((1, 3), (5, 7)))
print(get_common_section((1, 10), (5, 7)))
print(get_common_section((10, 11), (5, 7)))