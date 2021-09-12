from dbConnector import connectDB,queryValidationError,queryChecker

def create(conn,curr,query):
    try:
        if isinstance(query,list):
            for sqlQuery in query:
                if (queryChecker('Create',sqlQuery)):
                   curr.execute(sqlQuery)
                else:
                    raise queryValidationError('Invalid Create query')
        elif isinstance(query,str):
            if (queryChecker('Create', query)):
                curr.execute(query)
            else:
                raise queryValidationError('Invalid Create query')
        conn.commit()
    except (Exception,queryValidationError) as e:
        print(e)
        conn.rollback()
def insert(conn,curr,query=[]):
    try:
        if isinstance(query,list):
            for sqlQuery in query:
                if queryChecker('Insert',sqlQuery):
                    curr.execute(sqlQuery)
                else:
                    raise queryValidationError('Invalid Insert query')
        elif isinstance(query,str):
            if queryChecker('Insert',query):
                curr.execute(query)
            else:
                raise queryValidationError('Invalid Insert query')
            conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)

def readOne(curr,query):
    res = None
    if isinstance(query, str):
        try:
            curr.execute(query)
            res = curr.fetchone()
        except Exception as e:
            print(e)
        else:
            return res
    else:
        raise queryValidationError('Please provide one select query at a time, as string')
def readAll(curr,query):
    res = None
    if isinstance(query,str):
        try:
            curr.execute(query)
            res = curr.fetchall()
        except Exception as e:
            print(e)
        else:
            return res
    else:
        raise queryValidationError('Please provide one select query at a time, as string')
def update(conn,curr,query=[]):
    if isinstance(query, str):
        try:
            if queryChecker('Update',query):
                curr.execute(query)
            else:
                raise queryValidationError('Invalid Update query')
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
    else:
        raise queryValidationError('Please provide update query as string in input')

def delete(conn,curr,query):
    try:
        if isinstance(query,list):
            for sqlQuery in query:
                if queryChecker('Delete',sqlQuery):
                    curr.execute(query)
                else:
                    raise queryValidationError('Invalid Delete query')
        elif isinstance(query,str):
            if queryChecker('Delete',query):
                curr.execute(query)
            else:
                raise queryValidationError('Invalid Delete query')
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
def drop(conn,curr,query):
    try:
        if isinstance(query,list):
            for sqlQuery in query:
                if queryChecker('Drop',sqlQuery):
                    curr.execute(sqlQuery)
                else:
                    raise queryValidationError('Invalid Drop query')
        elif isinstance(query,str):
            if queryChecker('Drop'.query):
                curr.execute(query)
            else:
                raise queryValidationError('Invalid Drop query')
        conn.commit()
    except (Exception, queryValidationError) as e:
        print(e)
        conn.rollback()


if __name__ == '__main__':
    with connectDB('test_DB.db') as connObj:
        res = None
        try:
            drop(connObj.conn,connObj.curr,['drop table if exists test_table'])
            create(connObj.conn,connObj.curr,'create table test_table(item_id varchar(30))')
            insert(connObj.conn,connObj.curr,['insert into test_table values(101)','insert into test_table values(102)'])
            update(connObj.conn,connObj.curr,'update test_table set item_id = 103 where item_id = 102')
            res = readAll(connObj.curr,'select * from test_table')
        except Exception as e:
            print(e)
        else:
            for i in res:
                print(i)