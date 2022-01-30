
################################################################
#                     MoYu Studio © 2021                       #
################################################################
#                          Tinyland                            #
#                      SUGT06 a20 Bata                         #
################################################################
#                         MoYu Engine                          #
#                       Powed by OpenGL                        #
#                   Pyglet & Arcade & PyMunk                   #
################################################################

import pyglet
import arcade

import config.data.constants as C
import config.window as window
import config.system as system

def main():

    system.AssetsSystem.loader()

    screen = arcade.Window(C.window['width'],
                           C.window['height'],
                           C.window['title'],
                           C.window['fullscreen'],
                           C.window['resizable'],
                           C.window['update_rate'],
                           C.window['antialiasing'],
                           C.window['gl_version'],
                           C.window['screen'],
                           C.window['style'],
                           C.window['visible'],
                           C.window['vsync'],
                           C.window['gc_mode'],
                           C.window['center_window'],
                           )

    screen.set_icon(pyglet.image.load('moyu_engine/assets/graphics/tile/tileland/tileland1.png'))

    main_window = window.main_window.MainWindow()

    screen.show_view(main_window)

    main_window.setup()
    
    arcade.run()


if __name__ == '__main__':
    main()