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

ESPTOOL_PY_FILE= '/home/logic/_workspace/nodemcu_tryout/esptool-py/esptool.py'

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
    print(yellow('sleep before upload ... '))
    sleep(1)
    upload(lua_file)
    run(lua_file)
    print(green('DONE!!'))


def esptool_command(parameters, nodemcu_port="/dev/ttyUSB0"):
    command_format="%s --port %s %s" % (ESPTOOL_PY_FILE, nodemcu_port, ' '.join(parameters))
    with lcd(CWD):
        local(command_format)

def esptool_write_flash(firmware_file, flash_mode="dio"):
    esptool_command(['write_flash', '-fm %s' % flash_mode, '0x00000', firmware_file])

def update_firmware(firmware_file):
    esptool_write_flash(firmware_file)
