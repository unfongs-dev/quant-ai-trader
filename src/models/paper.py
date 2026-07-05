from dataclasses import dataclass


@dataclass
class Paper:
    """Research paper model."""

    title: str
    authors: list[str]
    year: int
    abstract: str