#!/usr/bin/python
# -*- coding: UTF-8 -*-
import generators.email
import generators.string
import generators.tel

__all__ = ["gen", "email", "string", "tel"]


class gen:
    email = email.gen_email
    string = string.gen_string
    tel = tel.gen_tel
    pass



# if __name__ == '__main__':
#     print('作为主程序运行')
# else:
#     print('package_runoob 初始化')
