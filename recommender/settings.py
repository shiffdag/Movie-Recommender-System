from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    root_dir: Path = Path(__file__).parents[1]
    data_dir: Path = root_dir / "data"


settings = Settings()
