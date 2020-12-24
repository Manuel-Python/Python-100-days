import turtle as tu
ti = tu.Turtle() # create a turtle
ti.penup()
ti.goto(40.0,-200.0)
ti.pendown()
#ti.screen.bgcolor('yellow') #Set turtle screen color
ti.left(90)      # turn turtle left by 90
ti.speed(20)      # set speed of turtle
ti.color('green')  #set turtle color
ti.pensize(1)      # set turtle pensize i.e thickness of lines
ti.screen.title("Fractal Tree") #set turtle title

# recursive function
def draw_fractal(blen):
    if(blen<10):   # set limit to fractal because it repeats itself infinetly
        return
    else:
        ti.forward(blen)
        ti.left(30)
        draw_fractal(3*blen/4)
        ti.right(60)
        draw_fractal(3*blen/4)
        ti.left(30)
        ti.backward(blen)

draw_fractal(100) #call the function
ti = tu.done()