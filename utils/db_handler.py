#encoding=utf-8
import pymysql
from utils.config_handler import ConfigParse

class DB(object):

    def __init__(self):
        self.db_config = ConfigParse.get_db_conf()
        self.conn = pymysql.connect(
            host = self.db_config["host"],
            port = self.db_config["port"],
            user = self.db_config["user"],
            password = self.db_config["password"],
            database = self.db_config["db"],
            charset = "utf8"
        )
        self.cur = self.conn.cursor()

    def close_connect(self):
        # 关闭数据连接
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def get_api_list(self):
        try:
            sqlStr = "select * from interface_api where Active='y'"
            self.cur.execute(sqlStr)
            # 返回tuple对象
            apiList = list(self.cur.fetchall())
            return apiList
        except Exception as err:
            raise err

    def isExists(self,table):
        sqlStr = "show tables"
        self.cur.execute(sqlStr)
        tables = self.cur.fetchall()
        tables_list = []
        for tab in tables:
            tables_list.append(tab[0])
        if table in tables_list:
            return True
        return False

    def get_api_case(self,api_table):
        sqlStr = "select * from %s where Active=\'y\';" % api_table
        # print(sqlStr)
        self.cur.execute(sqlStr)
        api_case_list = list(self.cur.fetchall())
        return api_case_list

    def get_rely_data(self,api_name,case_id):
        sqlStr = "select Data from interface_store_data where APIName=\'%s\' and Case_ID=%s" % (api_name,case_id)
        self.cur.execute(sqlStr)
        # 字典对象
        rely_data = self.cur.fetchone()
        if rely_data:
            return rely_data[0]
        return False

    def write_store_data(self,api_name,case_id,data_store):
        sqlStr = "select * from interface_store_data where APIName=\'%s\' and Case_ID=%s" % (api_name,case_id)
        self.cur.execute(sqlStr)
        # print(sqlStr)
        query_result = self.cur.fetchall()
        if query_result:
            sqlStr = "update interface_store_data set Data=\"%s\",ExecuteTime=now() where APIName=\'%s\' and Case_ID=%s" % (data_store,api_name,case_id)
            self.cur.execute(sqlStr)
            self.conn.commit()
        else:
            sqlStr = "insert into interface_store_data(APIName,Case_ID,Data,ExecuteTime) values(\'%s\', %s,\"%s\",now())" % (api_name,case_id,data_store)
            self.cur.execute(sqlStr)
            self.conn.commit()

    def write_check_result(self,api_table,case_id,response_code,response_data,status,error_info,):
        if error_info:
            sqlStr = "update %s set ResponseCode=%s,ResponseData=\"%s\",Status=\"%s\",ErrorInfo=\"%s\",ExecuteTime=now() where Case_ID=%s" \
                    %(api_table,response_code, response_data,status,error_info,case_id)
        else:
            sqlStr = "update %s set ResponseCode=%s,ResponseData=\"%s\",Status=\"%s\",ExecuteTime=now() where Case_ID=%s" \
                     % (api_table, response_code, response_data, status, case_id)
        # print(sqlStr)
        self.cur.execute(sqlStr)
        self.conn.commit()

if __name__ == "__main__":
    db = DB()
    # print(db.get_api_list())
    print(db.get_api_case('login'))
    # print(db.write_store_data('register',1,{wo are}))
    # db.write_check_result('register','running is fault....',{"username":"luxiaoxia", "code":"01"},4)
    # print(db.isExists('interface_login_test_case'))
    db.close_connect()