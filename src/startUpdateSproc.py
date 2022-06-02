import json
from awsSecrets import getDbPass
from mysql.connector import connect, Error

def startUpdateSproc():
    connection = connect(
        host = 'farm.cxqsjcdo8n1w.us-east-1.rds.amazonaws.com',
        user = 'GavSwe',
        password = getDbPass(),
        database = 'NFL'
    )
    
    cursor = connection.cursor();

    print(" ----- Update Stored Procedure Start ----- ")
    
    result = cursor.callproc("A1_WeeklyUpdate")
    print(result)

    
    connection.commit();
    cursor.close();
    connection.close();

    print(" ----- Update Stored Procedure Complete ----- ")
