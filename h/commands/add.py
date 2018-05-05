import click
from h import log


@click.command()
def add():
  log('add')