"""CyberSentinel application entry point."""

import uvicorn

from app.api import app
from app.utils import setup_logger
from config import settings

logger = setup_logger()


def main() -> None:
    """Launch the CyberSentinel API server."""
    logger.info("Starting %s on %s:%d", settings.app_name, settings.app_host, settings.app_port)
    uvicorn.run(
        "app.api:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )


if __name__ == "__main__":
    main()
