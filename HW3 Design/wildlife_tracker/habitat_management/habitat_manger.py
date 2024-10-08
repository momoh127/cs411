from typing import Optional, List, Any
from wildlife_tracker.habitat_management.habitat import Habitat

class HabitatManager:
    def __init__(self) -> None:
        self.habitats: dict[int, Habitat] = {}

    def add_habitat(self, habitat: Habitat) -> None:
        self.habitats[habitat.habitat_id] = habitat

    def remove_habitat(self, habitat_id: int) -> None:
        if habitat_id in self.habitats:
            del self.habitats[habitat_id]

    def get_habitat_by_id(self, habitat_id: int) -> Optional[Habitat]:
        return self.habitats.get(habitat_id)

    def update_habitat_details(self, habitat_id: int, **kwargs: dict[str, Any]) -> None:
        habitat = self.get_habitat_by_id(habitat_id)
        if habitat:
            habitat.update_habitat_details(**kwargs)
