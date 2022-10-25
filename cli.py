import click


@click.command()
@click.argument('path')
def yaha(path):
  print(path)
