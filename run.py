import uvicorn

from src.app import App
from src.core.config import Config, Mode

# TODO: ArgParser for Mode
config = Config(Mode.DEV)
app = App(config)

if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host=config.app.host,
        port=config.app.port,
        reload=True,
    )
