length = len(height)
ptr1 = 0
ptr2 = length - 1
width = length - 1
area = 0
while ptr1 < ptr2:
    tempArea = min(height[ptr1], height[ptr2]) * width
    if area < tempArea:
        area = tempArea
    if height[ptr1] < height[ptr2]:
        ptr1 += 1
    else:
        ptr2 -= 1
    width -= 1
return area