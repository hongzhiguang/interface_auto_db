from utils.db_handler import *

def get_req_data(db,api_name,case_id,request_data,rely_data_rule):
    req_data = {}
    for key in request_data:
        for item in rely_data_rule:
            if key == item.split(".")[-1]:
                storeData = db.get_rely_data(item.split(".")[1], case_id)
                if storeData:
                    storeData = eval(storeData)
                else:
                    continue
                if item in storeData.keys():
                    req_data[key] = storeData[item]
                else:
                    continue
            else:
                continue
    return req_data

# if __name__ == "__main__":
    # r = {"username": "", "password": ""}
    # rely_data_rule = ["request.register.1.username","request.register.1.password"]
    # storeData ={"request.register.1.username": "lujingxia","request.register.1.password": "lujingxia123"}
    # print(get_req_data(r,rely_data_rule,storeData))
