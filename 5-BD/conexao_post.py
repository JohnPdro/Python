import psycopg2

conn = psycopg2.connect(
    database = 'fliperama',
    user = 'postgres',
    password = '123456',
    host = 'localhost',
    port = '5432'
)