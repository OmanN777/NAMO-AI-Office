import sqlite3
import argparse
import os
import json
from datetime import datetime

# Define database path relative to this script
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, "memory_bank.db")

def get_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the SQLite database with the necessary tables."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            key TEXT NOT NULL,
            value TEXT NOT NULL,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(category, key)
        )
    ''')
    conn.commit()
    conn.close()

def save_memory(category, key, value):
    """Save or update a memory in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Memories (category, key, value, updated_at)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(category, key) DO UPDATE SET 
            value=excluded.value,
            updated_at=CURRENT_TIMESTAMP
    ''', (category, key, value))
    conn.commit()
    conn.close()
    return True

def get_memory(category, key):
    """Retrieve a specific memory by category and key."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT value FROM Memories WHERE category = ? AND key = ?', (category, key))
    row = cursor.fetchone()
    conn.close()
    return row['value'] if row else None

def search_memory(keyword):
    """Search for memories containing the keyword in category, key, or value."""
    conn = get_connection()
    cursor = conn.cursor()
    search_term = f"%{keyword}%"
    cursor.execute('''
        SELECT category, key, value, updated_at 
        FROM Memories 
        WHERE category LIKE ? OR key LIKE ? OR value LIKE ?
        ORDER BY updated_at DESC
    ''', (search_term, search_term, search_term))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def list_all():
    """List all stored memories."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT category, key, value, updated_at FROM Memories ORDER BY category, key')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def delete_memory(category, key):
    """Delete a memory."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Memories WHERE category = ? AND key = ?', (category, key))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted

if __name__ == "__main__":
    init_db()
    parser = argparse.ArgumentParser(description="Malli's SQLite Memory Bank Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # save command
    parser_save = subparsers.add_parser("save", help="Save a memory")
    parser_save.add_argument("category", help="Category (e.g., Rules, UserProfile, Config)")
    parser_save.add_argument("key", help="Key name")
    parser_save.add_argument("value", help="The memory content to store")

    # get command
    parser_get = subparsers.add_parser("get", help="Get a specific memory")
    parser_get.add_argument("category", help="Category")
    parser_get.add_argument("key", help="Key name")

    # search command
    parser_search = subparsers.add_parser("search", help="Search across memories")
    parser_search.add_argument("keyword", help="Keyword to search for")

    # list command
    parser_list = subparsers.add_parser("list", help="List all memories")

    # delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a memory")
    parser_delete.add_argument("category", help="Category")
    parser_delete.add_argument("key", help="Key name")

    args = parser.parse_args()

    if args.command == "save":
        save_memory(args.category, args.key, args.value)
        print(f"Memory saved: [{args.category}] {args.key}")
    elif args.command == "get":
        val = get_memory(args.category, args.key)
        if val:
            print(val)
        else:
            print(f"No memory found for [{args.category}] {args.key}")
    elif args.command == "search":
        results = search_memory(args.keyword)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    elif args.command == "list":
        results = list_all()
        print(json.dumps(results, indent=2, ensure_ascii=False))
    elif args.command == "delete":
        success = delete_memory(args.category, args.key)
        if success:
            print(f"Deleted: [{args.category}] {args.key}")
        else:
            print(f"Not found: [{args.category}] {args.key}")
    else:
        parser.print_help()
