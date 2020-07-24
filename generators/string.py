import random
from abc import ABC

import Generator


class gen_string(Generator.Generator):
    @classmethod
    def get_help(cls, ):
        return

    @classmethod
    def generate(cls, arg):
        # charset: str or list, length: int
        if "charset" in arg.keys():
            charset = arg["charset"]
        else:
            charset = arg.get("charset", "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890")
        special_sql = ""
        special_html = ""
        length = arg.get("length", 8)
        if type(charset) == type([]):
            charset = "".join(charset)
        return "".join([random.choice(charset) for i in range(length)])
