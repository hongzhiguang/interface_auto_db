import os

# 工程路径
proj_path = os.path.dirname(os.path.dirname(__file__))

# 数据库配置文件路径
config_filePath = os.path.normpath(os.path.join(proj_path,"conf","db_config.ini"))