"""
John Gareth Kyle C. Yumul
G3 - Level 5 - Cybersecurity
Exercise 2: Alexa Tell Me a Joke
"""

import random  # Shuffle the jokes into a random order
import tkinter as tk  # GUI toolkit
from pathlib import Path  # Build the joke file's path from this script's location
from tkinter import messagebox  # Error message pop-up if the joke file can't be loaded

