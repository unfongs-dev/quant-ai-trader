import typer

from src.core.logger import app_logger
from src.core.config import PROJECT_NAME, MODEL
from src.agents.research_agent import ResearchAgent

app = typer.Typer()

@app.command()
def start():
    """Start Quant AI Trader"""

    app_logger.info("=" * 50)
    app_logger.info(f"Project : {PROJECT_NAME}")
    app_logger.info(f"Model   : {MODEL}")
    app_logger.info("=" * 50)

    app_logger.success("Configuration Loaded")
    app_logger.success("Application Started")


@app.command()
def research():
    """Run Research Agent"""

    research_agent = ResearchAgent()
    research_agent.run()