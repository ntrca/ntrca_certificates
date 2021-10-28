# Connect Postgresql database in Python
import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(
        host="localhost",
        database="ntrca_db",
        password="Atpl123#",
        user="ntrca"
    )

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    cursor.execute("SELECT * FROM ntrca_app_ntrcaresult")
    all_data = cursor.fetchall()
    d = 0
    roll_no_list = []
    for data in all_data:
        primary_key=data[0]
        s_number = data[1]
        total_number = data[2]
        v_number =  data[3]
        board = data[4]
        dob = data[5]
        father = data[6]
        h_exam = data[7]
        h_result = data[8]
        h_result_text = data[9]
        interview_date = data[10]
        invoice = data[11]
        mother = data[12]
        name = data[13]
        s_exam = data[14]
        s_result = data[15]
        s_result_text = data[16]
        subject_code = data[17]
        comment = data[18]
        roll = data[19]
        try:
            total = float(total_number)
        except Exception as e:
            total = 0
        if roll == None:
            roll = "null"
        if s_number == None:
            s_number = "null"
        if total_number == None:
            total_number = "null"
        if board == None:
            board = "null"
        if dob == None:
            dob = "null"
        if h_exam == None:
            h_exam = "null"
        if h_result == None:
            h_result = "null"
        if h_result_text == None:
            h_result_text = "null"
        if interview_date == None:
            interview_date = "null"
        if invoice == None:
            invoice = "null"
        if name == None:
            name = "null"
        if s_exam == None:
            s_exam = "null"
        if mother == None:
            mother = "null"
        if s_result == None:
            s_result = "null"
        if s_result_text == None:
            s_result_text = "null"
        if subject_code == None:
            subject_code = "null"
        if comment == None:
            comment = "null"
        if father == None:
            father = "null"
        if v_number == None:
            v_number = "null"
        if roll == None:
            roll = "null"
        if roll not in roll_no_list:
            if roll:
                roll_no_list.append(roll)
                cursor.execute(
                    "CREATE TABLE ntrca_result(id INT PRIMARY KEY NOT NULL, roll TEXT NOT NULL, s_number integer);"
                )
                connection.commit()
            else:
                print(f"Invalid or Absence Candidate {roll}")
        else:
            print("Duplicate Roll No. = ", roll)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")