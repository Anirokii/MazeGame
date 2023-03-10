import turtle
import random
import math

def main():

    #définition de la classe SquarePen pour dessiner les murs
    class SquarePen(turtle.Turtle):
        def __init__(self):
            # initialization of class
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("white")
            self.penup()
            # self.setx(0)
            # self.sety(0)
            self.speed(0)
            # Animation Speed

    #définition de la classe Win pour dessiner la sortie du carte
    class Win(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape("circle")
            self.color("red")
            self.penup()
            self.speed(0)
            self.gold = 100
            self.goto(x, y)

    #définition de la classe Player
    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("pica.gif")
            self.color("blue")
            self.penup()
            self.speed(0)
            self.gold = 0

        def go_up(self):
            # Calculating spot to move
            move1_to_x = player.xcor()
            move1_to_y = player.ycor() + 23

            # Checking of walls
            if (move1_to_x, move1_to_y) not in walls:
                self.goto(move1_to_x, move1_to_y)

        def go_down(self):
            # Calculating spot to move
            movee_to_x = player.xcor()
            movee_to_y = player.ycor() - 23

            # Checking of walls
            if (movee_to_x, movee_to_y) not in walls:
                self.goto(movee_to_x, movee_to_y)

        def go_left(self):
            # Calculating spot to move
            move2_to_x = player.xcor() - 23
            move2_to_y = player.ycor()

            # Checking of walls
            if (move2_to_x, move2_to_y) not in walls:
                self.goto(move2_to_x, move2_to_y)

        def go_right(self):
            # Calculating spot to move
            move_to_x = player.xcor() + 23
            move_to_y = player.ycor()

            # Checking of walls
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def collision(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))

            if distance < 5:
                return True
            else:
                return False

    #définition de la classe Enemy
    class Enemy(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape("bombleft.gif")
            self.penup()
            self.speed(0)
            self.gold = 25
            self.goto(x, y)
            self.direction = random.choice(["up", "down", "left", "right"])

        def move(self):
            if self.direction == "up":
                dx = 0
                dy = 23
            elif self.direction == "down":
                dx = 0
                dy = -23
            elif self.direction == "left":
                dx = -23
                dy = 0
                self.direction == "left"
            elif self.direction == "right":
                dx = 23
                dy = 0
                self.shape("bombright.gif")
            else:
                dx = 0
                dy = 0
            # Calculate spot to move to
            to_x = self.xcor() + dx
            to_y = self.ycor() + dy

            # Checking that the spot is not wall
            if (to_x, to_y) not in walls:
                self.goto(to_x, to_y)

            else:
                self.direction = random.choice(["up", "down", "left", "right"])
            turtle.ontimer(self.move, t=random.randint(100, 300))

    #définition de la classe Treasure pour dessiner les trésor
    class Treasure(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape("tre.gif")
            self.color("gold")
            self.penup()
            self.speed(0)
            self.gold = 100
            self.goto(x, y)
        #methode pur effacer un tresor du la carte
        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

#part 1 : initialization and declaration of main varibales :

    # Window initialization
    mn = turtle.Screen()
    mn.bgcolor("black")
    mn.title("A Maze Game")
    mn.setup(1000, 10000)

    # Add game graphic resources
    images = ["pica.gif", "tre.gif", "bombleft.gif", "bombright.gif"]
    for image in images:
        turtle.register_shape(image)

    #Game Basic varibales
    # Treasure List
    treasures = []
    # Enemy list
    enemies = []
    # Win list
    wins = []
    # Levels list
    levels = [""]
    # Walls Coordinate list
    walls = []

    # Creating level 1 (Map 1)
    level_1 = [
        "XXXXXXXXXXXXX PXXXXXXXXXXXXXXXXX",
        "X           X                  X",
        "X   XXX  X  X                  X",
        "X     X  X  X  XXXX  X  XXXX   X",
        "X     X  X     X     X     X   X",
        "XXXX  XXXXXXXXXXXXXXXXT XXXXE  X",
        "X   E    XE   T   X     X      X",
        "XE       X  X     X     X      X",
        "X  XXXXXXX  XXXX  XXXXXXX  X   X",
        "X        X     X  X     X  X   X",
        "X        X     X  X     X  X   X",
        "X   X  XXXXXX  X  X  XXXX  XXXXX",
        "X   X       X  X     ET XE     X",
        "X   XTE     X  X        X      X",
        "X   XXXXXX  X  XXXXXXX  XXXX E X",
        "X   X       X  X        X  X   X",
        "X   X       X  X        X  X   X",
        "X   XXXXXXXXX  X  XXXX  X  X   X",
        "X    TE  XE    X  X  X   E XE  X",
        "X        X     X  X  XE    X   X",
        "XXXXXXXT X  XXXXT X  XXXX  X   X",
        "X           XE    XE    X  X  EX",
        "X           X     X     X  X   X",
        "X  X  XXXXXXX  XXXX     X  X   X",
        "X  XE    X  X  X     X     X   X",
        "X  X     X  X  X     XE    X   X",
        "XXXX     X  X  XXXX  X  XXXXE  X",
        "X E   X     X     X  X         X",
        "X     X     X     X  X         X",
        "XXXXXXXXXXXXXXXX--XXXXXXXXXXXXXX"]
    levels.append(level_1)

    # set game parameters : a method for map creation and changing levels
    def set_maze(levels):

        #a SquarePen object
        pen = SquarePen()

        # we will browse our level matrix table and create the map with every letter meaning
        # choice of values is made after a search on google to present the game in the middle of the window
        for y in range(len(levels)):
            for x in range(len(levels[y])):
                char = levels[y][x]
                screen_x = -370 + (x * 23)
                screen_y = 325 - (y * 23)

                if char == 'X':
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    # Storing wall in walls
                    walls.append((screen_x, screen_y))
                if char == '-':
                    wins.append(Win(screen_x, screen_y))

                if char == 'P':
                    player.goto(screen_x, screen_y)

                if char == 'T':
                    treasures.append(Treasure(screen_x, screen_y))

                if char == 'E':
                    enemies.append(Enemy(screen_x, screen_y))

#Part 2 : Main game execution:

    # a player object
    player = Player()
    #method set_maze call
    set_maze(levels[1])

    # Keyboard Binding
    turtle.listen()
    turtle.onkey(player.go_left, "Left")
    turtle.onkey(player.go_right, "Right")
    turtle.onkey(player.go_down, "Down")
    turtle.onkey(player.go_up, "Up")
    mn.tracer(0)

    # Starting enemy to move
    for enemy in enemies:
        turtle.ontimer(enemy.move, t=250)

    #Main game loop :
    while True:

        # Check for player collision with treasure
        for treasure in treasures:
            if player.collision(treasure):
                # Score incrementation
                player.gold += treasure.gold
                print("**Player gold:", int(format(player.gold)))
                # Destroy the treasure
                treasure.destroy()
                # Remove the Treasure from list
                treasures.remove(treasure)

        # Check for player collision with enemy
        for enemy in enemies:
            if player.collision(enemy):
                print("*****You lose try Again*****")
                exit()

        # Check for player collision with win
        for win in wins:
            if player.collision(win):
                print("********Winner*********")
                exit()

        # Update the window with changes
        mn.update()

if __name__ == "__main__":
    main()


