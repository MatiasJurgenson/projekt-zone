import pyglet
from pyglet import shapes
from pyglet.window import key, mouse

pyglet.options['audio'] = ('openal', 'pulse', 'xaudio2', 'directsound', 'silent')

window = pyglet.window.Window(900, 600, visible=False)
window.set_caption('A different caption')
x, y = window.get_location()
window.set_location(x+200, y)
batch = pyglet.graphics.Batch()

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

#lisab äpp ikoonid
#icon1 = pyglet.image.load('16x16.png')
#icon2 = pyglet.image.load('32x32.png')
#window.set_icon(icon1, icon2)
# ... perform some additional initialisation

#image = pyglet.resource.image('Untitled.png')

#def on_key_press(symbol, modifiers): #programm ei tee midagi enne kui nuppu pole vajutatud
#def on_text(text): #kui on vaja kirjutada ja mitte karakterit liigutada

#def on_mouse_press(x, y, button, modifiers):
 #   pass

#def on_mouse_release(x, y, button, modifiers):
  #  pass

#def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
#    pass

circle = shapes.Circle(x=100, y=150, radius=100, color=(50, 225, 30))
square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')


circle = shapes.Circle(100, 150, 100, color=(50, 225, 30), batch=batch)
square = shapes.Rectangle(200, 200, 200, 200, color=(55, 55, 255), batch=batch)

@window.event
def on_draw():
    window.clear()
    batch.draw()
    label.draw()
#    image.blit(0, 0) # mis kordinaatitel pilt joonitadakse

music = pyglet.resource.media('music.mp3') #pyglet.media.load() kui filepath on teada
music.play()



#sound = pyglet.resource.media('shot.wav', streaming=False) # kui on vaja midagi korduvalt kasutada
#sound.play()
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

window.set_visible()

pyglet.app.run()