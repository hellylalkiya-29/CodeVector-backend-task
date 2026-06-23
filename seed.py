import psycopg2

# Supabase Pooler URL
DB_URL = "postgresql://postgres.zwnpwxnusnquwdtyzaee:1INshM278tTXx2ct@aws-1-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require"

def seed_db():
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        print("Connected! Starting to seed 200,000 records...")

        # Table create karna
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name TEXT,
                category TEXT,
                price FLOAT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        cur.execute("TRUNCATE TABLE products;") # Table saaf karo
        
        batch_size = 10000
        for i in range(0, 200000, batch_size):
            data = [
                (f"Product {j}", "Electronics", 100.0 + j) 
                for j in range(i + 1, i + batch_size + 1)
            ]
            cur.executemany("INSERT INTO products (name, category, price) VALUES (%s, %s, %s)", data)
            conn.commit() 
            print(f"Inserted {i + batch_size} records...")

        cur.close()
        conn.close()
        print("Successfully seeded 200,000 records!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    seed_db()