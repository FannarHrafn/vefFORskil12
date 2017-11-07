#Fannar Hrafn Haraldsson
#7.11.17
#skilaverkefni 12
import os
from bottle import *

@route('/')
def index():
  return "Bottle forrit í pycharm"

run(host='0.0.0.0', port=os.environ.get('PORT'))