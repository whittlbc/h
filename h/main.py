import click
from h.commands import all_cmds, display_global_help
from h.utils.help_displayer import display_help_entry

# Allow '-h' to be an alias of '--help'
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command()
@click.pass_context
@click.argument('subcmd', required=False)
def cli(ctx, subcmd=None):
  if subcmd is None:
    display_global_help()
  elif subcmd in all_cmds:
    ctx.invoke(all_cmds[subcmd])
  else:
    display_help_entry(tag=subcmd)


if __name__ == '__main__':
  cli()