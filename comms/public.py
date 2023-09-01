from configparser import ConfigParser
from comms.constants import CONF_File


def replace_data(my_dict, key, new_value):
    """
    :param my_dict: 需要替换的字典类型的字符串
    :param key: 需要替换的key
    :param new_value: 替换数据
    :return: 替换后的字符串
    """
    try:
        mp_data = eval(my_dict)
        mp_data[key] = new_value
        return str(mp_data)
    except Exception as e:
        print('替换数据失败！', e)


def get_ini_data(head, key):
    """
    :param head: 配置文件区块名称
    :param key: 获取区块下对应的key
    :return: 返回该区块中key对应的值
    """
    try:
        cf = ConfigParser()
        cf.read(CONF_File, encoding='utf-8')
        return cf.get(head, key)
    except Exception as e:
        print('从ini文件读取测试数据失败！', e)


if __name__ == '__main__':
    result = get_ini_data('mysql', 'port')
    print(result)
