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

def insert_cursor(phone_number, is_scam, transcription):
    try:
        cursor.execute(
            f"INSERT INTO phone_scam_list (is_scam, phone_number, transcription) VALUES ({is_scam},{phone_number}, '{transcription}')",
        )
        connection.commit()
        logging.debug(f"Updated phone number {phone_number} with is_scam = {is_scam}")
    except Exception as e:
        logging.error(f"Error updating phone number {phone_number}: {e}")

def update_cursor(phone_number, is_scam):
    try:
        cursor.execute(
            f"UPDATE phone_scam_list SET is_scam = {is_scam}, phone_number = {phone_number}",
        )
        connection.commit()
        logging.debug(f"Updated phone number {phone_number} with is_scam = {is_scam}")
    except Exception as e:
        logging.error(f"Error updating phone number {phone_number}: {e}")

def read_cursor():
    try:
        cursor.execute("SELECT * FROM phone_scam_list")
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
 
