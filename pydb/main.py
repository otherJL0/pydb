import typer

app = typer.Typer()


@app.command()
def pydb():
    print("pydb")
