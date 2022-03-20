from classes import *

def startOperation():
    generator = DragonGenerator()
    counter = 0
    while counter != 1:
        dragon = generator.generate()
        print(dragon.info)
        counter += 1



if __name__ == "__main__":
    # startOperation()
    img = Image.open('C:\\Users\\Pouya\Desktop\\NFT_Generator\\Circle of Light\\Background\\Blossom-bg.jpg')
    img2 = Image.open('C:\\Users\\Pouya\\Desktop\\NFT_Generator\\Circle of Light\\Body\\Amethyst\\Amethyst.png')
    print(img.format, img.size, img.mode)
    print(img2.format, img2.size, img2.mode)
    img3 = Image.alpha_composite(img, img2)
    img3.show()




