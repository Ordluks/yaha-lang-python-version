import click
from compose import compose
from read import read
from compiller import compiller


@click.command()
@click.argument('path')
def yaha(path):
  compose(compiller, read)(path)
