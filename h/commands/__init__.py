from .add import add
from h import log

all_cmds = {
  'add': add
}


def display_global_help():
  log('Global help')