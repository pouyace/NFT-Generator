from os import path
from config import *
from PIL import Image
import random
import os
import matplotlib.pyplot as plt
import pandas as pd
# Dragon name = rarity_type_background_hair_horn_eyes_eyescolor_glasses_orb_

class Dragon:
    def __init__(self):
        self.info = {}



class DragonGenerator:
    dragons = []
    def __init__(self):
        pass

    def generate(self):
        dragon = None
        while 1:
            dragon = Dragon()
            info = dragon.info
            info[RARITY], info[TYPE] = self.selectDragonType()
            info[NAME] = info[RARITY] + '_' + info[TYPE] + '_'

            for i in ITEMS.items():
                if TYPE in i[1].keys():
                    result = self.randomSelect(i[1][TYPE])
                    info[NAME] += result + '_'
                    info[i[0]] = result

            if self.enrollDragon(info[NAME]):
                break
        self.composite(dragon)
        return dragon


    def randomSelect(self, list):
        return list[random.randint(0, len(list)-1)]


    def selectDragonType(self):
        step = 0
        rand = round(random.random(),2)
        # print("Random Number:", rand)
        for i in DragonType.items():
            step += i[1][Probability]
            if rand <= step:
                dragonColor = self.randomSelect(i[1][COLORS])
                return i[0], dragonColor


    def enrollDragon(self, newDragon):
        if newDragon not in DragonGenerator.dragons:
            DragonGenerator.dragons.append(newDragon)
            return True
        return False

    def composite(self, dragon):
        images = []
        counter = 0
        for i in ITEMS.items():
            newImage = self.openImage(dragon, i[0])
            images.append(newImage)
            if counter > 0:
                images[0] = Image.alpha_composite(images[0], newImage)
            counter += 1
        Image.save(images[0])

    def openImage(self, dragon, item):
        dragon = dragon.info
        imagePath = ITEMSDIR + item + '\\';
        suffix = '.png'
        switcher = {
            BACKGROUND: dragon[BACKGROUND] + '.jpg',
            BODY:       dragon[TYPE] + '\\' + dragon[TYPE],
            EYES:       dragon[EYESCOLOR] + '\\' + dragon[EYES],
            GLASSES:    dragon[GLASSES],
            HAIR:       dragon[TYPE] + '\\' + dragon[HAIR],
            HEAD:       dragon[TYPE] + '\\' + dragon[TYPE],
            HORN:       dragon[TYPE] + '\\' + dragon[HORN],
            ORB:        dragon[ORB]
        }
        imagePath += switcher.get(item)
        if item != BACKGROUND:
            imagePath += suffix
        if os.path.exists(imagePath):
            img = Image.open(imagePath)
            return img
        else:
            print("FFFFFFFFF")