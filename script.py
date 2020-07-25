import math
from os import rename
import sys

import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello {}".format(who_to_greet)
    return greeting


print(greet("Mukhtar Mohamoud"))

r = requests.get("https://newny.io")
print(r.status_code)
