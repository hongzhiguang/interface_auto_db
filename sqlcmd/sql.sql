#------创建数据库interface_autotester
CREATE DATABASE IF NOT EXISTS interface_autotester DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

#------创建表interface_api
create table interface_api(
	API_ID int not null auto_increment comment "自增长主键",
	APIName varchar(50) not null comment "接口的名字",
	RequestUrl varchar(50) not null comment "请求接口的URL",
	RequestMethod varchar(10) not null comment "接口请求的方式",
	paramsType varchar(20) not null comment "传参方式",
	APITestCase varchar(50) not null comment "接口API对应的测试用例",
	Active varchar(10) not null comment "API是否执行测试",
	RelyDB tinyint default 0 comment "是否依赖数据库",
	ExecuteTime datetime,
	unique index(APIName),
	primary key(API_ID)
)engine=InnoDB default charset=utf8;

#------向表interface_api插入数据
insert into interface_api(APIName,RequestUrl,RequestMethod,paramsType,APITestCase,Active) values("register","http://39.106.41.11:8080/register/","post","form","注册接口用例","y");
insert into interface_api(APIName,RequestUrl,RequestMethod,paramsType,APITestCase,Active) values("login","http://39.106.41.11:8080/login/","post","form","登录接口用例","n");
insert into interface_api(APIName,RequestUrl,RequestMethod,paramsType,APITestCase,Active) values("query","http://39.106.41.11:8080/getBlogContent/","get","url","查询博文用例","n");

#------创建表interface_register_test_case\interface_login_test_case\interface_query_test_case
create table interface_register_test_case(
	Case_ID int not null auto_increment comment "自增长主键",
	RequestData varchar(255) comment "接口请求数据",
	RelyData varchar(255) comment "case依赖的数据",
	ResponseCode int comment "接口返回的响应码",
	ResponseData varchar(255) comment "接口响应body",
	DataStore varchar(255) comment "需要存储的数据",
	CheckPoint varchar(255) comment "接口响应校验依据数据",
	Active varchar(10) not null comment "是否执行测试",
    Status  varchar(10) comment "",
	ErrorInfo varchar(1000) comment "错误信息列",
	ExecuteTime datetime,
	primary key(Case_ID),
  index(API_ID)
)engine=InnoDB default charset utf8;

create table interface_login_test_case(
	Case_ID int not null auto_increment comment "自增长主键",
	RequestData varchar(255) comment "接口请求数据",
	RelyData varchar(255) comment "case依赖的数据",
	ResponseCode int comment "接口返回的响应码",
	ResponseData varchar(255) comment "接口响应body",
	DataStore varchar(255) comment "需要存储的数据",
	CheckPoint varchar(255) comment "接口响应校验依据数据",
	Active varchar(10) not null comment "是否执行测试",
    Status  varchar(10) comment "",
	ErrorInfo varchar(1000) comment "错误信息列",
	ExecuteTime datetime,
	primary key(Case_ID),
  index(API_ID)
)engine=InnoDB default charset utf8;

create table interface_query_test_case(
	Case_ID int not null auto_increment comment "自增长主键",
	RequestData varchar(255) comment "接口请求数据",
	RelyData varchar(255) comment "case依赖的数据",
	ResponseCode int comment "接口返回的响应码",
	ResponseData varchar(255) comment "接口响应body",
	DataStore varchar(255) comment "需要存储的数据",
	CheckPoint varchar(255) comment "接口响应校验依据数据",
	Active varchar(10) not null comment "是否执行测试",
    Status  varchar(10) comment "",
	ErrorInfo varchar(1000) comment "错误信息列",
	ExecuteTime datetime,
	primary key(Case_ID),
  index(API_ID)
)engine=InnoDB default charset utf8;

#------向表interface_register_test_case插入数据
insert into interface_register_test_case(RequestData,RelyData,DataStore,CheckPoint,Active)
values('{"username":"luxiaoxia","password":"luxiaoxia123","email":"luxiaoxia@qq.com"}','','{"request":["username","password"],"response":["userid"]}','{"code":"01"}','y');
insert into interface_register_test_case(RequestData,RelyData,DataStore,CheckPoint,Active)
values('{"username":"lujingsi","password":"lujingxia123","email":"lujingxia@qq.com"}','','{"request":["username","password"],"response":["userid"]}','{"code":"01"}','y');
insert into interface_register_test_case(RequestData,RelyData,DataStore,CheckPoint,Active)
values('{"username":"lujingwen","password":"lujingwen123","email":"lujingwen@qq.com"}','','{"request":["username","password"],"response":["userid"]}','{"code":"01"}','y');
insert into interface_register_test_case(RequestData,RelyData,DataStore,CheckPoint,Active)
values('username=wcd23&password=wcx123wac&email=wcx@qq.com','','{"request":["username","password"],"response":["code"]}','{"code":"01"}','y');

#------向表interface_login_test_case插入数据
insert into interface_login_test_case(RequestData,RelyData,DataStore,CheckPoint,Active)
values('{"username":"","password":""}','["request.register.1.username","request.register.1.password"]','{"response":["token","userid"]}','{"code":"00"}','y');
insert into interface_login_test_case(RequestData,RelyData,DataStore,CheckPoint,Active)
values('{"username":"","password":""}','["request.register.2.username","request.register.2.password"]','{"response":["token","userid"]}','{"code":"00"}','y');
insert into interface_login_test_case(RequestData,RelyData,DataStore,CheckPoint,Active)
values('{"username":"","password":""}','["request.register.3.username","request.register.3.password"]','{"response":["token","userid"]}','{"code":"00"}','y');
insert into interface_login_test_case(RequestData,RelyData,DataStore,CheckPoint,Active)
values('{"username":"","password":""}','["request.register.4.username","request.register.4.password"]','{"response":["token","userid"]}','{"code":"00"}','y');

#------向表interface_query_test_case插入数据
insert into interface_query_test_case(RequestData,RelyData,DataStore,CheckPoint,Active)
values('{"userid": "" , "token": "" }','["response.login.1.userid","response.login.1.token"]','','{"code":"00"}','y');


#------创建interface_data_store表
create table interface_store_data(
    APIName varchar(50) not null comment "接口的名字",
    Case_ID int not null comment "对应interface_test_case里面的id",
    Data varchar(255) comment "存储的依赖数据",
    ExecuteTime datetime,
    index(APIName,Case_ID)
)engine=InnoDB default charset=utf8;