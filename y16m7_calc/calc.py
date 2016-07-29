#conding=UTF-8

#This is a simple calculator

import re
import functools


def remove_duplicates(formula):

    formula = re.sub(r'\+\s*\+', '+', formula)
    formula = re.sub(r'\+\s*\-', '-', formula)
    formula = re.sub(r'\-\s*\+', '-', formula)
    formula = re.sub(r'\-\s*\-', '+', formula)
    return formula


def handle_special_case(plus_minus_opretors, multiply_divide_formula):
    for index, item in enumerate(multiply_divide_formula):
        if item.endswith('*') or item.endswith('/'):
            multiply_divide_formula[index] = multiply_divide_formula[index] + plus_minus_opretors[index] + multiply_divide_formula[index+1]
            del plus_minus_opretors[index]
            del multiply_divide_formula[index+1]
    return plus_minus_opretors, multiply_divide_formula


def compute_multiply_divide(formula):
    _MD_opretors = re.findall(r'[*/]', formula)
    _calc_list = re.split(r'[*/]', formula)
    _MD_res = None
    for index, item in enumerate(_calc_list):
        if _MD_res is not None:
            if _MD_opretors[index-1] == '*':
                _MD_res = _MD_res * float(item)
            else:
                _MD_res = _MD_res / float(item)
        else:
            _MD_res = float(item)
    print('This MD_res is: %s' % _MD_res)
    return _MD_res


def compute(formula):

    formula = formula.strip('()')
    formula = remove_duplicates(formula)
    formula = re.sub(r'\s+', '', formula)
    plus_minus_opretors = re.findall(r'[+-]', formula)
    multiply_divide_formula = re.split(r'[+-]', formula)
    if multiply_divide_formula[0] == '':
        if plus_minus_opretors[0] == '+':
            del plus_minus_opretors[0]
            del multiply_divide_formula[0]
        else:
            multiply_divide_formula[1] = plus_minus_opretors[0] + multiply_divide_formula[1]
            del plus_minus_opretors[0]
            del multiply_divide_formula[0]
    plus_minus_opretors, multiply_divide_formula = handle_special_case(plus_minus_opretors, multiply_divide_formula)
    for index, item in enumerate(multiply_divide_formula):
        if re.search(r'[*/]', item):
            MD_res = compute_multiply_divide(item)
            multiply_divide_formula[index] = MD_res

    print(multiply_divide_formula, plus_minus_opretors)

    total_res = None
    for index, item in enumerate(multiply_divide_formula):
        if total_res is not None:
            if plus_minus_opretors[index-1] == '+':
                total_res = total_res + float(item)
            else:
                total_res = total_res - float(item)
        else:
            total_res = float(item)

    print(formula, total_res)
    return total_res


def calc(formula):
    parentheses_flag = True
    _calc_res = None
    while parentheses_flag:
        _re_item = re.search(r'\([^()]+\)', formula)
        if _re_item:
            formula = formula.replace(_re_item.group(), str(compute(_re_item.group())))
        else:
            parentheses_flag = False
            _calc_res = compute(formula)
    return _calc_res




# res = calc('1 - 2 * ( (60-30 +(-9-2-5-2*3-5/3-40*4/2-3/5+6*3) * (-9-2-5-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )')
# print 'The result is : %s' % res

res1 = calc('2+(3*6-5*(-5*4))')
print 'test: %s' % res1