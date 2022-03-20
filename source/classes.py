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
                    if i[0] == GLASSES:
                        r = round(random.random(),2)
                        if r > 0.2:
                            info[i[0]] = ''
                            continue
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
            if i[0] == EYESCOLOR or (i[0] == GLASSES and (dragon.info[GLASSES] == '')):
                continue
            newImage = self.openImage(dragon, i[0])
            if newImage == None or newImage is None:
                print("What the hell?")
            images.append(newImage)
            if counter > 0:
                try:
                    images[0] = Image.alpha_composite(images[0], newImage)
                except:
                    print("Error ", i[0], dragon.info)
            counter += 1
        images[0].save(NFTsDir + dragon.info[NAME] + '.png')
        print(dragon.info , "Saved")
        # images[0].show()

    def openImage(self, dragon, item):
        dragon = dragon.info
        imagePath = ITEMSDIR + item + '\\';
        suffix = '.png'
        switcher = {
            BACKGROUND: dragon[BACKGROUND] + '.jpg',
            BODY:       dragon[TYPE] + '\\' + dragon[TYPE] + suffix,
            EYES:       dragon[EYESCOLOR] + '\\' + dragon[EYES] + suffix,
            GLASSES:    dragon[GLASSES] + suffix,
            HAIR:       dragon[TYPE] + '\\' + dragon[HAIR] + suffix,
            HEAD:       dragon[TYPE] + '\\' + dragon[TYPE] + suffix,
            HORN:       dragon[TYPE] + '\\' + dragon[HORN] + suffix,
            ORB:        dragon[ORB] + suffix
        }
        imagePath += switcher.get(item)
        if os.path.exists(imagePath):
            img = Image.open(imagePath)
            #print(img.size)
            if item == BACKGROUND:
                img = img.convert("RGBA")
                #print("Background found.")
            #img.close()
            return img
        else:
            print("path=", imagePath)
            print("Could not open image")
