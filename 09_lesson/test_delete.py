from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:040913@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    user_id = 44133
    check_before = text("SELECT * FROM student WHERE user_id = :user_id")
    result_before = connection.execute(check_before, {"user_id": 44133})
    rows_before = result_before.fetchall()
    assert len(rows_before) == 1

    sql = text("DELETE FROM student WHERE user_id = :id")
    connection.execute(sql, {"id": 44133})

    result_after = connection.execute(check_before, {"user_id": user_id})
    rows_after = result_after.fetchall()
    assert len(rows_after) == 0

    transaction.commit()
    connection.close()


def test_delete_2():
    connection = db.connect()
    transaction = connection.begin()

    insert_sql = text(
        "INSERT INTO student (user_id, "
        "level, education_form, subject_id) "
        "VALUES (:user_id, :level, :education_form, :subject_id)")
    connection.execute(insert_sql, {
        "user_id": 8888,
        "level": "Advanced",
        "education_form": "group",
        "subject_id": 1
    })
    check_sql = text("SELECT * FROM student WHERE user_id = :user_id")
    result = connection.execute(check_sql, {"user_id": 8888})
    rows = result.fetchall()
    assert len(rows) == 1

    sql_delete = text("DELETE FROM student WHERE user_id = :id")
    connection.execute(sql_delete, {"id": 8888})

    result_after = connection.execute(check_sql, {"user_id": 8888})
    assert len(result_after.fetchall()) == 0

    transaction.commit()
    connection.close()
