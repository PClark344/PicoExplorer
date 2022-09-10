import time
import random
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P8

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P8)

WIDTH, HEIGHT = display.get_bounds()

# We're creating 100 lights with their own individual colour and 1 BG colour
# for a total of 101 colours, which will all fit in the custom 256 entry palette!


class Light:
    def __init__(self, x, y, r, dx, dy, pen):
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.pen = pen


# initialise shapes
lights = []
for i in range(0, 3):


    r = 20
    
    lights.append(
        Light(
            random.randint(r, r + (WIDTH - 2 * r)),
            random.randint(r, r + (HEIGHT - 2 * r)),
            r,
            0,
            0,
            #display.create_pen(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            display.create_pen(222,100,22),
        )
    )

BG = display.create_pen(40, 40, 40)

while True:
    display.set_pen(BG)
    display.clear()

    for light in lights:
        light.x += light.dx
        light.y += light.dy

        xmax = WIDTH - light.r
        xmin = light.r
        ymax = HEIGHT - light.r
        ymin = light.r

        if light.x < xmin or light.x > xmax:
            light.dx *= -1

        if light.y < ymin or light.y > ymax:
            light.dy *= -1

        display.set_pen(light.pen)
        display.circle(int(light.x), int(light.y), int(light.r))

    display.update()
    time.sleep(0.01)
