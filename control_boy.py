from pico2d import *

import game_world
from grass import Grass
from boy import Boy
from game_world import *

# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global boy

    running = True

    boy = Boy()
    game_world.add_object(boy , 1)

    grass1 = Grass(40)
    game_world.add_object(grass1, 0)
    grass2 = Grass(20)
    game_world.add_object(grass2, 1)



def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
