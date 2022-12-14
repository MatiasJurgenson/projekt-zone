import pyglet
from pyglet.window import key, Window
from pyglet import clock
from pyglet.window import mouse
from pyglet import shapes
import random

game_window = pyglet.window.Window(800, 600)

#batch - saab lisada hulk asju mida samal ajal joonistada
batch_paus = pyglet.graphics.Batch()
batch_müük = pyglet.graphics.Batch()
square = shapes.Rectangle(0, 0, 800, 600, color=(0, 0, 0), batch=batch_paus)
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
    ruumivahetus2 = 11
    ruumivahetus3 = 12
    poemüüa = False
    mäng_läbi = 9

mängu_olek = mängu_olekud.main_menu

#main menu tekst
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


#pausmenuu tekst
paus_info = pyglet.text.Label('Nupud/Paus menüü (P)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=50, y=500, batch=batch_paus)   

inventory_info = pyglet.text.Label('Inventar (E)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=50, y=400, batch=batch_paus)
                          

attack_info = pyglet.text.Label('rünnak (tühik)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=50, y=300, batch=batch_paus)

liikumine_vasak_info = pyglet.text.Label('Liikumine vasakule (A/vasak nool)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=50, y=200, batch=batch_paus)

liikumine_parem_info = pyglet.text.Label('Liikumine paremale (D/parem nool)',
                          font_name='Times New Roman',
                          font_size=36,
                          x=50, y=100, batch=batch_paus)

allaminek = pyglet.text.Label('Järgmine korrus (vajuta S/nool alla)',
                          font_name='Times New Roman',
                          font_size=30,
                          x=game_window.width//2, y=game_window.height//2+100,
                          anchor_x='center', anchor_y='center')
allaminek.color = (0, 0, 0, 255)


#poodlemise tekst
poodlemine = pyglet.text.Label('Poodlemine (vajuta W/nool üles)',
                          font_name='Times New Roman',
                          font_size=30,
                          x=game_window.width//2, y=game_window.height//2+100,
                          anchor_x='center', anchor_y='center')
poodlemine.color = (0, 0, 0, 255)

lahkumine = pyglet.text.Label('Lahkumine (vajuta W/nool üles)',
                          font_name='Times New Roman',
                          font_size=30,
                          x=game_window.width//2, y=500,
                          anchor_x='center', anchor_y='center', batch=batch_müük)

uuenda_mõõk_1 = pyglet.text.Label('Uuenda mõõka',
                          font_name='Times New Roman',
                          font_size=30,
                          x=50, y=game_window.height//2+50,
                          anchor_y='center', batch=batch_müük)

uuenda_mõõk_2 = pyglet.text.Label('(Vajutage 1)',
                          font_name='Times New Roman',
                          font_size=30,
                          x=50, y=game_window.height//2-50,
                          anchor_y='center', batch=batch_müük)

uuenda_mõõk_3 = pyglet.text.Label('Maksab 30',
                          font_name='Times New Roman',
                          font_size=30,
                          x=50, y=game_window.height//2-100,
                          anchor_y='center', batch=batch_müük)

elustamine_1 = pyglet.text.Label('Täitke elud',
                          font_name='Times New Roman',
                          font_size=30,
                          x=500, y=game_window.height//2+50,
                          anchor_y='center', batch=batch_müük)

elustamine_2 = pyglet.text.Label('(Vajutage 2)',
                          font_name='Times New Roman',
                          font_size=30,
                          x=500, y=game_window.height//2-50,
                          anchor_y='center', batch=batch_müük)

elustamine_3 = pyglet.text.Label('maksab 20',
                          font_name='Times New Roman',
                          font_size=30,
                          x=500, y=game_window.height//2-100,
                          anchor_y='center', batch=batch_müük)

#ruumivahetustekst
ruumivahetus = pyglet.text.Label('Sisenete ruumi 2',
                          font_name='Times New Roman',
                          font_size=36,
                          x=game_window.width//2, y=game_window.height//2,
                          anchor_x='center', anchor_y='center')

ruumivahetus2 = pyglet.text.Label('Sisenete bossi ruumi',
                          font_name='Times New Roman',
                          font_size=36,
                          x=game_window.width//2, y=game_window.height//2,
                          anchor_x='center', anchor_y='center')

ruumivahetus3 = pyglet.text.Label('Mäng läbi',
                          font_name='Times New Roman',
                          font_size=36,
                          x=game_window.width//2, y=game_window.height//2,
                          anchor_x='center', anchor_y='center')


pyglet.resource.path = ['raamatukogu']
pyglet.resource.reindex()

mängija_pilt = pyglet.resource.image("karakter.png")
vastane1_pilt = pyglet.resource.image("vastane1.png")
vastane2_pilt = pyglet.resource.image("vastane2.png")
vastane3_pilt = pyglet.resource.image("vastane3.png")
vastane4_pilt = pyglet.resource.image("vastane4.png")
boss_pilt = pyglet.resource.image("boss.png")
taust1_pilt = pyglet.resource.image("taust1.png")
taust2_pilt = pyglet.resource.image("taust2.png")
taust3_pilt = pyglet.resource.image("taust3.png")

mõõk = pyglet.resource.image("mõõk.png")
mõõk2 = pyglet.resource.image("mõõk2.png")
inventory = pyglet.resource.image("inventory.png")
müüja_pilt = pyglet.resource.image("müüja.png")

inventory_sprite = pyglet.sprite.Sprite(img=inventory, x=100, y=150)


def center_image(image):
    #pildi ankur punktis on pildi keskkoht mitte alumine vasak nurk
    image.anchor_x = image.width // 2

center_image(mängija_pilt)
center_image(vastane1_pilt)
center_image(vastane2_pilt)
center_image(vastane3_pilt)
center_image(vastane4_pilt)
center_image(boss_pilt)
center_image(müüja_pilt)
center_image(mõõk)
center_image(mõõk2)


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
                #print("surnud")
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
        self.rahakott = 10
        self.mõõga_võimsus = 50

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




#                                    mängija sprite    x ja y on mängija positsioon ekraanil
mängija_sprite = pyglet.sprite.Sprite(img=mängija_pilt, x=400, y=100)
mängija_mõõk =  pyglet.sprite.Sprite(img=mõõk, x=500, y=170)
mängija = Mängija(mängija_sprite, mängija_mõõk, 100)

vastane1_sprite = pyglet.sprite.Sprite(img=vastane1_pilt, x=1300, y=100)
vastane1_mõõk = pyglet.sprite.Sprite(img=mõõk2, x=1200, y=190)
vastane1 = Vastane(vastane1_sprite, vastane1_mõõk, 100)

vastane2_sprite = pyglet.sprite.Sprite(img=vastane2_pilt, x=900, y=100)
vastane2_mõõk = pyglet.sprite.Sprite(img=mõõk2, x=800, y=160)
vastane2 = Vastane(vastane2_sprite, vastane2_mõõk, 100)

vastane3_sprite = pyglet.sprite.Sprite(img=vastane3_pilt, x=1000, y=100)
vastane3_mõõk = pyglet.sprite.Sprite(img=mõõk2, x=900, y=160)
vastane3 = Vastane(vastane3_sprite, vastane3_mõõk, 200)

vastane4_sprite = pyglet.sprite.Sprite(img=vastane4_pilt, x=1800, y=100)
vastane4_mõõk = pyglet.sprite.Sprite(img=mõõk2, x=1700, y=160)
vastane4 = Vastane(vastane4_sprite, vastane4_mõõk, 200)

boss_sprite = pyglet.sprite.Sprite(img=boss_pilt, x=1000, y=100)
boss_mõõk = pyglet.sprite.Sprite(img=mõõk2, x=900, y=160)
boss = Vastane(boss_sprite, boss_mõõk, 200)

poemüüja_sprite = pyglet.sprite.Sprite(img=müüja_pilt, x=1800, y=100)
poemüüja = Vastane(poemüüja_sprite, vastane4_mõõk, 100)

inventory_järjend = [mängija.mõõga_sprite, mängija.rahakott]
room1_vastased = [vastane1, vastane2]
room2_vastased = [vastane3, vastane4]
room3_vastased = [boss]
vastased = [room1_vastased, room2_vastased, room3_vastased]


clk = clock.get_default()
clk.schedule_interval(vastane1.attack, 6)
clk.schedule_interval(vastane2.attack, 6)
clk.schedule_interval(vastane3.attack, 4)
clk.schedule_interval(vastane4.attack, 4)
clk.schedule_interval(boss.attack, 3)



vasakule, paremale = False, False
taust_x = 0

def callback_ruumivahetus(dt):
    global mängu_olek
    mängu_olek = mängu_olekud.room_2

def callback_ruumivahetus2(dt):
    global mängu_olek
    mängu_olek = mängu_olekud.boss

def callback_ruumivahetus3(dt):
    global mängu_olek
    mängu_olek = mängu_olekud.main_menu

@game_window.event
def on_key_press(key, modifiers): #Looks for a keypress
    global vasakule, paremale, taust_x, taust, mängu_olek

    #liikumine
    if (key == pyglet.window.key.LEFT or key == pyglet.window.key.A) and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2 or mängu_olek == mängu_olekud.boss) and not mängu_olekud.paus:
        vasakule = True
    elif (key == pyglet.window.key.RIGHT or key == pyglet.window.key.D) and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2 or mängu_olek == mängu_olekud.boss) and not mängu_olekud.paus:
        paremale = True

    #rünnak
    elif key == pyglet.window.key.SPACE and mängija.aktiivne_mõõk == False and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2 or mängu_olek == mängu_olekud.boss) and not mängu_olekud.paus:
        mängija.attack(1)

    # paus
    elif key == pyglet.window.key.P and not mängu_olekud.paus:
        mängu_olekud.paus = True
    elif key == pyglet.window.key.P and  mängu_olekud.paus:
        mängu_olekud.paus = False

    #poemüük
    elif (key == pyglet.window.key.W or key == pyglet.window.key.UP)and not mängu_olekud.poemüüa and mängija.collision_karakterid(poemüüja):
        mängu_olekud.poemüüa = True
    elif (key == pyglet.window.key.W or key == pyglet.window.key.UP) and  mängu_olekud.poemüüa:
        mängu_olekud.poemüüa = False

    # ruumivahetus
    elif (key == pyglet.window.key.DOWN or key == pyglet.window.key.S) and mängu_olek == mängu_olekud.room_1 and not mängu_olekud.paus and -taust + 100 >= taust_x:
        mängu_olek = mängu_olekud.ruumivahetus
        taust_x = 0
        clock.schedule_once(callback_ruumivahetus, 3)
    elif (key == pyglet.window.key.DOWN or key == pyglet.window.key.S) and mängu_olek == mängu_olekud.room_2 and not mängu_olekud.paus and -taust + 100 >= taust_x:
        mängu_olek = mängu_olekud.ruumivahetus2
        taust_x = 0
        clock.schedule_once(callback_ruumivahetus2, 3)
    elif (key == pyglet.window.key.DOWN or key == pyglet.window.key.S) and mängu_olek == mängu_olekud.boss and not mängu_olekud.paus and -taust + 100 >= taust_x:
        mängu_olek = mängu_olekud.ruumivahetus3
        taust_x = 0
        clock.schedule_once(callback_ruumivahetus3, 3)


@game_window.event
def on_key_release(key, modifiers):
    global vasakule, paremale, mängu_olek

    #liikumine
    if (key == pyglet.window.key.LEFT or key == pyglet.window.key.A) and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2 or mängu_olek == mängu_olekud.boss):
        vasakule = False
    elif (key == pyglet.window.key.RIGHT or key == pyglet.window.key.D) and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2 or mängu_olek == mängu_olekud.boss):
        paremale = False

    #mängu sisenemine
    elif key == pyglet.window.key.ENTER and mängu_olek == mängu_olekud.main_menu:
        mängu_olek = mängu_olekud.room_1

    #inventory
    elif (key == pyglet.window.key.E and mängu_olekud.inventory == False) and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2 or mängu_olek == mängu_olekud.boss):
        mängu_olekud.inventory = True
    elif (key == pyglet.window.key.E and mängu_olekud.inventory == True) and (mängu_olek == mängu_olekud.room_1 or mängu_olek == mängu_olekud.room_2 or mängu_olek == mängu_olekud.boss):
        mängu_olekud.inventory = False

    #poemüük
    elif key == pyglet.window.key._2 and mängu_olekud.poemüüa and mängija.rahakott >= 20:
        mängija.elud = 100
        mängija.rahakott -= 20
    
    elif key == pyglet.window.key._1 and mängu_olekud.poemüüa and mängija.rahakott >= 30:
        mängija.mõõga_võimsus *= 1.5
        mängija.rahakott -= 30

