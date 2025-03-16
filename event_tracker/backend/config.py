def data_config():
    user = input("Enter username: ")
    password = input("Enter password: ")
    database = input("Enter database name: ")
    DATABASE_CONFIG = {
        'host' : 'localhost',
        'user' : user,
        'password' : password,
        'database' :database
    }
    return DATABASE_CONFIG

DATABASE_CONFIG = data_config()