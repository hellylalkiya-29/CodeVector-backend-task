from fastapi import FastAPI
import psycopg2
from typing import Optional

app = FastAPI()
DB_URL = "postgresql://postgres.zwnpwxnusnquwdtyzaee:1INshM278tTXx2ct@aws-1-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require"

def get_db():
    return psycopg2.connect(DB_URL)

@app.get("/products")
async def get_products(limit: int = 20, last_id: Optional[int] = None):
    conn = get_db()
    cur = conn.cursor()
    
    # Keyset Pagination logic
    if last_id:
        query = "SELECT id, name, category, price FROM products WHERE id > %s ORDER BY id ASC LIMIT %s"
        cur.execute(query, (last_id, limit))
    else:
        query = "SELECT id, name, category, price FROM products ORDER BY id ASC LIMIT %s"
        cur.execute(query, (limit,))
        
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {"products": rows}