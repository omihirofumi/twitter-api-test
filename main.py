import json

import requests
import csv
import os
import configparser
import logging
import log_func
from httpClient import http_client

# 変数宣言
CONFIG_DIR = 'config'
CONFIG_FILE_NAME = 'twitter_api.config'

# log
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
log_util = log_func.LogUtil(logger)

def load_config():
    """
    config読み込み
    :return:
    """
    log_util.log_func_start(load_config.__name__)
    config_file_path = os.path.join(CONFIG_DIR, CONFIG_FILE_NAME)
    logger.debug('config path: %s', os.path.abspath(config_file_path))
    config = configparser.RawConfigParser()
    config.read(config_file_path)
    api_key = config.get("twitter", "api_key")
    api_key_secret = config.get("twitter", "api_key_secret")
    token = config.get("twitter", "bearer_token")
    logger.debug('api_key: %s', api_key)
    logger.debug('api_key_secret: %s', api_key_secret)
    logger.debug('token: %s', token)
    log_util.log_func_end(load_config.__name__)
    return api_key, api_key_secret, token

def main():
    log_util.log_func_start(__name__)
    # config読み込み
    api_key, api_key_secret, token = load_config()
    # httpClient生成
    httpclient = http_client.HttpClient(api_key, api_key_secret, token)
    # username
    username = 'username'
    username_list = []
    user_field_list = ['id', 'name', 'username', 'description']
    username_list.append(username)
    res = httpclient.get_user_info(username_list, user_field_list)
    logger.info(res)
    log_util.log_func_end(__name__)

if __name__ == '__main__':
    main()
