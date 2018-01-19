import click

from commands import initcd
from commands import playcd
from commands import pausecd
from utils import Player


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    Player.__init__()
    if ctx.invoked_subcommand is None:
        click.echo('Welcome to ply!')


@cli.command()
def init():
    initcd.run()


@cli.command()
def pause():
    pausecd.run()


@cli.command()
@click.option('-s')
def play(s):
    if s == "":
        click.echo("Invalid song")
    else:
        playcd.run(song=s)
