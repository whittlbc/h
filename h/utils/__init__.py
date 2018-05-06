import os
from h.definitions import *


def entry_filepath_from_tag(tag):
  return os.path.join(ENTRIES_DIR, '.'.join((tag.lower(), ENTRIES_EXT)))


def create_empty_file(path):
  open(path, 'a').close()