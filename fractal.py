"""
Author: Shaam Prakash
UPI: spra990
"""

import turtle
def draw_shape(t ,pos ,size ,level):
	
	if level == 0:
	#Once finished goes to the middle
		t.up()
		t.goto(0,0)

	if level > 0:
	# Draws the I shape
		t.setpos(pos)
		t.backward(size)
		t.right(90)
		t.backward(size)
		xbotleft = t.pos()
		t.down()
		t.forward(size*2)
		xbotright = t.pos()
		t.up()
		t.backward(size)
		t.left(90)
		t.down()
		t.forward(size*2)
		t.left(90)
		t.up()
		t.backward(size)
		xtopright = t.pos()
		t.down()
		t.forward(size*2)
		xtopleft = t.pos()
		t.up()
		t.backward(size)
		t.right(90)
		t.backward(size)
			
		draw_shape(t,xtopright,size/2, level - 1)		#top Right
		
	
		draw_shape(t,xbotright,size/2, level - 1)		#Bottom Right
		
		
		draw_shape(t,xbotleft,size/2, level - 1)		#Bottom Left
		
		
		draw_shape(t,xtopleft,size/2, level - 1)		#Top Left		
		
	


def q1():
	my_win = turtle.Screen()
	my_turtle = turtle.Turtle()
	my_turtle.speed(0)
	my_turtle.left(90)
	my_turtle.color("Black")
	my_turtle.up()
	position = 0,0
	n = int(input('Draw shape at level: '))
	draw_shape(my_turtle,position,100,n)
	my_win.exitonclick()
	
q1()