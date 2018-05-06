"""Решение домашнего задания №17 курса Нетология Пайтон."""
import requests


class ApiYandex():
    """Класс для описания методов подключения к API Яндекс Метрика."""

    url = None
    app_id = None
    token = None
    responce = None
    params = None

    def __init__(self, url, app_id, token):
        """Описание характеристик класса."""
        self.url = url
        self.app_id = app_id
        self.token = token
        self.params = {'id': self.app_id, 'oauth_token': self.token}

    def conect(self, key_for_url, params={}):
        """Выполнение запроса к API Яндекс Метрика."""
        if len(params) == 0:
            params = self.params
        self.responce = \
            requests.get('{}{}'.format(self.url, key_for_url), params)

    def get_counters(self, type_of_counters_param):
        """Получение перечня счетчиков."""
        return [counter[type_of_counters_param]
                for counter in self.responce.json()['counters']]


def main():
    """Инициализация программы и вывод результатов."""
    URL = 'https://api-metrika.yandex.ru/'
    APP_ID = 'b1a888e5e4e145da9d5e7fa88aab6f13'
    TOKEN = 'AQAAAAAD-yicAAT8Hym6nbCV0kDOpr7ls7Xiax0'

    counters_yandex = ApiYandex(URL, APP_ID, TOKEN)
    counters_yandex.conect('management/v1/counters')
    counters = counters_yandex.get_counters('id')

    for counter in counters:
        params = {'metrics': 'ym:s:visits,ym:s:pageviews,ym:s:users',
                  'id': counter, 'oauth_token': counters_yandex.token}
        counters_yandex.conect('stat/v1/data', params)
        information = counters_yandex.responce.json()['totals']
        print('Счетчик - {}:'.format(counter))
        print('Визиты - {}'.format(information[0]))
        print('Просмотры - {}'.format(information[1]))
        print('Посетители - {}'.format(information[2]))


main()
