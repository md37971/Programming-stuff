from ursina import*
import time,random


#Settings
""""
application.development_mode = False
window.exit_button.enabled = False
window.fps_counter.enabled = False
window.cog_button.enabled = False
"""

#updatefunction
def update():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    global speed
    cube.color = color.rgb(r,g,b)
    cube.x = cube.x + time.dt * speed
    cube.rotation_y = cube.rotation_y + time.dt * 100
    #cube.y = cube.position.y + time.dt * -abs(random.randint(1,5))
    if abs(cube.x) > 5:
        speed = speed * -1
    if abs(cube.x) < -5:
        speed = speed * 1
    

#Application
app = Ursina()
speed = 3
cube = Entity(model="cube", position = (0,0,0))
app.run()
