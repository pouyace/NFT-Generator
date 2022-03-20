
import random

# User Config
NFTsCount = 1200
BACKGROUNDCOLORS = ["Blossom-bg", "Dessert-bg", "Island-bg", "Mountain-bg", "Tropical-bg"]
ITEMSDIR         = "..\\Circle of Light"


# System Config

Probability = "Prob"
COLORS      = "Colors"
LEGENADRY   = "Legendary"
MYTHIC      = "Mythic"
COMMON      = "Common"
BACKGROUND  = "Background"
HAIR        = "Hair"
HORN        = "Horn"
EYES        = "Eyes"
GLASSES     = "Glasses"
ORB         = "Orb"
TYPE        = "Type"
RARITY      = "Rarity"
EYESCOLOR   = "EyesColor"
NAME        = "Name"


DragonType = {LEGENADRY:{Probability:0.01, COLORS:["Shiny"]},
              MYTHIC:   {Probability:0.05, COLORS:["Golden"]},
              COMMON:   {Probability:0.94, COLORS:["Amethyst", "Crystal", "Emerald", "Ruby", "Turquoise"]},
              }

ITEMS = {BACKGROUND:{TYPE: BACKGROUNDCOLORS},
         HAIR:      {TYPE:["Braid", "Curly", "Layered", "Straight", "Wavy", "Windy"]},
         HORN:      {TYPE:["Antler", "Argali", "Kudu", "Stag", "Tahr", "Unicorn"]},
         EYES:      {TYPE:["Almond", "Eyelash", "Hooded", "Monolid", "Round"]},
         EYESCOLOR: {TYPE:["Heather", "Orchid", "Violet"]},
         GLASSES:   {TYPE:["Heather", "Orchid", "Violet"]},
         ORB:       {TYPE:["Electra", "Ice", "Rock", "Sand", "Wind"]}
         }

# Dragon name = rarity_type_background_hair_horn_eyes_eyescolor_glasses_orb_
class Dragon:
    def __init__(self):
        self.info = {}



class DragonGenerator:
    dragons = []
    def __init__(self):
        pass

    def generate(self):
        dragon = Dragon()
        info = dragon.info
        info[RARITY], info[TYPE] = self.selectDragonType()
        info[NAME] = info[RARITY] + '_' + info[TYPE] + '_'

        for i in ITEMS.items():
            result = self.randomSelect(i[1][TYPE])
            info[NAME] += result + '_'
            info[i[0]] = result
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
        if newDragon not in dragons:
            dragons.append(newDragon)
            return true
        return false