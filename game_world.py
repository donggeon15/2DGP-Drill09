#wolrd[0]에는 백그라운드 객체들
#world[1]에는 앞에 객체들
world = [], []

def add_object(o, depth):
    world[depth].append(o)

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    print(f'CRETICAL: 존재하지않는 객체{o}를 지우려고 합니다.')