import logging
import log_func
import os
import requests

# error定義
class InvalidStatusCode(Exception):
    pass

# ログの設定
logger = logging.getLogger(__name__)
log_util = log_func.LogUtil(logger)

class HttpClient():
    base_url = r'https://api.twitter.com/'
    def __init__(self, api_key, api_key_secret, token):
        self.api_key = api_key
        self.api_key_secret = api_key_secret
        self.token = token
        self.header = self.__create_header()

    def __create_header(self):
        """
        ヘッダ作成
        :param token:
        :return:
        """
        return {'Authorization': f'Bearer {self.token}'}

    def send_get_method(self, url):
        """
        urlにgetメソッドを投げる
        :param url:
        :param header:
        :return:
        """
        log_util.log_func_start(self.send_get_method.__name__)
        # リクエスト
        url = self.base_url + url
        logger.info('request get %s', url)
        response = requests.request('GET', url, headers=self.header)
        logger.debug('response: %s', response)
        if response.status_code != 200:
            logger.error('status code: %s', response.status_code)
            logger.error('response body: %s', response.text)
            raise InvalidStatusCode('Request not success')
        log_util.log_func_end(self.send_get_method.__name__)
        return response.json()


    def get_user_info(self, username_list = None, user_field_list = None):
        """
        URLを作成
        :param username:
        :param user_fields:
        :return:
        """
        log_util.log_func_start(self.get_user_info.__name__)
        method_url = r'2/users/by'
        if username_list is None:
            username_list = []
        if user_field_list is None:
            user_field_list = ['id', 'name', 'username']
        query_username = rf'usernames={",".join(username_list)}'
        query_user_field = rf'user.fields={",".join(user_field_list)}'
        logger.debug('query_username: %s', query_username)
        logger.debug('query_user_field: %s', query_user_field)
        url = rf'{method_url}?{query_username}&{query_user_field}'
        log_util.log_func_end(self.get_user_info.__name__)
        return self.send_get_method(url)


    def get_followers(self, userid):
        """
        follower取得
        :return:
        """
        log_util.log_func_start(self.get_followers.__name__)
        method_url = fr'2/lists/{userid}/followers'
        log_util.log_func_end(self.get_followers.__name__)
        return self.send_get_method(method_url)

