from typing import Any, Optional, List
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:
    def __init__(self, migration_id: int, paths: List[MigrationPath], status: str = "Scheduled") -> None:
        self.migration_id = migration_id
        self.paths = paths
        self.status = status

    def get_migration_details(self) -> dict:
        return {
            "migration_id": self.migration_id,
            "paths": [path.get_migration_path_details() for path in self.paths],
            "status": self.status
        }

    def update_migration_details(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
