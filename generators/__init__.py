#!/usr/bin/python
# -*- coding: UTF-8 -*-
import generators.email
import generators.string

__all__ = ["email", "string", "gen"]


class gen:
    email = email.gen_email
    string = string.gen_string
    pass



# if __name__ == '__main__':
#     print('作为主程序运行')
# else:
#     print('package_runoob 初始化')
