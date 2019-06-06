import pycom
from time import sleep
import ucrypto as crypto
import machine
import os
from ubinascii import hexlify
from network import LTE
from WiPyFunctions import *


def connect_lte(timeout=30):
    lte = LTE()         # instantiate the LTE object
    lte.deinit()
    lte.init()

    lte.attach()        # attach the cellular modem to a base station
    cycles = 0
    while not lte.isattached():
        sleep(1)
        cycles += 1
        if cycles > timeout:
            raise Exception("Failed to attach cellular modem to base station")

    lte.connect()       # start a data session and obtain an IP address
    cycles = 0
    while not lte.isconnected():
        sleep(1)
        cycles += 1
        if cycles > timeout:
            raise Exception("Failed to obtain cellular data session")

    return lte

