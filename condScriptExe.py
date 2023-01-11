def rectangleArea(width, length):
    """Takes in two numbers, the width and length of a rectangle, and returns the area of the rectangle"""
    return width * length

if __name__ == '__main__':
    print("Testing the function...")
    area1 = rectangleArea(30, 25)
    print("The area of a", 30, "by", 25, "rectangle is:", area1)
    area2 = rectangleArea(100, 100)
    print("The area of a", 100, "by", 100, "rectangle is", area2)