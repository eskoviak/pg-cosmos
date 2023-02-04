import psycopg2

conn = psycopg2.connect(
    host="c.sophocles.postgres.database.azure.com",
    database="citus",
    user="citus",
    password="P0stM3##",
    port=5432,
    sslmode="require",
    sslrootcert="/Users/edmundlskoviak/.ssh/DigiCertGlobalRootG2.crt.pem"
)

cur = conn.cursor()
print(f"PostgreSQL version: {cur.execute('SELECT version()')}")