#test
@game_window.event
def on_mouse_press(x, y, buttons, modifiers):
    if buttons & mouse.LEFT and x > 400 and mängu_olekud.poemüüa and mängija.rahakott >= 20:
        mängija.elud = 100
        mängija.rahakott -= 20
    elif buttons & mouse.LEFT and x < 400 and mängu_olekud.poemüüa and mängija.rahakott >= 30:
        mängija.mõõga_võimsus *= 1.5
        mängija.rahakott -= 30
        

@game_window.event
def liikumine(dt):
    global taust_x, taust, mängu_olek

    #liigutab tausta ja vastaseid
    if vasakule and taust_x >= -taust and taust_x < 0:
        taust_x += 5

        poemüüja.liikuvus(5)

        if mängu_olek == mängu_olekud.room_1:
                for vastane_1 in vastased[0]:
                    vastane_1.liikuvus(5)

        elif mängu_olek == mängu_olekud.room_2:
                for vastane_2 in vastased[1]:
                    vastane_2.liikuvus(5)
    elif paremale and taust_x > -taust and taust_x <= 0:
        taust_x -= 5

        poemüüja.liikuvus(-5)

        if mängu_olek == mängu_olekud.room_1:
                for vastane_1 in vastased[0]:
                    vastane_1.liikuvus(-5)

        elif mängu_olek == mängu_olekud.room_2:
                for vastane_2 in vastased[1]:
                    vastane_2.liikuvus(-5)
    
    elif paremale and taust_x > -taust and taust_x <= 0:
        taust_x -= 5

        if mängu_olek == mängu_olekud.boss:
                for vastane_3 in vastased[2]:
                    vastane_3.liikuvus(-5)
    
    

    #collision vaataja
    if poemüüja.collision_mõõk_mängija():
        poemüüja.vigastatav = False
        poemüüja.hit(mängija.mõõga_võimsus)
            
    if mängu_olek == mängu_olekud.room_1:
        for vastane_1 in vastased[0]:
            if vastane_1.collision_mõõk_mängija():
                #print("hit")
                vastane_1.vigastatav = False
                vastane_1.hit(mängija.mõõga_võimsus)

            if mängija.collision_mõõk_vatsane(vastane_1) or mängija.collision_karakterid(vastane_1):
                #print("hit")
                mängija.vigastatav = False
                mängija.hit(20)
    
    elif mängu_olek == mängu_olekud.room_2:
        for vastane_2 in vastased[1]:
            if vastane_2.collision_mõõk_mängija() or poemüüja.collision_mõõk_mängija():
                #print("hit")
                vastane_2.vigastatav = False
                vastane_2.hit(mängija.mõõga_võimsus)

            if mängija.collision_mõõk_vatsane(vastane_2) or mängija.collision_karakterid(vastane_2):
                #print("hit")
                mängija.vigastatav = False
                mängija.hit(25)

            
    elif mängu_olek == mängu_olekud.boss:
        for vastane_3 in vastased[2]:
            if vastane_3.collision_mõõk_mängija() or poemüüja.collision_mõõk_mängija():
                #print("hit")
                vastane_3.vigastatav = False
                vastane_3.hit(mängija.mõõga_võimsus)
            
            if mängija.collision_mõõk_vatsane(vastane_3) or mängija.collision_karakterid(vastane_3):
                #print("hit")
                mängija.vigastatav = False
                mängija.hit(30)

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
        #restarib vastaste positsioonid
        if vastane1.elus:
            vastane1.sprite.x = 1300
            vastane1.mõõga_sprite.x = 1200

        if vastane4.elus:
            vastane4.sprite.x = 1600
            vastane4.mõõga_sprite.x = 1500

        if vastane3.elus:
            vastane3.sprite.x = 1000
            vastane3.mõõga_sprite.x = 900

        if vastane2.elus:
            vastane2.sprite.x = 900
            vastane2.mõõga_sprite.x = 800

        if boss.elus:
            boss.sprite.x = 1000
            boss.mõõga_sprite.x = 900        
    

    
    elif  mängu_olek == mängu_olekud.room_1:
        taust = taust2_pilt.width // 2
        game_window.clear()
        #joonistab asju 
        taust1_pilt.blit(taust_x, 0)
        mängija.joonista()
        vastane1.joonista()
        vastane2.joonista()
        poemüüja.joonista()
        if mängu_olek == mängu_olekud.inventory:
            inventory_sprite.draw()
        if -taust + 100 >= taust_x:
            allaminek.draw()
        if mängija.collision_karakterid(poemüüja):
            poodlemine.draw()
    
    elif  mängu_olek == mängu_olekud.room_2:
        taust = taust2_pilt.width - 800
        game_window.clear()
        #joonistab asju 
        taust2_pilt.blit(taust_x, 0)
        mängija.joonista()
        vastane3.joonista()
        vastane4.joonista()
        poemüüja.joonista()
        print(mängija.mõõga_võimsus)
        if mängu_olek == mängu_olekud.inventory:
            inventory_sprite.draw()
        #print(taust_x)
        if -taust + 100 >= taust_x:
            allaminek.draw()
        if mängija.collision_karakterid(poemüüja):
            poodlemine.draw()
    
    elif  mängu_olek == mängu_olekud.boss:
        taust = taust2_pilt.width - 800
        game_window.clear()
        #joonistab asju 
        taust3_pilt.blit(taust_x, 0)
        mängija.joonista()
        boss.joonista()
        if mängu_olek == mängu_olekud.inventory:
            inventory_sprite.draw()
        #print(taust_x)
        if -taust + 100 >= taust_x:
            allaminek.draw()

    elif mängu_olek == mängu_olekud.mäng_läbi:
        game_window.clear()
    
    elif mängu_olek == mängu_olekud.ruumivahetus:
        game_window.clear()
        ruumivahetus.draw()
        poemüüja.sprite.x = 2100
    
    elif mängu_olek == mängu_olekud.ruumivahetus2:
        game_window.clear()
        ruumivahetus2.draw()
        poemüüja.sprite.x = 2100
    
    elif mängu_olek == mängu_olekud.ruumivahetus3:
        game_window.clear()
        ruumivahetus3.draw()

    if mängu_olekud.paus:
        if mängu_olek == mängu_olekud.main_menu:
            game_window.clear()
        batch_paus.draw()

    if mängu_olekud.poemüüa:
        game_window.clear()
        raha = pyglet.text.Label(f'raha kokku: {mängija.rahakott}',
                          font_name='Times New Roman',
                          font_size=30,
                          x=game_window.width//2, y=450,
                          anchor_x='center', anchor_y='center')
        raha.draw()
        batch_müük.draw()


            

pyglet.clock.schedule_interval(liikumine, 1 / 120)

if __name__ == '__main__':
    pyglet.app.run()