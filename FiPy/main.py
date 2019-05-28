from machine import reset
from FiPyFunctions import FlashingLight, LED_RED, LED_OFF, simple_connect
from GoldenFightFi import GoldenFight
import time
from sys import print_exception

if __name__ == "__main__":
    try:
        FLASHING_LIGHT = FlashingLight(colors=[LED_RED, LED_OFF], ms=250)
        goldenfight = GoldenFight(FLASHING_LIGHT=FLASHING_LIGHT)
        goldenfight.main()
    except Exception as e:
        print("Failed GoldenFight execution")
        print_exception(e)
        time.sleep(5)
        reset()
