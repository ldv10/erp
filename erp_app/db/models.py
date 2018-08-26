from peewee import SqliteDatabase
from playhouse.reflection import Introspector

database = SqliteDatabase(
    'erp.db',
    pragmas=(
        ('cache_size', -1024 * 64), # 64MB page-cache
        ('journal_mode', 'wal'), # Use WAL-mode
        ('foreign_keys', 1) # Enforce foreign-key contraints
    )
)

introspector = Introspector.from_database(database)
models = introspector.generate_models()

print(models)

Cuopon = models.get('cuopon')
User = models.get('user')
Client = models.get('client')

