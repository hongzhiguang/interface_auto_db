from utils.db_handler import DB
from utils.HttpClient import *
from action.encryption import *
from action.rely_data_store import *
from action.check_result import check
from action.get_rely import get_req_data


db = DB()
# 获取API
api_list = db.get_api_list()
for api in api_list:
    api_name = api[1]
    request_url = api[2]
    request_method = api[3]
    request_type = api[4]
    api_test_case = api[5]
    # print(api_name,api_test_case)
    if db.isExists(api_test_case):
        # 对API的case进行操作
        api_case_list = db.get_api_case(api_test_case)
        for case in api_case_list:
            case_id = case[0]
            try:
                request_data = eval(case[1])
            except SyntaxError as err:
                continue
            rely_data_rule = case[2]
            data_store_rule = case[5]
            check_point = case[6]
            # print(case_id,rely_data_rule,data_store_rule,check_point)
            # 如果rely_data不为空，进行数据依赖处理
            if rely_data_rule:
                rely_data_rule = eval(case[2])
                request_data = get_req_data(db,api_name,case_id,request_data,rely_data_rule)
            # 如果是登录接口，需要对密码进行加密
            if api_name == "login":
                request_data = Encryption.md5(request_data)
            response_obj = HttpClient.request(request_url,request_method,request_type,request_data)
            # 进行数据依赖存储
            if response_obj.status_code == 200 and data_store_rule:
                response_data = response_obj.json()
                data_store(db,api_name,case_id,eval(data_store_rule),request_data,response_data)
            # 进行验证响应结果
            if check_point:
                error_info = check(response_obj.json(),eval(check_point))
            # 解决responsebody中同时包含有单引号和双引号的问题
            resp_str = str(str(response_obj.json())).replace("'", "\\'")
            resp_str_1 = resp_str.replace('"', '\\"')
            if error_info:
                db.write_check_result(api_test_case,case_id,response_obj.status_code,resp_str_1,
                                      "fail",error_info)
            else:
                db.write_check_result(api_test_case,case_id,response_obj.status_code,resp_str_1,
                                      "pass","")








