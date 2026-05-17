import board
import neopixel
import time

led = neopixel.NeoPixel(
    board.D18,
    7,
    pixel_order=neopixel.RGBW,
    auto_write=False
)

print("Testing RED...")
led.fill((255, 0, 0, 0))
led.show()
time.sleep(2)

print("Testing ORANGE...")
led.fill((255, 165, 0, 0))
led.show()
time.sleep(2)

print("Testing GREEN...")
led.fill((0, 255, 0, 0))
led.show()
time.sleep(2)

print("Turning off...")
led.fill((0, 0, 0, 0))
led.show()