import board
import neopixel
import time

led = neopixel.NeoPixel(board.D18, 7, pixel_order=neopixel.RGBW, auto_write=False)

led.fill((255, 0, 0, 0))
led.show()
time.sleep(2)

led.fill((0, 255, 0, 0))
led.show()
time.sleep(2)

led.fill((0, 0, 0, 0))
led.show()