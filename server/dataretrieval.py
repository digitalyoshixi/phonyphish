from databricks import sql
import os
import logging
from dotenv import load_dotenv
load_dotenv()

logging.getLogger("databricks.sql").setLevel(logging.DEBUG)
logging.basicConfig(filename = "results.log",
                   level    = logging.DEBUG)


connection = sql.connect(
                       server_hostname = "dbc-2fb01cd0-7bda.cloud.databricks.com",
                       http_path = "/sql/1.0/warehouses/fea7e42c01f5782d",
                       access_token = os.getenv("POSTDATABRICKS"))


cursor = connection.cursor()

cursor.execute("SELECT * from range(10)")
result = cursor.fetchall()


def update_cursor(phone_number, is_scam):
    try:
        cursor.execute(
            "UPDATE your_table_name SET is_scam = ? WHERE phone_number = ?",
            (is_scam, phone_number)
        )
        connection.commit()
        logging.debug(f"Updated phone number {phone_number} with is_scam = {is_scam}")
    except Exception as e:
        logging.error(f"Error updating phone number {phone_number}: {e}")

update_cursor("1234567890", True)
breakpoint()

def read_cursor():
    try:
        cursor.execute("SELECT * FROM your_table_name")
        result = cursor.fetchall()
        logging.debug(f"Read {len(result)} rows")
        return result
    except Exception as e:
        logging.error(f"Error reading table: {e}")
        return []
    
def delete_cursor(phone_number):
    try:
        cursor.execute(
            "DELETE FROM your_table_name WHERE phone_number = ?",
            (phone_number,)
        )
        connection.commit()
        logging.debug(f"Deleted phone number {phone_number}")
    except Exception as e:
        logging.error(f"Error deleting phone number {phone_number}: {e}")
  

for row in result:
  logging.debug(row)

cursor.close()
connection.close()
