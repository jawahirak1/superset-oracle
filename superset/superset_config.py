SECRET_KEY = 'thisISaSECRET_key'

import sys
import oracledb
try:
    oracledb.init_oracle_client(lib_dir="/opt/oracle/instantclient_latest")
    print("Oracle Thick mode enabled successfully.")
except oracledb.DatabaseError as e:
    print(f"Error enabling Oracle Thick mode: {e}")
    # Handle the error appropriately, perhaps exit if thick mode is critical
    sys.exit(1)
oracledb.version = "8.3.0"
sys.modules["cx_Oracle"] = oracledb
import cx_Oracle
