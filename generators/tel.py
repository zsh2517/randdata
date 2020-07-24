import random
from abc import ABC

import Generator


class gen_tel(Generator.Generator):
    """
    手机号随机
    """

    @classmethod
    def get_help(cls, ):
        return

    @classmethod
    def generate(cls, arg):
        tel_format = "(+A)B-xxxx-xxxx"  # (+86)131-2333-3333
        tel_format = arg.get("format", "Bxxxxxxxx")
        if "code" in arg.keys():
            code = arg["code"]
        else:
            code = {
                "A": ["86"],
                # A 部分代码，主要是国家代码
                "B": [
                    "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "157", "158", "159", "178",
                    "182",
                    "183", "184", "187", "188",  # 中国移动
                    "130", "131", "132", "145", "155", "156", "185", "186", "176", "175",  # 中国联通
                    "133", "149", "153", "180", "181", "189", "177",  # 中国电信
                ]
                # B 部分代码，可以是地区代码或者是比如国内的号段
            }
        this = tel_format
        for k in code.keys():
            if k in this:
                this = this.replace(k, random.choice(code[k]))
        this = list(this)
        for i in range(len(this)):
            if this[i] == "x":
                this[i] = str(random.randint(0, 9))
        return "".join(this)
