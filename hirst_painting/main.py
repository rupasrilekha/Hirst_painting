# import colorgram
#
# colors= colorgram.extract('image.jpg',45)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random

t.colormode(255)
tim= t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list=[(248, 248, 247), (234, 242, 240), (230, 235, 241), (245, 239, 244), (2, 9, 30), (121, 95, 42), (69, 32, 22), (237, 212, 72), (220, 81, 60), (223, 118, 101), (92, 1, 21), (178, 140, 171), (150, 92, 115), (34, 90, 27), (8, 154, 73), (204, 63, 92), (2, 64, 147), (168, 129, 78), (4, 80, 29), (220, 179, 218), (5, 220, 217), (79, 135, 179), (123, 153, 178), (81, 112, 139), (115, 186, 166), (4, 220, 225), (119, 14, 33), (244, 204, 8), (134, 223, 209), (229, 174, 166), (187, 190, 199), (71, 64, 52), (89, 51, 46), (126, 221, 226)]
tim.setheading(220)
tim.forward(300)
tim.setheading(0)
num_of_dots=100


for dot_count in range(1,num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()