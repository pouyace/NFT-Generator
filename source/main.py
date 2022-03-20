from classes import *

def startOperation():
    generator = DragonGenerator()
    counter = 0
    while counter != 1:
        dragon = generator.generate()
        print(dragon.info)
        counter += 1



if __name__ == "__main__":
    startOperation()
    #img = Image.open('C:\\Users\\Pouya\Desktop\\NFT_Generator\\Circle of Light\\Background\\Blossom-bg.jpg')
    #img2 = Image.open('C:\\Users\\Pouya\\Desktop\\NFT_Generator\\Circle of Light\\Body\\Amethyst\\Amethyst.png')




