import src.data_service.data_table_adaptor as dta
import json
import src.data_service.RDBDataTable as rdb

def t2():
    d= dta.get_databases()
    print("t2 result =", json.dumps(d, indent=2))


def t3():
    connect_info = {
        "host" : "127.0.0.1:3306",
        "user": "dbuser",
        "password": "lichiqu123"
    }
    db = rdb.RDBDataTable("People","lahman2019clean", connect_info = connect_info)
    d = db.get_row_count()
    print(f"t3 result ={d}")

def t4():
    connect_info = {
        "host" : "127.0.0.1:3306",
        "user": "dbuser",
        "password": "lichiqu123"
    }
    db = rdb.RDBDataTable("appearances", "lahman2019clean", connect_info=connect_info)
    db.get_primary_key_columns()

def t5():
    connect_info = {
        "host" : "127.0.0.1:3306",
        "user": "dbuser",
        "password": "lichiqu123"
    }

    d = dta.get_tables("lahman2019clean")
    print("t5 result =", json.dumps(d, indent=2))
