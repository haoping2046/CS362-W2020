from random import choice
from unittest import TestCase
import datetime

class test_Action_card(TestCase):

    def test_init(self):
        self.testme()

    def inputChar(self):
        char_list = ['[', '(', '{', ' ', 'a', 'x', '}', ')', ']', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
        c = choice(char_list)
        return c

    def inputString(self):
        char_list = ['r', 'e', 's', 't', 'a', 'b', 'c', 'd', 'f', 'g' 'h', 'i', 'j', 'k', 'l',
                     'm', 'n', 'o', 'p', 'q', 'r', 'u', 'v', 'w', 'x', 'y']
        s = [choice(char_list) for n in range(5)]
        return s

    def testme(self):
        begin = datetime.datetime.now()

        tcCount = 0
        s = ''
        c = ''
        state = 0
        while True:
            tcCount += 1
            c = self.inputChar()
            s = self.inputString()
            print("Interation ", tcCount, ": c=", c, "s=", s, "state=", state)

            if c == '[' and state == 0:
                state = 1
            if c == '(' and state == 1:
                state = 2
            if c == '{' and state == 2:
                state = 3
            if c == ' ' and state == 3:
                state = 4
            if c == 'a' and state == 4:
                state = 5
            if c == 'x' and state == 5:
                state = 6
            if c == '}' and state == 6:
                state = 7
            if c == ')' and state == 7:
                state = 8
            if c == ']' and state == 8:
                state = 9
            if len(s) == 5 and s[0] == 'r' and s[1] == 'e' and s[2] == 's' and s[3] == 'e' and s[4] == 't' and state == 9:
                print("error ")
                end = datetime.datetime.now()
                print("run time: ", (end - begin).total_seconds())
                break



