import turtle
import random



def tribonacci_main():
    def tribonacci(n):
        if n == 3:
            return 1
        elif n == 2:
            return 0
        elif n == 1:
            return 0
        else:
            return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

    print('Значение 10 ряда трибоначи:', tribonacci(10))


def main_tree():
    def tree(branchLen, t):
        if branchLen > 5:
            t.width(branchLen / 10)

            if branchLen < 50:
                t.color("green")
            else:
                t.color("brown")

            t.forward(branchLen)
            r = random.randint(15, 45)
            t.right(r / 2)
            tree(branchLen - random.randint(5, 20), t)

            t.left(r)
            tree(branchLen - random.randint(5, 20), t)

            t.right(r / 2)

            if branchLen >= 50:
                t.color("brown")
            t.backward(branchLen)

    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(100000)
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color("brown")
    tree(110, t)
    screen.exitonclick()


def main_koh():
    def koh(n, angle, l, t):
        if n <= 1:
            t.forward(l)
            t.left(180 - angle)
            t.forward(l)
            t.right(angle)
            t.forward(l)
            t.left(180 - angle)
            t.forward(l)
        else:
            koh(n - 1, angle, l, t)
            t.left(180 - angle)
            koh(n - 1, angle, l, t)
            t.right(angle)
            koh(n - 1, angle, l, t)
            t.left(180 - angle)
            koh(n - 1, angle, l, t)

    screen = turtle.Screen()
    canvas = screen.getcanvas()

    def move_left():
        canvas.xview_scroll(-1, "units")

    def move_right():
        canvas.xview_scroll(1, "units")

    def move_up():
        canvas.yview_scroll(-1, "units")

    def move_down():
        canvas.yview_scroll(1, "units")

    screen.tracer(False)
    t = turtle.Turtle()

    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.listen()

    t.up()
    t.backward(600)
    t.left(90)
    t.backward(300)
    t.right(90)
    t.down()
    koh(5, 120, 10, t)
    screen.exitonclick()


def main_stone():
    def stone(n, angle, l, route, t):
        if n <= 1:
            t.forward(l)
        else:
            if route == 'up':
                stone(n - 1, angle, l / 2, 'up', t)
                t.right(angle)
                stone(n - 2, angle, l / 12, 'down', t)
                t.left(angle)
                stone(n - 1, angle, l / 2, 'up', t)
            else:
                stone(n - 1, angle, l / 2, 'down', t)
                t.left(angle)
                stone(n - 2, angle, l / 12, 'up', t)
                t.right(angle)
                stone(n - 1, angle, l / 2, 'down', t)


    screen = turtle.Screen()
    canvas = screen.getcanvas()

    def move_left():
        canvas.xview_scroll(-1, "units")

    def move_right():
        canvas.xview_scroll(1, "units")

    def move_up():
        canvas.yview_scroll(-1, "units")

    def move_down():
        canvas.yview_scroll(1, "units")

    t = turtle.Turtle()
    t.speed(100000)

    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.listen()

    t.up()
    t.backward(300)
    t.left(90)
    t.backward(300)
    t.right(30)
    t.down()
    stone(7, 120, 900, 'up', t)
    t.right(120)
    stone(7, 120, 900, 'down', t)
    screen.exitonclick()


if __name__ == '__main__':
    c = int(input("Введите номер задания: "))
    if c == 1:
        print("Задание 1 находится в отдельном файле")
    elif c == 2:
        tribonacci_main()
    elif c == 3:
        main_tree()
    elif c == 4:
        main_koh()
    elif c == 5:
        main_stone()
    elif c == 6:
         print('\u0FD1')

    else:
        print('Вы ввели что-то не то')
