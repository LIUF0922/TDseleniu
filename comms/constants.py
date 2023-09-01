import os

# 获取项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)
# 测试用例执行文件所在路径
CASE_DIR = os.path.join(BASE_DIR, 'testcases')
# 测试数据所在路径
DATA_DIR = os.path.join(BASE_DIR, 'datas')
# 测试数据excel文件
DATA_FILE = os.path.join(DATA_DIR, 'casesloc.xlsx')
# log所在路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')
INFO_FILE = os.path.join(LOG_DIR, 'info.log')
ERROR_FILE = os.path.join(LOG_DIR, 'error.log')
# 配置文件所在路径
CONF_DIR = os.path.join(BASE_DIR, 'cofig')
CONF_File = os.path.join(CONF_DIR, 'Basicdata.ini')
# 结果报告所在路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')
REPORT_FILE = os.path.join(REPORT_DIR, '结果报告.html')


