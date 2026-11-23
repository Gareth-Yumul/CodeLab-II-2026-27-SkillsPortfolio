"""
John Gareth Kyle C. Yumul
G3 - Level 5 - Cybersecurity
Exercise 1: Maths Quiz
"""

import random # Imports random Number
import re  # Imports regular Expression
import tkinter as tk # GUI toolkit
from tkinter import messagebox # Imports pop-up message such as "play again?"

Questions_Per_Game = 10 #The amount of questions you'll get in a game
Points_First_Try = 10 # The amount of points you will get in first attempt in each questions
Points_Second_Try = 5 # The amount of points you will get in second attempt in each questions
Max_Score = Questions_Per_Game * Points_First_Try # Total amount points got in the quiz
Feedback_Delay_Ms = 1200 # It shows how long the "Correct" or "Wrong" stays in milliseconds 

# This Dictonaries shows the level and the min and max number in each level
Difficulties = {
    "Easy": (1, 9),
    "Moderate": (10, 99),
    "Advanced": (1000, 9999),
}

# This list of tuple (minimum score, grade) shows the score depending the users result 
Grade_Boundaries = [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D"), (0, "F")]

# This allows user input to be valis such as "1_000" or "-54" but inputs such as "abc" or "4x" invalid
Integer_Pattern = re.compile(r"-?\d+")

