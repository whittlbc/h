import click
import os
from h import log, messages
from h.utils import create_empty_file, entry_filepath_from_tag
from h.utils.entry_opener import open_entry


@click.command()
@click.argument('tag')
@click.option('--file', '-f')
def add(tag, seed_filepath):
  tag = tag.lower()

  # Construct entry file path from tag.
  entry_filepath = entry_filepath_from_tag(tag)

  # Ensure entry doesn't already exist for tag.
  if os.path.exists(entry_filepath):
    log(messages.ENTRY_ALREADY_EXISTS.format(tag))
    return

  # If no seed filepath was provided to create entry from...
  if not seed_filepath:
    # Create empty help entry.
    create_empty_file(entry_filepath)

    # Open an editor, allowing the user to edit the new blank help entry.
    open_entry(path=entry_filepath)
    return

  # A seed file path was provided, so ensure it actually exists.
  if not os.path.exists(seed_filepath):
    log(messages.NO_FILE_AT_PROVIDED_PATH.format(seed_filepath))
    return

  # TODO: copy-paste the seed_filepath to the entry_filepath