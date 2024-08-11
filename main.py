import turtle 
t=turtle.Turtle()
s=turtle.Screen()
t.color("white")
s.bgcolor("blue")
turtle.speed(10)
t.fillcolor("white")
t.begin_fill()
for i  in range(36):
   t.forward(20)
   t.right(10)
t.end_fill()
input("hi")