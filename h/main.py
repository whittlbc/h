import click
from h.commands import all_cmds, display_global_help
from h.utils.entry_displayer import display_entry


@click.command()
@click.pass_context
@click.argument('sub_cmd', required=False)
def cli(ctx, sub_cmd=None):
  if sub_cmd is None:
    display_global_help()
  elif sub_cmd in all_cmds:
    ctx.invoke(all_cmds[sub_cmd])
  else:
    display_entry(sub_cmd)


if __name__ == '__main__':
  cli()