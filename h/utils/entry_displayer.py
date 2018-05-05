import os
from h import log, messages
from h.utils import entry_filepath_from_tag


def display_entry(tag):
  tag = tag.lower()

  # Construct entry file path from tag.
  entry_filepath = entry_filepath_from_tag(tag)

  # Return if no entry exists for tag.
  if not os.path.exists(entry_filepath):
    log(messages.NO_ENTRY.format(tag))
    return

  # Get entry contents.
  with open(entry_filepath) as f:
    entry_contents = f.read()

  # Display entry contents.
  log(entry_contents)