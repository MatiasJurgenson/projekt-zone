import pyglet
from pyglet.window import key, Window
from pyglet import clock
from pyglet.window import mouse
from pyglet import shapes
import random

game_window = pyglet.window.Window(800, 600)


batch = pyglet.graphics.Batch()
square = shapes.Rectangle(0, 0, 800, 600, color=(0, 0, 0), batch=batch)
square.opacity = 75

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

paus_info = pyglet.text.Label('Nupud/Paus menüü (P)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=50, y=500, batch=batch)   

inventory_info = pyglet.text.Label('Inventar (E)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=50, y=400, batch=batch)
                          

attack_info = pyglet.text.Label('rünnak (tühik)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=50, y=300, batch=batch)

liikumine_vasak_info = pyglet.text.Label('Liikumine vasakule (A/vasak nool)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=50, y=200, batch=batch)

liikumine_parem_info = pyglet.text.Label('Liikumine paremale (D/parem nool)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=50, y=100, batch=batch)

allaminek = pyglet.text.Label('Järgimne korrus (vajuta S/nool alla)',
                          font_name='Times New Roman',
                          font_size=30,
                          x=game_window.width//2, y=game_window.height//2+100,
                          anchor_x='center', anchor_y='center')
allaminek.color = (0, 0, 0, 255)

ruumivahetus = pyglet.text.Label('Sisenete ruumi 2',
                          font_name='Times New Roman',
                          font_size=36,
                          x=game_window.width//2, y=game_window.height//2,
                          anchor_x='center', anchor_y='center')



pyglet.resource.path = ['raamatukogu']
pyglet.resource.reindex()

mängija_pilt = pyglet.resource.image("karakter.png")
vastane1_pilt = pyglet.resource.image("vastane1.png")
vastane2_pilt = pyglet.resource.image("vastane2.png")
taust1_pilt = pyglet.resource.image("background.png")
taust2_pilt = pyglet.resource.image("backlong.png")

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
        #print("woo")   

    def hit(self, damage):
        if self.elus:
            self.elud -= damage
            #print(self.elud)
            if self.elud <= 0:
                #print("surnu")
                self.elus = False
                mängija.rahakott += random.randint(10, 20)
                #print(mängija.rahakott)

        clock.schedule_once(self.callback_vigastatav, 2)
    
    def attack(self, dt):
        if self.elus and not mängu_olekud.paus:
            #print("yes")
            self.aktiivne_mõõk = True
            clock.schedule_once(self.callback_mõõk, 1)

    def callback_mõõk(self, dt):
        self.aktiivne_mõõk = False
        #print("big brain")

    def callback_vigastatav(self, dt):
        self.vigastatav = True

    def joonista(self):
        if self.elus:
            self.sprite.draw()
        if self.aktiivne_mõõk:
            self.mõõga_sprite.draw()


class Mängija(Karakter):
    def __init__(self, sprite, mõõga_sprite, elud):
        super().__init__(sprite, mõõga_sprite, elud)
        self.rahakott = 0

    def collision_karakterid(self, enemy):
        if self.sprite.x + 50 > enemy.sprite.x -50 and self.sprite.x - 50 < enemy.sprite.x + 50 and self.vigastatav and enemy.elus:
            return True
        return False

    def collision_mõõk_vatsane(self, enemy):
        if self.sprite.x + 50 > enemy.mõõga_sprite.x -75 and self.sprite.x - 50 < enemy.mõõga_sprite.x + 75 and self.vigastatav and enemy.aktiivne_mõõk:
            return True
        return False
    
    def joonista(self):
        label = pyglet.text.Label(f"Elud {self.elud}",
                          font_name='Times New Roman',
                          font_size=36,
                          x=25, y=545)
        label.color = (0, 0, 0, 255)
        label.draw()
        super().joonista()


class Vastane(Karakter):
    def collision_mõõk_mängija(self):
        if mängija.mõõga_sprite.x + 75 > self.sprite.x -50 and mängija.mõõga_sprite.x - 75 < self.sprite.x + 50 and self.vigastatav and mängija.aktiivne_mõõk:
            return True
        return False

    def liikuvus(self,arv):
        self.sprite.x += arv
        self.mõõga_sprite.x += arv



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


inventory_järjend = [mängija.mõõga_sprite, mängija.rahakott]
vastased = [vastane1, vastane2]


clk = clock.get_default()
clk.schedule_interval(vastane1.attack, 6)
clk.schedule_interval(vastane2.attack, 6)



vasakule, paremale = False, False
taust_x = 0

def callback_ruumivahetus(dt):
    global mängu_olek
    mängu_olek = mängu_olekud.room_2

@game_window.event
def on_key_press(key, modifiers): #Looks for a keypress
    global vasakule, paremale, taust_x, taust, mängu_olek
    if (key == pyglet.window.key.LEFT or key == pyglet.window.key.A) and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2) and not mängu_olekud.paus:
        vasakule = True
    elif (key == pyglet.window.key.RIGHT or key == pyglet.window.key.D) and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2) and not mängu_olekud.paus:
        paremale = True
    elif key == pyglet.window.key.SPACE and mängija.aktiivne_mõõk == False and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2) and not mängu_olekud.paus:
        mängija.attack(1)
    elif key == pyglet.window.key.P and not mängu_olekud.paus:
        mängu_olekud.paus = True
    elif key == pyglet.window.key.P and  mängu_olekud.paus:
        mängu_olekud.paus = False
    elif (key == pyglet.window.key.DOWN or key == pyglet.window.key.S) and mängu_olek == mängu_olekud.room_1 and not mängu_olekud.paus and -taust + 100 >= taust_x:
        mängu_olek = mängu_olekud.ruumivahetus
        taust_x = 0
        clock.schedule_once(callback_ruumivahetus, 3)


@game_window.event
def on_key_release(key, modifiers):
    global vasakule, paremale, mängu_olek
    if (key == pyglet.window.key.LEFT or key == pyglet.window.key.A) and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2):
        vasakule = False
    elif (key == pyglet.window.key.RIGHT or key == pyglet.window.key.D) and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2):
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
    global taust_x, taust, mängu_olek
    if vasakule and taust_x >= -taust and taust_x < 0:
        taust_x += 5

        for vastane in vastased:
            vastane.liikuvus(5)
    elif paremale and taust_x > -taust and taust_x <= 0:
        taust_x -= 5

        for vastane in vastased:
            vastane.liikuvus(-5)

    #collision vaataja
    for vastane in vastased:
        if vastane.collision_mõõk_mängija():
            #print("hit")
            vastane.vigastatav = False
            vastane.hit(100)
        if mängija.collision_mõõk_vatsane(vastane) or mängija.collision_karakterid(vastane):
            #print("hit")
            mängija.vigastatav = False
            mängija.hit(20)


    if mängija.elus == False:
        mängu_olek = mängu_olekud.mäng_läbi
        


