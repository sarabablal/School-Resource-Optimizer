class Category:
    """Represents one education category: a level (Primaire/Collegial/Qualifiant)
    crossed with a sector (Public/Prive), based on national aggregated stats."""

    def __init__(
        self,
        category_id: str,
        level: str,
        sector: str,
        students: int,
        classes: int,
        rooms: int,
        establishments: int = 0,
    ):
        self.category_id = category_id
        self.level = level
        self.sector = sector
        self.students = students
        self.classes = classes
        self.rooms = rooms
        self.establishments = establishments

    # how many students per classroom, on average, in this category
    def get_students_per_room(self):
        if self.rooms == 0:
            return 0.0
        return self.students / self.rooms

    # flag the category based on how crowded its classrooms are
    def get_status(self, overcrowded_threshold: float = 38.0, light_threshold: float = 25.0):
        ratio = self.get_students_per_room()

        if ratio > overcrowded_threshold:
            return "Overcrowded"
        elif ratio < light_threshold:
            return "Light Load"
        else:
            return "Balanced"
