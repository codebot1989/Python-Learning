###########################################################################
#
#Write a program able to play the "Guess the number"-game, 
#where the number to be guessed is randomly chosen between 1 and 20.
#
#########################################################################

import random
import sys
class Game(object):

    def __init__(self):
        self.count = 0
        self.comp_rand = random.randint(0,20)
        self.name = raw_input("What is your Name\n")

    def process(self):
        if self.val1 == self.comp_rand:
            print "Amazing Guess!! My number is %d and you took %d guesses to find" % (self.comp_rand,self.count)
            sys.exit()
        elif self.val1 < self.comp_rand:
            print "Guess Little Higher"
            self.get_values()
        elif self.val1 > self.comp_rand:
            print "Guess Little Lower"
            self.get_values()

    def print_result(self):
        print "Well %s I am Thinking of a Number between 1 and 20 Take a Guess!\n" % self.name

    def get_values(self):
        self.count = self.count + 1
        self.val1 = input("Enter Value\n")
        self.process()

player = Game()
player.print_result()
player.get_values()
player.process()

