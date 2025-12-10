from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = ""
    DEBUG: bool = True

    API_HOST: str = "https://nonvisibly-untemporal-lawerence.ngrok-free.dev"
    API_PREFIX: str = "/api"
    API_V1_STR: str = "/v1"
    API_PORT: int = 8000

    BOT_TOKEN: str
    ADMIN_ID: int = 0
    USERS: dict = {}
    SET_WEBHOOK: bool = True
    WEBHOOK_STR: str = "/webhook"

    BOT_REDIS_DSN: str = "redis://localhost:6379/0"

    @property
    def WEBHOOK_URL(self) -> str:
        return f"{self.API_HOST}{self.API_PREFIX}{self.WEBHOOK_STR}"

    BOT_LOCALES: list = ["en", "uz"]
    DEFAULT_LOCALE: str = "en"
    BAD_WORDS: list = ["word1", "word2", "word3"]

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
