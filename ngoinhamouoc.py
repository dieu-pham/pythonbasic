# import turtle
#
# star = turtle.Turtle()
#
# for i in range(3):
#     star.forward(50)
#     star.right(144)
#
# turtle.done()



import turtle

#đặt kích thước viền cho hình tròn là 5
turtle.pensize (5)

#đặt màu sắc cho viền hình tròn là màu xanh
turtle.pencolor ("blue")

#for outer bigger circle
#đặt màu nền cho hình tròn là màu đỏ
turtle.fillcolor ("red")
turtle.begin_fill()

#đặt bán kính của hình tròn là 150
turtle.circle (150)
turtle.end_fill()
turtle.done