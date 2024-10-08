from typing import Any, Optional

class Animal:
    def __init__(self, animal_id: int, name: str, species: str, health_status: Optional[str] = None, age: Optional[int] = None) -> None:
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.health_status = health_status
        self.age = age

    def get_animal_details(self) -> dict[str, Any]:
        return {
            "animal_id": self.animal_id,
            "name": self.name,
            "species": self.species,
            "health_status": self.health_status,
            "age": self.age
        }
    
    def update_animal_details(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

