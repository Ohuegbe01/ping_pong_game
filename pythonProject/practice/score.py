from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.le_score = 0
        self.ri_score = 0
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.goto(100, 260)
        self.write(f'Score : {self.ri_score}', align='center', font=('courier', 20, 'normal'))
        self.goto(-100, 260)
        self.write(f'Score : {self.le_score}', align='center', font=('courier', 20, 'normal'))

    def l_score(self):
        self.le_score += 1
        self.clear()
        self.update()

    def r_score(self):
        self.ri_score += 1
        self.clear()
        self.update()


