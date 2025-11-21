import os
from pathlib import Path
from dotenv import load_dotenv


class Config:
    def __init__(self, env_file: str = None):
        self.env_file = env_file or Path(__file__).resolve().parents[2] / ".env"

        if isinstance(self.env_file, str):
            self.env_file = Path(self.env_file)

        # load environment variables from .env file
        if self.env_file.exists():
            load_dotenv(self.env_file, override=True)

        # read environment variables
        self.TYPHOON_API_KEY = os.getenv("TYPHOON_API_KEY")
        self.TYPHOON_ENDPOINT = os.getenv("TYPHOON_ENDPOINT")

        # validate that all required environment variables are set
        self.validate()

    def validate(self):
        required_vars = [
            "TYPHOON_ENDPOINT",
            "TYPHOON_API_KEY",
        ]
        missing_vars = [
            var
            for var in required_vars
            if not getattr(self, var)
        ]

        if missing_vars:
            raise ValueError(f"The following environment variables are missing: {', '.join(missing_vars)}")


config = Config()
