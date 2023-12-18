import click 


@click.command()
def greet():
    click.echo("Hello world")

@click.command
def add():
    a = int(input())
    b = int(input())
    click.echo(a+b)
greet()
add()