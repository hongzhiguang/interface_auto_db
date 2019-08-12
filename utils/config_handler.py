from configparser import ConfigParser
from conf.ProjVar import config_filePath

class ConfigParse(object):

    def __init__(self):
        pass

    @classmethod
    def get_db_conf(cls):
        configP = ConfigParser()
        configP.read(config_filePath)
        host = configP.get("mysqlconf","host")
        port = configP.get("mysqlconf","port")
        user = configP.get("mysqlconf","user")
        password = configP.get("mysqlconf","password")
        db = configP.get("mysqlconf","db_name")

        return {"host":host, "port":int(port), "user":user,
                "password":password, "db":db}

if __name__ == "__main__":
    print(ConfigParse.get_db_conf())