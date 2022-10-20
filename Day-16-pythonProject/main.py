# from turtle import Turtle, Screen
# kachu = Turtle()
# print(kachu)
# kachu.shape("turtle")
# kachu.color("green")
# kachu.forward(100.00)
# my_screen = Screen()
# print(my_screen.screensize())
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ['Pikachu','Squirtle', 'Bulbasaur','Charmander'])
table.add_column("Type",['Electric','Water','Grass','Fire'])
table.align = 'l'
print(table)