@game_window.event
def on_draw():
    global taust
    game_window.clear() # puhastab akna

    if mängu_olek == mängu_olekud.main_menu:
        game_window.clear()
        alusta.draw()
        main_menu_info.draw()
    
    elif  mängu_olek == mängu_olekud.room_1:
        taust = taust2_pilt.width // 2
        game_window.clear()
        #joonistab asju 
        taust2_pilt.blit(taust_x, 0)
        mängija.joonista()
        vastane1.joonista()
        vastane2.joonista()
        if mängu_olek == mängu_olekud.inventory:
            inventory_sprite.draw()
        if -taust + 100 >= taust_x:
            allaminek.draw()
    
    elif  mängu_olek == mängu_olekud.room_2:
        taust = taust1_pilt.width // 2
        game_window.clear()
        #joonistab asju 
        taust1_pilt.blit(taust_x, 0)
        mängija.joonista()
        if mängu_olek == mängu_olekud.inventory:
            inventory_sprite.draw()
        print(taust_x)
            

    elif mängu_olek == mängu_olekud.mäng_läbi:
        game_window.clear()
    
    elif mängu_olek == mängu_olekud.ruumivahetus:
        game_window.clear()
        ruumivahetus.draw()

    if mängu_olekud.paus:
        if mängu_olek == mängu_olekud.main_menu:
            game_window.clear()
        batch.draw()

            

pyglet.clock.schedule_interval(liikumine, 1 / 120)

if __name__ == '__main__':
    pyglet.app.run()