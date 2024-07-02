#Functions 102

username:str = input("username: ")
password:str = input("password: ")

def login_user():
    global username
    system_version = 5.2
    username = "ahmed"
    print(username)
    if username == "mohammed" and password == "1235":
        print(f"welcome to our system")
        print(f"version {system_version}")
    else:
        print("You are not authorized")



login_user()
print(username)


#Positional arguments: Args, keyword arguments: Kwargs

def rectangle_area(height:float, width:float, unit:str = "meter") -> float:
    """
    this calculates the area of a rectangle in the unit provided

    Args:
        height (float): the height of the rectangle.
        width (float): the width of the rectangle.
        unit (str, optional): the unit of the calculation

    Returns:
        str: a phrase describing the area in the rectangle
    
    """
    area = height*width
    result = f"the area of the rectangle is {area} square {unit}"
    return result


#positional arguments
print(rectangle_area(2, 3, "meter"))

#keyword arguments
print(rectangle_area(width=6, height=4, unit="meter"))

#using positional and keywords ?
print(rectangle_area(2, unit="cm",  width=3))

#optional / default values
print(rectangle_area(2, width=10))

