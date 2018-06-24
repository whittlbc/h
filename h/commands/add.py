import click
import os
import shutil
from h import log, messages
from h.utils import create_empty_file, entry_filepath_from_tag, upsert_entries_dir
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

  # Upsert entries directory.
  upsert_entries_dir()

  # If no seed filepath was provided to create entry from...
  if not seed_filepath:
    # Create empty help entry.
    create_empty_file(entry_filepath)

    # Open an editor, allowing the user to edit the new blank help entry.
    open_entry(path=entry_filepath)

    log(messages.ADD_SUCCESS_NO_SEED_FILE.format(tag))
    return

  # A seed file path was provided, so ensure it actually exists.
  if not os.path.exists(seed_filepath):
    log(messages.NO_FILE_AT_PROVIDED_PATH.format(seed_filepath))
    return

  # Copy-paste the seed file into the entry filepath
  shutil.copy(seed_filepath, entry_filepath)

  log(messages.ADD_SUCCESS_WITH_SEED_FILE.format(tag, seed_filepath))