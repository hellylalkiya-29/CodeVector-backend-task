# CodeVector Backend Task

Backend API for browsing 200,000 products with high performance.

## Tech Stack
- **Framework:** FastAPI
- **Database:** Supabase (PostgreSQL)
- **Pagination:** Keyset Pagination (Cursor-based)

## Why Keyset Pagination?
I chose Keyset Pagination over Offset Pagination because `OFFSET` performs poorly on large datasets (`O(n)` complexity). By using `created_at` and `id` as cursors, the query performance remains consistent (`O(log n)`) regardless of the dataset size.

## How to run
1. Clone the repo.
2. Install requirements: `pip install fastapi uvicorn psycopg2-binary`
3. Run seed script: `python seed.py`
4. Run server: `uvicorn main:app --reload`
