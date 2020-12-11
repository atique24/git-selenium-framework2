import cx_Oracle
import os


def db(username,password,ipaddress,serviceid_or_serviceName):
    os.environ['PATH'] = 'SOME PATH FROM ENVIRONMENT'
    con = cx_Oracle.connect(username,password,ipaddress,serviceid_or_serviceName)
    cur = con.cursor()

    insert_new_record = "insert into TableName values (102,'someStringValue')"                # assuming the table has two coloumns
    update_existing_record = "update TableName set columnName1 = 'SomeValue' where coloumnName2 = 'something'"  # update a particular column
    delete_record = "delete TableName where columnValue= 'Value'"   #delete row
    select_query = "select * from employees"
    select_one_record = "select customerId from customers where city = 'Walla' order by customerID desc"
    cur.execute(select_query)
    for columns in cur:
        print(columns[0], " ", columns[1], " ", columns[2])   # this will extract only 3 coloumns
    print('connected')

    con.close()
    con.commit() # if any update,delete query is run