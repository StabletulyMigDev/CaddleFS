# Typer Docs https://typer.tiangolo.com/tutorial/
# CaddleFS docs https://caddlefs.miglab.me/docs/

import App
import typer
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def web(name: Annotated[str, typer.Argument(help="Start Web gui", metavar="Web Gui")]):
    print('Hello, World');

if __name__ == "__main__":
   app()