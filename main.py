import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml
import os


def export_envs(environment: str = "dev") -> None:
    load_dotenv(f"config/.env.{environment}")


def export_secrets(secrets_file: str = "secrets.yaml") -> None:
    with open(secrets_file, "r") as file:
        data = yaml.safe_load(file)

    for key, value in data.items():
        os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("GOOGLE_API_KEY: ", settings.GOOGLE_API_KEY)
