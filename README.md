# 🚀 CodeVector Backend Task

This project provides a **high-performance backend API** built to handle large-scale data (200,000+ records) efficiently. It features cursor-based pagination to ensure consistent performance regardless of database size.

---

## 🛠 Tech Stack
* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
* **Database:** [Supabase](https://supabase.com/) (PostgreSQL)
* **Driver:** `psycopg2`
* **Technique:** Batch-processed data seeding & Keyset Pagination

---

## 🔑 Key Features
* **Optimized Pagination:** Uses **Keyset Pagination (Cursor-based)** instead of standard `OFFSET`.
    * *Performance:* Standard `OFFSET` pagination degrades in speed as you go deeper into the dataset (`O(n)` complexity). Keyset pagination maintains `O(log n)` speed using database indexes.
* **Scalable Seeding:** Includes a batch-processing script to generate 200,000 products efficiently without memory overflow.

---

## 🚀 How to Run

### 1. Prerequisites
Install the required dependencies:
```bash
pip install fastapi uvicorn psycopg2-binary 
2. Seed the Database
Run the script to populate the database with 200,000 records:

Bash
python seed.py
3. Start the API
Launch the server:

Bash
python -m uvicorn main:app --reload

##👤 Author
Helly Lalkiya | Karnavati University
