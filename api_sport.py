# -*- coding:utf-8 -*-
# __author__ = 'li.zh'
from http_request import Http


# search and search_by_team through different way to define method.
class sport_info:
    url = 'http://op.juhe.cn/onebox/basketball/nba?key=e36f907bb087e7ea19466492ca5f1dad'
    url_team = 'http://api.avatardata.cn/Nba/Team?key=17437a4f090a421e8ba33e1282acbd75&team={}'

    @classmethod
    def search(cls):
        return Http.get(cls.url)

    def search_by_team(self, team):
        search_url = self.url_team.format(team)
        result = Http.get(search_url)
        return result
