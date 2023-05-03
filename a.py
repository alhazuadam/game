from pygame import *


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')


img_back = "galaxy.jpg"
img_hero = "rocket.png"


class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_y, player_speed):

        sprite.Sprite.__init__(self)