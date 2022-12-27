import turtle as tl

def draw_fractal(length,depth):  # функция принимает два параметра
    if depth==0:
        for i in range(0,4):
            tl.forward(length)
            tl.left(90)
    else:
        draw_fractal(length/2,depth-1)
        tl.forward(length/2)
        draw_fractal(length/2,depth-1)
        tl.back(length/2)
        tl.left(90)
        tl.forward(length/2)
        tl.right(90)
        draw_fractal(length/2,depth-1)
        tl.left(90)
        tl.back(length/2)
        tl.right(90)


tl.speed(1000000)  # увеличиваем скорость черепашки
tl.pensize(2)
tl.penup()
tl.goto(-4, -35)  # сдвигаем начальное положение, чтобы поместился большой фрактал
tl.pendown()
tl.color('cyan')
draw_fractal (800,7)
