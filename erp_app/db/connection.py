from peewee import SqliteDatabase
from playhouse.reflection import Introspector

connection = SqliteDatabase(
    'erp.db',
    pragmas=(
        ('cache_size', -1024 * 64), # 64MB page-cache
        ('journal_mode', 'wal'), # Use WAL-mode
        ('foreign_keys', 1) # Enforce foreign-key contraints
    )
)