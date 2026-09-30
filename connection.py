import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()


async def get_connection():
    try:
        conn = await asyncpg.connect(
            host="localhost",
            user="postgres",
            database="job_db",
            password=os.getenv("DB_PASSWORD"),
            port=5432
        )
        return conn
    except Exception as error:
        print("connection error:", error)


async def create_table():
    conn = await get_connection()

    try:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(100),
                full_name VARCHAR(100),
                telegram_id VARCHAR,
                created_at TIMESTAMP DEFAULT NOW(),
                is_active BOOLEAN DEFAULT TRUE
            );
            CREATE TABLE IF NOT EXISTS categories(
                category_id SERIAL PRIMARY KEY,
                category_name varchar(100)
            );

            CREATE TABLE IF NOT EXISTS jobs (
                job_id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT,
                salary INT DEFAULT 0,
                category_id int REFERENCES categories(category_id)
            );

            CREATE TABLE IF NOT EXISTS applications (
                application_id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(user_id),
                job_id INT REFERENCES jobs(job_id),
                created_at TIMESTAMP DEFAULT NOW()
            );
        """)
    except Exception as error:
        print("connection error:", error)

    finally:
        await conn.close()
        print("Table created!")