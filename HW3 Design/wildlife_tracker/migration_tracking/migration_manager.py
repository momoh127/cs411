from typing import Any, Optional, List
from wildlife_tracker.migration_tracking.migration_path import MigrationPath
from wildlife_tracker.migration_tracking.migration import Migration

class MigrationManager:
    def __init__(self) -> None:
        self.migrations: dict[int, Migration] = {}

    def add_migration(self, migration: Migration) -> None:
        self.migrations[migration.migration_id] = migration

    def remove_migration(self, migration_id: int) -> None:
        if migration_id in self.migrations:
            del self.migrations[migration_id]

    def get_migration_by_id(self, migration_id: int) -> Optional[Migration]:
        return self.migrations.get(migration_id)

    def update_migration_details(self, migration_id: int, **kwargs: Any) -> None:
        migration = self.get_migration_by_id(migration_id)
        if migration:
            migration.update_migration_details(**kwargs)

