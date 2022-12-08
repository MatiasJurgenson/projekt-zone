import pyglet
from pyglet.window import key, Window
from pyglet import clock
from pyglet.window import mouse
from pyglet import shapes
import random

game_window = pyglet.window.Window(800, 600)

class mängu_olekud: #panen siia kõik kohad mis võiks meil olla, ei pea kõiki tegema
    main_menu = 0
    room_1 = 1
    room_2 = 2
    boss = 3
    inventory = False
    paus = False
    võitlus = 6
    ruumivahetus = 7
    poemüüa = 8
    mäng_läbi = 9

mängu_olek = mängu_olekud.main_menu

alusta = pyglet.text.Label('Alustamiseks vajutage (ENTER)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=game_window.width//2, y=game_window.height//2-150,
                          anchor_x='center', anchor_y='center')

main_menu_info = pyglet.text.Label('Nupud/Paus menüü (P)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=game_window.width//2, y=game_window.height//2+100,
                          anchor_x='center', anchor_y='center')

pyglet.resource.path = ['raamatukogu']
pyglet.resource.reindex()

mängija_pilt = pyglet.resource.image("karakter.png")
vastane1_pilt = pyglet.resource.image("vastane1.png")
vastane2_pilt = pyglet.resource.image("vastane2.png")
taust_pilt = pyglet.resource.image("background.png")
mõõk = pyglet.resource.image("mõõk.png")
inventory = pyglet.resource.image("inventory.png")

inventory_sprite = pyglet.sprite.Sprite(img=inventory, x=100, y=150)


def center_image(image):
    #pildi ankur punktis on pildi keskkoht mitte alumine vasak nurk
    image.anchor_x = image.width // 2

center_image(mängija_pilt)
center_image(vastane1_pilt)
center_image(vastane2_pilt)
center_image(mõõk)


class Karakter:
    def __init__(self, sprite, mõõga_sprite, elud):
        self.sprite = sprite
        self.mõõga_sprite = mõõga_sprite
        self.elud = elud
        self.aktiivne_mõõk = False
        self.elus = True
        self.vigastatav = True

    def callback_vigastatav(self, dt):
        self.vigastatav = True
        print("woo")   

    def hit(self, damage):
        self.elud -= damage
        print(self.elud)
        if self.elud <= 0:
            print("surnu")
            self.elus = False

        clock.schedule_once(self.callback_vigastatav, 2)
    
    def attack(self, dt):
        if self.elus and not mängu_olekud.paus:
            print("yes")
            self.aktiivne_mõõk = True
            clock.schedule_once(self.callback_mõõk, 1)

    def callback_mõõk(self, dt):
        self.aktiivne_mõõk = False
        print("big brain")

    def callback_vigastatav(self, dt):
        self.vigastatav = True

    def joonista(self):
        if self.elus:
            self.sprite.draw()
        if self.aktiivne_mõõk:
            self.mõõga_sprite.draw()


class Mängija(Karakter):
    def collision_karakterid(self, enemy):
        if self.sprite.x + 50 > enemy.sprite.x -50 and self.sprite.x - 50 < enemy.sprite.x + 50 and self.vigastatav and enemy.elus:
            return True
        return False

    def collision_mõõk_vatsane(self, enemy):
        if self.sprite.x + 50 > enemy.mõõga_sprite.x -75 and self.sprite.x - 50 < enemy.mõõga_sprite.x + 75 and self.vigastatav and enemy.aktiivne_mõõk:
            return True
        return False


class Vastane(Karakter):
    def collision_mõõk_mängija(self):
        if mängija.mõõga_sprite.x + 75 > self.sprite.x -50 and mängija.mõõga_sprite.x - 75 < self.sprite.x + 50 and self.vigastatav and mängija.aktiivne_mõõk:
            return True
        return False


#                                    mängija sprite    x ja y on mägija positsioon ekraanil
mängija_sprite = pyglet.sprite.Sprite(img=mängija_pilt, x=400, y=100)
mängija_mõõk =  pyglet.sprite.Sprite(img=mõõk, x=500, y=200)
mängija = Mängija(mängija_sprite, mängija_mõõk, 100)

vastane1_sprite = pyglet.sprite.Sprite(img=vastane1_pilt, x=1200, y=100)
vastane1_mõõk = pyglet.sprite.Sprite(img=mõõk, x=1100, y=150)
vastane1 = Vastane(vastane1_sprite, vastane1_mõõk, 100)

