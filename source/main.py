from os import path
from config import *
import os
import matplotlib.pyplot as plt
import pandas as pd


def startOperation():
    generator = DragonGenerator()
    counter = 0
    while counter != 10:
        dragon = generator.generate()
        print(dragon.info)
        counter += 1



if __name__ == "__main__":
    startOperation()





