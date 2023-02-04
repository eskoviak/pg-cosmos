import psycopg2

conn = psycopg2.connect(
    host="c.****.postgres.database.azure.com",
    database="citus",
    user="****",
    password="***",
    port=5432,
    sslmode="require",
    sslrootcert="/Users/edmundlskoviak/.ssh/DigiCertGlobalRootG2.crt.pem"
)

cur = conn.cursor()
print(f"PostgreSQL version: {cur.execute('SELECT version()')}")
