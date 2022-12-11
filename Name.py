import turtle as t

t.speed()
t.pensize(30)
t.color("white")
t.bgcolor("black")

#Huruf S
t.up()
t.backward(480)
t.down()
t.forward(50)
t.circle(90, 150)
t.forward(50)
t.circle(-90, 150)
t.forward(50)
t.up()
t.left(180)
t.forward(50)
t.circle(90, 150)
t.forward(50)
t.circle(-90, 150)
t.left(180)
t.up()
t.forward(150)

#Huruf I
t.down()
t.forward(35)
t.left(180)
t.forward(40)
t.left(180)
t.forward(20)
t.left(90)
t.forward(360)
t.left(90)
t.forward(20)
t.left(180)
t.forward(40)
t.left(180)
t.forward(20)
t.up()
t.left(90)
t.forward(360)
t.left(90)
t.forward(80)

#Hutuf L
t.down()
t.forward(120)
t.backward(120)
t.left(90)
t.forward(360)
t.backward(360)
t.right(90)
t.up()
t.forward(160)

#Huruf.M
t.down()
t.left(90)
t.forward(360)
t.right(135)
t.forward(150)
t.left(90)
t.forward(150)
t.right(135)
t.forward(360)
t.left(90)
t.up()
t.forward(50)

#Huruf A
t.down()
t.left(75)
t.forward(375)
t.right(150)
t.forward(375)
t.backward(180)
t.right(105)
t.forward(85)
t.up()

#Love
t.goto(0, 0)
t.left(90)
t.forward(400)
t.left(90)

def curve ():
	for i in range (200):
		t.right(1)
		t.forward(1)
		
t.pensize(20)
t.speed()
t.color("red", "pink")

t.begin_fill()
t.left(140)
t.forward(111.65)
curve()

t.left(120)
curve()
t.forward(111.65)
t.end_fill()

#Teks
t.color("Red")

t.goto(0, -600)
t.write('Iseng² bikin ginian hehe, Sekalian kasih nilai 1-10.', move=False, align="center", font=("Times", 8, "italic"))

t.hideturtle()

t.mainloop()
