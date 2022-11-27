import pyglet
from pyglet.window import key, Window
from pyglet import clock
from pyglet.window import mouse

game_window = pyglet.window.Window(800, 600)

class mängu_olekud: #panen siia kõik kohad mis võiks meil olla, ei pea kõiki tegema
    main_menu = 0
    room_1 = 1
    room_2 = 2
    boss = 3
    paus = 4
    inventory = 5
    võitlus = 6
    ruumivahetus = 7
    peomüüa = 8
    mäng_läbi = 9

mängu_olek = mängu_olekud.main_menu

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=game_window.width//2, y=game_window.height//2,
                          anchor_x='center', anchor_y='center')

pyglet.resource.path = ['raamatukogu']
pyglet.resource.reindex()

mängija_pilt = pyglet.resource.image("karakter.png")
vastane1_pilt = pyglet.resource.image("vastane1.png")
vastane2_pilt = pyglet.resource.image("vastane2.png")
taust_pilt = pyglet.resource.image("background.png")
mõõk = pyglet.resource.image("mõõk.png")

def center_image(image):
    #pildi ankur punktis on pili keskkoht mitte alumine vasak nurk
    image.anchor_x = image.width // 2

center_image(mängija_pilt)
center_image(vastane1_pilt)
center_image(vastane2_pilt)
center_image(mõõk)




class mängija:
#                                       mängija sprite    x ja y on mägija positsioon ekraanil
    mängija_sprite = pyglet.sprite.Sprite(img=mängija_pilt, x=400, y=100)
    elud = 100


vastane1_sprite = pyglet.sprite.Sprite(img=vastane1_pilt, x=1200, y=100)

vigastatav = True #kas vastane saab mängijat vigastada

def collision(hero, enemy):
    if hero.x + 50 > enemy.x -50 and hero.x - 50 < enemy.x + 50:
        return True
    return False

def callback(a):
    global vigastatav
    vigastatav = True
    print(a) 

vasakule, paremale = False, False

taust_x = 0

@game_window.event
def on_key_press(key, modifiers): #Looks for a keypress
    global vasakule, paremale
    if key == pyglet.window.key.LEFT or key == pyglet.window.key.A:
        vasakule = True
    elif key == pyglet.window.key.RIGHT or key == pyglet.window.key.D:
        paremale = True

@game_window.event
def on_key_release(key, modifiers):
    global vasakule, paremale, mängu_olek
    if key == pyglet.window.key.LEFT or key == pyglet.window.key.A:
        vasakule = False
    elif key == pyglet.window.key.RIGHT or key == pyglet.window.key.D:
        paremale = False
    elif key == pyglet.window.key.ENTER:
        mängu_olek = mängu_olekud.room_1

@game_window.event
def on_mouse_press(x, y, buttons, modifiers):
    if buttons & mouse.LEFT and x > 400:
        print("UwU")
        

@game_window.event
def liikumine(dt):
    global taust_x
    global vigastatav
    if vasakule and taust_x >= -800 and taust_x < 0:
        taust_x += 5
        vastane1_sprite.x += 5
    elif paremale and taust_x > -800 and taust_x <= 0:
        taust_x -= 5
        vastane1_sprite.x -= 5

    if collision(mängija.mängija_sprite, vastane1_sprite) and vigastatav:
        vigastatav = False
        clock.schedule_once(callback, 2)
        


@game_window.event
def on_draw():
    game_window.clear() # puhastab akna

    if mängu_olek == mängu_olekud.main_menu:
        game_window.clear()
        label.draw()
    
    elif  mängu_olek == mängu_olekud.room_1:
        game_window.clear()
        #joonistab asju 
        taust_pilt.blit(taust_x, 0)
        mängija.mängija_sprite.draw()
        vastane1_sprite.draw()

pyglet.clock.schedule_interval(liikumine, 1 / 120)

if __name__ == '__main__':
    pyglet.app.run()