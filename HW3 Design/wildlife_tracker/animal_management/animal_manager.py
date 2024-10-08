from typing import Optional, Any
from wildlife_tracker.animal_management.animal import Animal

class AnimalManager:
    def __init__(self) -> None:
        self.animals: dict[int, Animal] = {}

    def register_animal(self, animal: Animal) -> None:
        self.animals[animal.animal_id] = animal

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        return self.animals.get(animal_id)

    def remove_animal(self, animal_id: int) -> None:
        if animal_id in self.animals:
            del self.animals[animal_id]

    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        animal = self.get_animal_by_id(animal_id)
        if animal:
            animal.update_animal_details(**kwargs)
