import math
from pynput.mouse import Controller
from pynput import keyboard
import numpy as np
import time

# CONFIG
center_pos = [698, 457]
n = 3
delay = 0.01

queue_start = False
end_loop = False
end_program = False
mouse = Controller()

def run():
    global center_pos, queue_start, n, mouse, end_loop, delay
    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()
    while not end_program:
        if (queue_start):
            queue_start = False
            center = np.array(center_pos)
            mouse_pos = np.array(mouse.position)
            disp_vec = center - mouse_pos
            length = np.linalg.norm(disp_vec)
            beginning_theta = math.degrees(math.atan(disp_vec[1] / disp_vec[0]))
            d_theta = 360 / n
            for i in range(1,n+1):
                if (end_loop):
                    end_loop = False
                    break
                theta = math.radians(beginning_theta + d_theta * i)
                mouse_disp = np.array([length * math.cos(theta), length * math.sin(theta)])
                mouse.position = np.asarray(center_pos + mouse_disp)
                time.sleep(delay)

def on_press(key):
    try:
        global center_pos, queue_start, end_loop, end_program
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if (key.char == "c"):
            center_pos = mouse.position
            print(mouse.position)
        if (key.char == "r"): queue_start = True
        if (key.char == "s"): end_loop = True
        if (key.char == "q"): end_program = True
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

if __name__ == '__main__':
    run()
