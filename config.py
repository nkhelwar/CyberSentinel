"""Application configuration loaded from environment variables."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """CyberSentinel runtime settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    app_name: str = "CyberSentinel"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    debug: bool = False
    log_level: str = "INFO"

    nvd_api_base_url: str = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    nvd_api_key: str = ""
    nvd_request_timeout: int = 30
    nvd_results_limit: int = 10

    reports_dir: str = "reports"

    @property
    def reports_path(self) -> Path:
        """Return the reports directory as a resolved Path."""
        return Path(self.reports_dir).resolve()


settings = Settings()
