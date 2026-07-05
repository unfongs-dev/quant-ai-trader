from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.getenv("MODEL")

PROJECT_NAME = os.getenv("PROJECT_NAME")

DATA_PATH = os.getenv("DATA_PATH")

RESEARCH_PATH = os.getenv("RESEARCH_PATH")

REPORT_PATH = os.getenv("REPORT_PATH")

LOG_PATH = os.getenv("LOG_PATH")

PAPER_PATH = os.getenv("PAPER_PATH")
