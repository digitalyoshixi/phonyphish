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


a = cursor.execute("SELECT * from range(10)")
breakpoint()

result = cursor.fetchall()

for row in result:
  logging.debug(row)

cursor.close()
connection.close()