vastane2_sprite = pyglet.sprite.Sprite(img=vastane2_pilt, x=800, y=100)
vastane2_mõõk = pyglet.sprite.Sprite(img=mõõk, x=700, y=150)
vastane2 = Vastane(vastane2_sprite, vastane2_mõõk, 100)


vastased = [vastane1, vastane2]


clk = clock.get_default()
clk.schedule_interval(vastane1.attack, 6)
clk.schedule_interval(vastane2.attack, 6)



vasakule, paremale = False, False

taust_x = 0

@game_window.event
def on_key_press(key, modifiers): #Looks for a keypress
    global vasakule, paremale
    if (key == pyglet.window.key.LEFT or key == pyglet.window.key.A) and mängu_olek == mängu_olekud.room_1 and not mängu_olekud.paus:
        vasakule = True
    elif (key == pyglet.window.key.RIGHT or key == pyglet.window.key.D) and mängu_olek == mängu_olekud.room_1 and not mängu_olekud.paus:
        paremale = True
    elif key == pyglet.window.key.SPACE and mängija.aktiivne_mõõk == False and mängu_olek == mängu_olekud.room_1 and not mängu_olekud.paus:
        mängija.attack(1)
    elif key == pyglet.window.key.P and not mängu_olekud.paus:
        mängu_olekud.paus = True
    elif key == pyglet.window.key.P and  mängu_olekud.paus:
        mängu_olekud.paus = False

@game_window.event
def on_key_release(key, modifiers):
    global vasakule, paremale, mängu_olek
    if key == pyglet.window.key.LEFT or key == pyglet.window.key.A and mängu_olek == mängu_olekud.room_1:
        vasakule = False
    elif key == pyglet.window.key.RIGHT or key == pyglet.window.key.D and mängu_olek == mängu_olekud.room_1:
        paremale = False
    elif key == pyglet.window.key.ENTER and mängu_olek == mängu_olekud.main_menu:
        mängu_olek = mängu_olekud.room_1
    elif key == pyglet.window.key.E and mängu_olekud.inventory == False:
        mängu_olekud.inventory = True
    elif key == pyglet.window.key.E and mängu_olekud.inventory == True:
        mängu_olekud.inventory = False

@game_window.event
def on_mouse_press(x, y, buttons, modifiers):
    if buttons & mouse.LEFT and x > 400:
        print("UwU")
        

@game_window.event
def liikumine(dt):
    global taust_x
    global mängu_olek
    if vasakule and taust_x >= -800 and taust_x < 0:
        taust_x += 5
        #toppi klassi
        vastane1.sprite.x += 5
        vastane1.mõõga_sprite.x += 5
        vastane2.sprite.x += 5
        vastane2.mõõga_sprite.x += 5
    elif paremale and taust_x > -800 and taust_x <= 0:
        taust_x -= 5
        #toppi klassi
        vastane1.sprite.x -= 5
        vastane1.mõõga_sprite.x -= 5
        vastane2.sprite.x -= 5
        vastane2.mõõga_sprite.x -= 5


    if mängija.collision_karakterid(vastane1):
        print("hit")
        mängija.vigastatav = False
        mängija.hit(20)

    if mängija.collision_mõõk_vatsane(vastane1):
        print("hit")
        mängija.vigastatav = False
        mängija.hit(20)

    for vastane in vastased:
        if vastane.collision_mõõk_mängija():
            print("hit")
            vastane.vigastatav = False
            vastane.hit(100)


    if mängija.elus == False:
        mängu_olek = mängu_olekud.mäng_läbi
        


@game_window.event
def on_draw():
    game_window.clear() # puhastab akna

    if mängu_olek == mängu_olekud.main_menu:
        game_window.clear()
        alusta.draw()
        main_menu_info.draw()
    
    elif  mängu_olek == mängu_olekud.room_1:
        game_window.clear()
        #joonistab asju 
        taust_pilt.blit(taust_x, 0)
        mängija.joonista()
        vastane1.joonista()
        vastane2.joonista()
        if mängu_olekud.paus:
            main_menu_info.draw()
        if mängu_olek == mängu_olekud.inventory:
            inventory_sprite.draw()

    elif mängu_olek == mängu_olekud.mäng_läbi:
        game_window.clear()


            

pyglet.clock.schedule_interval(liikumine, 1 / 120)

if __name__ == '__main__':
    pyglet.app.run()