# /usr/bin/env python

#!/usr/bin/env python
# init_py_dont_write_bytecode

#init_boilerplate

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.project import *
from fabric.colors import *


from time import sleep

CWD = os.path.dirname(__file__)

def threaded_local(command):
    local(command, capture=True)


def nodemcu_command(parameters):
    with lcd(CWD):
        local('nodemcu-tool.js %s' % (' '.join(parameters)))

def mkfs():
    nodemcu_command(['mkfs --noninteractive'])

def reset():
    nodemcu_command(['reset'])

def upload(lua_file):
    nodemcu_command(['upload %s' % lua_file ])

def run(lua_file):
    nodemcu_command(['run %s' % lua_file ])


def fresh_upload(lua_file):
    # mkfs()
    reset()
    sleep(3)
    run(lua_file)
    print(green('DONE!!'))
