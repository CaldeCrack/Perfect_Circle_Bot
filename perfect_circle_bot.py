from pynput.mouse import Button, Controller
from pynput import keyboard
import time
import math

RADIUS: int = 330
STEPS: int = 360
WAIT: float = 0.005

mouse: Controller = Controller()

def on_press(key):
  x: int = 0
  y: int = 0
  if key == keyboard.Key.enter:
    x, y = mouse.position
    mouse.position = (x + RADIUS, y)
    mouse.press(Button.left)

    start = time.perf_counter()
    for i in range(1, STEPS):
      target = start + i * WAIT
      angle: float = (i / STEPS) * 2 * math.pi
      new_x: int = x + round(RADIUS * math.cos(angle))
      new_y: int = y + round(RADIUS * math.sin(angle))
      mouse.position = (new_x, new_y)

      while time.perf_counter() < target:
        pass

    while time.perf_counter() < start + STEPS * WAIT:
      pass
    mouse.position = (x + RADIUS, y)
    mouse.release(Button.left)
    mouse.position = (x, y)

def on_release(key):
  if key == keyboard.Key.esc:
    raise keyboard.Listener.StopException

def main():
  print("Press Enter to draw a perfect circle around your mouse 🟢.")
  print("Press Esc to exit 💥.")
  listener = keyboard.Listener(on_press=on_press, on_release=on_release)
  listener.start()
  listener.join()

if __name__ == "__main__":
  main()
