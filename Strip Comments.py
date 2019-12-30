# -*- coding: utf-8 -*-

                       
def solution(string,markers):
    string_list = string.split('\n')
    for m in markers:
        string_list = [x.split(m)[0].strip() for x in string_list]
    new_string = ('\n').join(string_list)
    return new_string
    