from pathlib import Path

from src.core.logger import app_logger
from src.services.pdf_service import PDFService
from src.core.config import PAPER_PATH


class ResearchAgent:

    def __init__(self):
        self.pdf_service = PDFService()

    def run(self) -> None:

        app_logger.info("Research Agent Started")

        paper_folder = Path(PAPER_PATH)
        pdf_files = list(paper_folder.glob("*.pdf"))

        app_logger.info(f"Found {len(pdf_files)} PDF files")

        for pdf_file in pdf_files:

            app_logger.info(f"Reading {pdf_file.name}")

            text = self.pdf_service.extract_text(str(pdf_file))

            app_logger.info(
                f"Extracted {len(text):,} characters"
            )

        app_logger.success("Research Agent Finished")