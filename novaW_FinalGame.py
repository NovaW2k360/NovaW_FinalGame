#Nova Winston
#CS120
#June 12, 2025
#Game Design

#Nova Winston
#CS120
#June 12, 2025
#Game Design

import pygame, simpleGE

#textA = [
#"How to play: ",
#"Navigate through each scenario by choosing between 2 options.",
#"But be careful! Less than wise options may result in game over!",
#"Try to survive!"
#]

#class Intro(simpleGE.Scene):
    #def __init__(self):
        #super().__init__()

        #self.status = "quit"
        #self.setImage("bloodybkg.png")

        #self.lblInstructions = simpleGE.MultiLabel()
        #self.lblInstructions.textLines = textA

        #self.lblInstructions.center = (325, 200)
        #self.lblInstructions.size = (800, 300)

        #self.btnPlay = simpleGE.Button()
        #self.btnPlay.center = (150, 400)
        #self.btnPlay.text = "Play"

        #self.btnQuit = simpleGE.Button()
        #self.btnQuit.center = (500, 400)
        #self.btnQuit.text = "Quit"

        #self.sprites = [
        #self.lblInstructions,
        #self.btnPlay,
        #self.btnQuit
        #]

#def process(self):
    #if self.btnPlay.clicked:
        #self.status = "play"
        #self.stop()
    #if self.btnQuit.clicked:
        #self.status = "quit"
        #self.stop()

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()

        self.setImage("stn_bkg.png")
        self.sound = pygame.mixer.Sound("Station.mp3")
        pygame.mixer.music.load("Station.mp3")
        pygame.mixer.music.play()
        
        self.adv = self.getAdventure()

        self.lblDesc = simpleGE.Label()                      
        self.lblDesc.size = (700, 200)
        self.lblDesc.center = (320, 240)
        self.lblDesc.bgColor = "darkred"

        self.btnChoice1 = simpleGE.Button()
        self.btnChoice1.center = (150, 400)
        self.btnChoice1.text = "{menu1}"

        self.btnChoice2 = simpleGE.Button()
        self.btnChoice2.center = (500, 400)
        self.btnChoice2.text = "{menu2}"

        self.sprites = [
        self.lblDesc,
        self.btnChoice1,
        self.btnChoice2
            ]

        self.displayNode("start")

    def process(self):
        if self.btnChoice1.clicked:
            self.displayNode(self.node1)
        if self.btnChoice2.clicked:
            self.displayNode(self.node2)

    def getAdventure(self):
        game = {
            "start": ["How will you escape?", "Make a run for the door!", "run", "Fight them off!", "fight"], 
            "run": ["You escape! But the zombies will be back, what will you do?", "Find a weapon!", "weapon", "Hide until its over!", "hide"], 
            "fight": ["You try to fight them, but there are too many. You're quickly eaten alive.", "Start over", "start", "Quit", "quit"], 
            "weapon": ["You search for a weapon. You find a bat and a jump rope.", "Bat", "bat", "Jump rope", "jumprope"], 
            "hide": ["You try to hide, but the zombies could still smell you! They find and eat you.", "Start over", "start", "Quit", "quit"], 
            "bat": ["Sturdy! Now you're protected, but they're catching up! Quick, how will you get away?", "Car!", "car", "Bike!", "bike"], 
            "jumprope": ["That's...a ridiculous weapon. The zombies laugh as they eat you.", "Start over", "start", "Quit", "quit"], 
            "car": ["That would be a great option! Except you have no keys...or gas...the zombies find you pretty quickly.", "Start over", "start", "Quit", "quit"], 
            "bike": ["Not the fastest, but definitely convenient! You peddle away, but what to look for now?", "Other survivors!", "survivors", "Food!", "food"], 
            "survivors": ["You find a group of people. They seem well off! How will you approach?", "Threaten them!", "threat", "Be nice!", "nice"], 
            "food": ["You search for food until the sun goes down. But the zombies find you before you've found a crumb.", "Start over", "start", "Quit", "quit"], 
            "threat": ["You try to threaten the group! But...wait, when were there so many? They overpower you, and you die.", "Start over", "start", "Quit", "quit"], 
            "nice": ["You approach, trying to show how nice you are! They welcome you! You survived!", "Start over", "start", "Quit", "quit"],

            }


        return game

    def displayNode(self, key):
        if key == "quit":
            self.stop()
        else:
            currentNode = self.adv[key]
            (desc, menuA, nodeA, menuB, nodeB) = currentNode
            self.lblDesc.text = desc
            self.btnChoice1.text = menuA
            self.btnChoice1.size = (250, 45)
            self.btnChoice2.text = menuB
            self.btnChoice2.size = (250, 45)
            self.node1 = nodeA
            self.node2 = nodeB



def main():
# intro = Intro()
# intro.start()

    game = Game()
    game.start()


if __name__ == "__main__":
    main()

