import requests
import urllib
from abc import ABC, abstractmethod


class Generator(object):
    @classmethod
    def get_help(cls):
        return

    @classmethod
    def generate(cls, arg):
        # charset: str or list, length: int
        charset = arg["charset"]
        length = arg["length"]
        if type(charset) == type([]):
            charset = "".join(charset)
        charset = urllib.parse.quote(charset)
        return requests.get("http://tools.zsh2517.com/rand/?set={0}&len={1}".format(charset, length)).text

    @classmethod
    def special_multi(cls):
        """
        是否针对多元素单独调用，如果是的话，会调用 generate_multi ，否则仅仅反复调用 generate
        :return:
        """
        return True

    @classmethod
    def generate_multi(cls, length, arg):
        return [cls.generate(arg) for i in range(length)]

