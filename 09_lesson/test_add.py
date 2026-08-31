from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:040913@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_add_subject():
    connection = db.connect()
    transaction = connection.begin()

    test_code = "9999"
    sql = text("INSERT INTO subject (subject_title) VALUES (:code)")
    connection.execute(sql, {"code": test_code})

    check_sql = text("SELECT * FROM subject WHERE subject_title = :code")
    result = connection.execute(check_sql, {"code": test_code})
    rows = result.fetchall()

    assert len(rows) == 1

    delete_sql = text("DELETE FROM subject WHERE subject_title = :code")
    connection.execute(delete_sql, {"code": test_code})

    transaction.commit()
    connection.close()
