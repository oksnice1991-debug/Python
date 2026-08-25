from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:040913@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_update_studet():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE student SET level = :new_level "
               "WHERE user_id = :user_id")
    connection.execute(sql, {"new_level": 'Beginner', "user_id": 85426})

    check_sql = text("SELECT * FROM student WHERE user_id = :user_id")
    result = connection.execute(check_sql, {"user_id": 85426})
    rows = result.fetchall()
    assert len(rows) == 1
    assert rows[0][1] == "Beginner"

    transaction.commit()
    connection.close()
