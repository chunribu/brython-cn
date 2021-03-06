from browser import document, window

moving = document["rot15"]
x = 0
dx = 3
run = None

def change(event):
    global run
    if run is None:
        # start animation
        animloop(1)
    else:
        # stop animation
        window.cancelAnimationFrame(run)
        run = None

document["button15"].bind("click", change)

def render():
    global x, dx
    moving.style.transform = "translate({}px,0)".format(x)
    x += dx
    if x > document["zone15"].offsetWidth-moving.offsetWidth:
        dx = -dx
        moving.html = "◄" # left triangle
    elif x <= 0:
        dx = -dx
        moving.html = "►" # right triangle

def animloop(t):
    global run
    run = window.requestAnimationFrame(animloop)
    render()