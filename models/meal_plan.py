from dataclasses import dataclass
from datetime import date
from typing import List, Optional
import uuid


@dataclass
class MealPlan:
    user_id: str
    date: date
    recipe_ids: List[str]
    id: Optional[str] = None

    def __post_init__(self):
        if self.id is None:
            self.id = str(uuid.uuid4())
