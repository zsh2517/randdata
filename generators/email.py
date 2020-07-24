import Generator
import generators.string
import random


class gen_email(Generator.Generator):
    @classmethod
    def generate(cls, arg: dict):
        """
        charset: str or list, length: int, suffix: list
        """
        charset = arg.get("charset", "1234567890poiuytrewqasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM")
        length = arg.get("length", random.randint(4, 10))
        suffix = arg.get("suffix", ["qq.com", "gmail.com", "outlook.com", "126.com", "163.com"])
        p_gen: generators.string.gen_string = generators.string.gen_string()
        prefix = p_gen.generate({
            "charset": charset,
            "length": length
        })
        return prefix + "@" + random.choice(suffix)
