"""
John Gareth Kyle C. Yumul
G3 - Level 5 - Cybersecurity
Exercise 2: Alexa Tell Me a Joke
"""

import random  # Shuffle the jokes into a random order
import tkinter as tk  # GUI toolkit
from pathlib import Path  # Build the joke file's path from this script's location
from tkinter import messagebox  # Error message pop-up if the joke file can't be loaded

# This allows to connect the python file to the txt file
Jokes_File = Path(__file__).parent / "randomJokes.txt"

# Reads the jokes.txt file and returns a list of (setup, punchline) pairs, skipping bad lines
def load_jokes(path):
    jokes = []
    with open(path, encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()
            if line.startswith("-"):
                line = line[1:].strip()
            if "?" not in line:  # No questions mark jokes means nothing to split
                continue
            setup, _, punchline = line.partition("?")
            setup, punchline = setup.strip(), punchline.strip()
            if not setup or not punchline:
                continue
            jokes.append((setup + "?", punchline))
    if not jokes: # If file has no usable jokes 
        raise ValueError("No usable jokes found in the file.")
    return jokes