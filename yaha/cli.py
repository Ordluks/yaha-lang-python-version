import click
from compose import compose
from read import read
from compiller import compiller


__compile_file = compose(compiller, read)

@click.command()
@click.argument('path')
def yaha(path):
  __compile_file(path)
