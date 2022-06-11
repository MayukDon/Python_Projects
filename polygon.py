import turtle

print ("This program will draw a polygon of your choice for you!")

edge = input ("Enter the nuber of edges you want your polygon to have: "  )
side = input ("The lenght that each side should have ")

if (int(edge) < 4):
    print("There must be minimum 3 edges in a polygon")
elif (int(edge)<0):
    print("invalid number")
else:
    turtle.Screen()
    polygon = turtle.Turtle()
    polygon.penup()
    polygon.goto(10,10)
    polygon.pendown()
    polygon.color("blue")   
    polygon.begin_fill()
    for i in range (int(edge)):
        polygon.forward(int(side))
        polygon.right(360/int(edge))

    polygon.end_fill()
    turtle.done()
    turtle.mainloop()