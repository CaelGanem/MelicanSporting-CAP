import os
import json
import keep_alive
import requests
from urllib.request import urlopen
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

keep_alive.keep_alive()