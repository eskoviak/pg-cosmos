from sqlalchemy import (create_engine, text, URL)
from sqlalchemy.orm import Session

pg_uri = URL.create(
    "postgresql+psycopg2",
    username="citus",
    password="P0stM3##",
    host="c.sophocles.postgres.database.azure.com",
    port=5432,
    database="citus",
    query={"sslmode": "require", "sslrootcert":"/Users/edmundlskoviak/.ssh/DigiCertGlobalRootG2.crt.pem"}
)

engine = create_engine(pg_uri)

stmt = '''SELECT *
FROM activity.test;
'''

with engine.connect() as conn:
    result = conn.execute(text(stmt))
    for row in result:
        print(row) #type: ignore





