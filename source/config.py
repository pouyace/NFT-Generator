# User Config
NFTsCount = 1200
BACKGROUNDCOLORS = ["Blossom-bg", "Dessert-bg", "Island-bg", "Mountain-bg", "Tropical-bg"]
ITEMSDIR         = "..\\Circle of Light\\"
NFTsDir          = '..\\NFTs\\'

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
HEAD        = "Head"
BODY        = "Body"

DragonType = {LEGENADRY:{Probability:0.01, COLORS:["Shiny"]},
              MYTHIC:   {Probability:0.05, COLORS:["Golden"]},
              COMMON:   {Probability:0.94, COLORS:["Amethyst", "Crystal", "Emerald", "Ruby", "Turquoise"]},
              }

ITEMS = {BACKGROUND:{TYPE: BACKGROUNDCOLORS},
         BODY:      {},
         HAIR:      {TYPE:["Braid", "Curly", "Layered", "Straight", "Wavy", "Windy"]},
         HEAD:      {},
         HORN:      {TYPE:["Antler", "Argali", "Kudu", "Stag", "Tahr", "Unicorn"]},
         EYES:      {TYPE:["Almond", "Eyelash", "Hooded", "Monolid", "Round"]},
         EYESCOLOR: {TYPE:["Heather", "Orchid", "Violet"]},
         GLASSES:   {TYPE:["Heather", "Orchid", "Violet"]},
         ORB:       {TYPE:["Electra", "Ice", "Rock", "Sand", "Wind"]}
         }

# Dragon name = rarity_type_background_hair_horn_eyes_eyescolor_glasses_orb_