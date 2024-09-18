import pymysql

endpoint = "rds-primerentrega.cvq0gu80k5jn.us-east-1.rds.amazonaws.com"
userdb = 'admin'
passworddb = 'basededatos123' 

def connect2SQL():

    try:
        pymysql.connect(

            host = endpoint,
            user = userdb,
            password = passworddb
        )

        print("Connection was successful")

    except Exception as err:
        print("error:", err)

connect2SQL()