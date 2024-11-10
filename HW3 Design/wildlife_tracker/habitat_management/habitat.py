from typing import Optional, List, Any
from wildlife_tracker.animal_management.animal import Animal

class Habitat:
    def __init__(self, habitat_id: int, geographic_area: str, size: int, environment_type: str, animals: Optional[List[int]] = None) -> None:
        self.habitat_id = habitat_id
        self.geographic_area = geographic_area
        self.size = size
        self.environment_type = environment_type
        self.animals = animals or []

    def get_habitat_details(self) -> dict:
        return {
            "habitat_id": self.habitat_id,
            "geographic_area": self.geographic_area,
            "size": self.size,
            "environment_type": self.environment_type,
            "animals": self.animals
        }

    def assign_animals_to_habitat(self, animals: List[Animal]) -> None:
        for animal in animals:
            if animal.animal_id not in self.animals:
                self.animals.append(animal.animal_id)

    def update_habitat_details(self, **kwargs: dict[str, Any]) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
