import pandas as pd
from src.school import Category


class ResourceOptimizer:
    """Loads category data and partitions categories by classroom-crowding status."""

    def __init__(self, csv_filepath: str):
        self.csv_filepath = csv_filepath
        self.categories = []

    def load_categories(self):
        df = pd.read_csv(self.csv_filepath)
        self.categories = []

        for _, row in df.iterrows():
            category = Category(
                category_id=str(row.get("category_id", "")),
                level=str(row.get("level", "")),
                sector=str(row.get("sector", "")),
                students=int(row.get("students", 0)),
                classes=int(row.get("classes", 0)),
                rooms=int(row.get("rooms", 0)),
                establishments=int(row.get("establishments", 0)) if not pd.isna(row.get("establishments")) else 0,
            )
            self.categories.append(category)

        return self.categories

    def partition_categories(self):
        overcrowded = []
        light_load = []

        for category in self.categories:
            status = category.get_status()
            if status == "Overcrowded":
                overcrowded.append(category)
            elif status == "Light Load":
                light_load.append(category)

        return overcrowded, light_load
