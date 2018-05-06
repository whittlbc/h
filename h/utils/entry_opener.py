from h.utils import entry_filepath_from_tag
from savvy.shell import shell


def open_entry(tag=None, path=None):
  if not path:
    path = entry_filepath_from_tag(tag)

  # Open entry file with vi
  shell.exec(('vi', path))