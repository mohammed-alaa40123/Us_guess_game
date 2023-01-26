import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Fame")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
x_coor = data['x'].to_list()
y_coor = data['y'].to_list()
coors_list = []
for element in range(len(x_coor)):
    coor_tuple = (int(x_coor[element]), int(y_coor[element]))
    coors_list.append(coor_tuple)
states = data.state.to_list()
U_S_Dict = {
    'stateName': states,
    'position' : coors_list
}

DataFrame = pandas.DataFrame(U_S_Dict)
answer = turtle.Turtle()
answer.hideturtle()
t = turtle.Turtle()
s =turtle.Turtle()
score = 0

while score < 50:
    answer = (screen.textinput('Guess the State', "What's the next state's name?")).title()
    GotItRight = []

    if answer == "Exit":
        States_To_Memorize = pandas.DataFrame([state for state in states if state not in GotItRight ]).to_csv("States_To_Memorize.csv")

    if answer in states:
        t.hideturtle()
        t.penup()
        t.goto(U_S_Dict['position'][states.index(answer)])
        t.write(answer)
        score += 1
        s.hideturtle()
        s.penup()
        s.goto(-250,250)
        s.clear()
        style = ('Courier', 50, 'bold')
        s.write(f'SCORE: {score}/50',font=style)
        GotItRight.append(answer)



screen.exitonclick()
