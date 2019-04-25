def submit_query(query, conn):
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()