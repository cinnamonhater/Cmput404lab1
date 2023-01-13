import requests
from os import getcwd

url = "https://raw.githubusercontent.com/cinnamonhater/Cmput404lab1/main/scripts.py"
directory = getcwd()
filename = directory + 'scripts.py'
r = requests.get(url)

f = open(filename, 'r')
print(f)
