import re

def check(response_data,check_point):
    errorKey = {}
    for key,value in check_point.items():
        if isinstance(value,str):
            # 说明是等值校验
            if response_data[key] != value:
                errorKey[key] = response_data[key]
        elif isinstance(value.dict):
            # 说明是需要通过正则或者类型做模糊校验
            sourceData = response_data[key]
            if "type" in value:
                # 说明是校验数据类型
                typeS = value["type"]
                if typeS == "N":
                    # 说明是校验整数类型
                    if not isinstance(sourceData, int):
                        errorKey[key] = sourceData
            elif "value" in value:
                # 说明需要通过正则表达式去模糊校验
                regStr = value["value"]
                rg = re.match(regStr, "%s" % sourceData)
                if not rg:
                    errorKey[key] = sourceData
            return errorKey

if __name__ == "__main__":
    r = {"code": "01", "userid": 12, "id": "a12"}
    c = {"code": "00", "userid": {"type": "N"}, "id": {"value": "^\d+$"}}
    print(check(r, c))

