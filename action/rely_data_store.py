from utils.db_handler import DB

def data_store(db,api_name,case_id,data_store_rule,request_data,response_data):
    data = {}
    for key in data_store_rule:
        if key == "request":
            for item in data_store_rule[key]:
                if item in list(request_data.keys()):
                    k = "{0}.{1}.{2}.{3}".format("request",api_name,str(case_id),item)
                    data[k] = request_data[item]
                else:
                    continue
        elif key == "response":
            for item in data_store_rule[key]:
                if item in list(response_data.keys()):
                    k = "{0}.{1}.{2}.{3}".format("response", api_name, str(case_id), item)
                    data[k] = response_data[item]
                else:
                    continue
        else:
            return False
    try:
        db.write_store_data(api_name,case_id,data)
    except Exception as err:
        return False

if __name__ == "__main__":
    db = DB()
    data_store_rule = {"request":["username","password"],"response":["userid"]}
    request_data = {"username":"luxiaoxia","password":"luxiaoxia123","email":"luxiaoxia@qq.com"}
    response_data = {'username': 'luxiaoxia', 'code': '01'}
    data_store(db,"register",1,data_store_rule,request_data,response_data)