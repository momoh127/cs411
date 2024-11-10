from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self, migration_id: int, start_location: Habitat, destination: Habitat, species: str, duration: Optional[int] = None) -> None:
        self.migration_id = migration_id
        self.start_location = start_location
        self.destination = destination
        self.species = species
        self.duration = duration

    def get_migration_path_details(self) -> dict:
        return {
            "migration_id": self.migration_id,
            "start_location": self.start_location.get_habitat_details(),
            "destination": self.destination.get_habitat_details(),
            "species": self.species,
            "duration": self.duration
        }
