# TODO: Version 2 - Internet Search
from src.models.paper import Paper


class SearchService:
    """Search research papers."""

    def search(self, keyword: str) -> list[Paper]:

        papers = [
            Paper(
                title="Adaptive Momentum Strategy",
                authors=["John Doe"],
                year=2024,
                abstract="Example abstract...",
            )
        ]

        return papers