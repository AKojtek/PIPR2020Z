def square(lenght,height):
    for i in range(0,height):
        print('{:*<{size}}'.format("",size=lenght))

lenght=int(input("Insert square width "))
height=int(input("Insert square height "))
square(lenght,height)