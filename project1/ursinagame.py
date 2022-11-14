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
    cube.rotation_x = cube.rotation_x + time.dt*100
    cube.rotation_y = cube.rotation_y + time.dt*100
    cube.x = cube.position.x + time.dt * random.randint(1,5)
    print(cube.x)
    #cube.y = cube.position.y + time.dt * -abs(random.randint(1,5))
    if abs(cube.x) > 3:
        speed = speed * -1
        #cube.x =-6


#Application
app = Ursina()
speed = 3
cube = Entity(model="cube", position = (3,2,6))
text = Text(text = "Cat",scale = 5)
app.run()


  

