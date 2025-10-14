from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    GOOGLE_API_KEY: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        if value not in ["dev", "test", "prod"]:
            raise ValueError("ENVIRONMENT must be one of: dev, test, prod")
        return value

    @field_validator("APP_NAME")
    @classmethod
    def validate_app_name(cls, value):
        if not value:
            raise ValueError("APP_NAME must be set")
        return value

    @field_validator("GOOGLE_API_KEY")
    @classmethod
    def validate_google_api_key(cls, value):
        if not value:
            raise ValueError("GOOGLE_API_KEY must be set")
        return value
