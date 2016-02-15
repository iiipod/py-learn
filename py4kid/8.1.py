class Animals:
    def breath(self):
        print('Breathe')
    def move(self):
        print('Moveing')
    def eat_food(self):
        print('Eat food')

class Mammals(Animals):
    def feed_young(self):
        print('Feed young with milk')

class Giraffes(Mammals):
    def eat_leaves(self):
        print('Eat leaves from trees')
    def left_Foot_Forward(self):
        print('left foot forward')
    def left_Foot_Back(self):
        print('left foot back')
    def right_Foot_Forward(self):
        print('right foot forward')
    def right_Foot_Back(self):
        print('right foot back')

    def dance(self):
        self.left_Foot_Forward()
        self.left_Foot_Back()
        self.right_Foot_Forward()
        self.right_Foot_Back()
        self.left_Foot_Back()
        self.right_Foot_Back()
        self.right_Foot_Forward()
        self.left_Foot_Forward()

reginald = Giraffes()
reginald.dance()
reginald.feed_young()
reginald.breath()
reginald.move()
reginald.eat_food()
