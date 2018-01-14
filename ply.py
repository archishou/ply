import click

from commands import initcd


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('I was invoked without subcommand')
    if ctx.invoked_subcommand is initcd:
        click.echo('I am about to invoke init')


@cli.command()
def init():
    initcd.run()
