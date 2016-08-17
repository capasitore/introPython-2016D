__author__ = 'andaro'

import sys
import csv
player = 1
board = ['1','2','3','4','5','6','7','8','9']
validPlace = [1,2,3,4,5,6,7,8,9]


def printGameArea():
    print board[0:3]
    print board[3:6]
    print board[6:9]


def play():
    while True:
        printGameArea()
        placeSign(1)
        placeSign(2)

def placeSign(player):
    if player == 1:
        response = input("enter something") - 1
        board[response] = "x";
    if player == 2:
        response = input("enter something") - 1
        board[response] = "o";


play()