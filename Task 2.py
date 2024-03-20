import turtle

def pifagoras_tree(size, level):
    if level > 0:
        turtle.forward(size)
        turtle.left(45)
        pifagoras_tree(0.7 * size, level - 1)
        # Рекурсивний виклик для правої гілки
        turtle.right(90)
        pifagoras_tree(0.7 * size, level - 1)
        # Рекурсивний виклик для лівої гілки
        turtle.left(45)
        turtle.backward(size)

def main():
    level = int(input("Вкажіть рівень рекурсії => "))
    
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("blue")
    turtle.left(90)

    pifagoras_tree(100, level)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()