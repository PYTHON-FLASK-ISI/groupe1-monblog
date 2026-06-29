import os

from flask.cli import load_dotenv

from app import create_app

load_dotenv()

app = create_app(os.getenv("FLASK_CONFIG","dev"))

if __name__ == "__main__":
    app.run()