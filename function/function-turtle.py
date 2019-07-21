import turtle

def draw_square(t, sz):
    for i in range(8):
        t.forward(sz)
        t.right(45)

def draw_multiple_square(t, sz):
    for i in ['red', 'purple', 'hotpink', 'blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)


def scenario1():
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    wn.title('This is a example code.')

    example = turtle.Turtle()
    draw_square(example, 50)
    wn.mainloop()


def scenario2():
    wn = turtle.Screen()
    # wn.bgcolor('lightgreen')
    tess = turtle.Turtle()
    tess.pensize(3)
    size = 20

    for i in range(40):
        draw_multiple_square(tess, size)
        size = size + 10
        tess.forward(10)
        tess.right(18)
    wn.mainloop()


def main():
    scenario1()
    scenario2()

if __name__ == '__main__':
    main()
