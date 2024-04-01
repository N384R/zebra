from copy import deepcopy
from itertools import chain

def split_operator(operator):
    operator = operator.split()
    _operator = [[operator[0]]]
    if len(operator) == 0:
            print("Error: Invalid Operator")
            exit()
    __operator = []
    for i in range(1, len(operator)):
        __operator.append(operator[i])
    _operator.append(__operator)
    return _operator

def number_sort(operator):
    def _number_sort(operator):
        for i in range(len(operator)-1):
            if ('^' in operator[i]) and ('^' in operator[i]):
                if operator[i][:-1] < operator[i+1][:-1]:
                    operator[i], operator[i+1] = operator[i+1], operator[i]
                    if operator[0] != '-':
                        operator.insert(0, '-')
                    elif operator[0] == '-':
                        del operator[0]
                    return _number_sort(operator)
            elif ('^' not in operator[i]) and ('^' not in operator[i+1]):
                if operator[i] > operator[i+1]:
                    operator[i], operator[i+1] = operator[i+1], operator[i]
                    if operator[0] != '-':
                        operator.insert(0, '-')
                    elif operator[0] == '-':
                        del operator[0]
                    return _number_sort(operator)
        return operator 
    
    for i in range(1, len(operator)):
        operator[i] = _number_sort(operator[i])
    return operator

def sign_sort(operator):
    sign = False
    for i in range(1, len(operator)):
        if operator[i] == '-':
            if sign is True:
                operator[i] = '+'  
                sign = False
            elif sign is False:
                sign = True
    return operator

def dirac_sort(operator):
    def _dirac_sort(operator):
        _operator = []
        __operator = deepcopy(operator)
        for i in range(len(operator)-1):
            if ('^' not in operator[i]) and ('^' in operator[i+1]) and (operator[i] != '-'):
                if operator[i] == operator[i+1][:-1]:
                    operator[i], operator[i+1] = operator[i+1], operator[i]
                    del __operator[i]; del __operator[i]
                    if operator[0] == '-':
                        del operator[0]; del __operator[0]
                        _operator.append('-')
                    _operator.append(__operator)
                    _operator.append('-')
                    _operator.append(operator)
                    return True, True, _operator
                else:
                    operator[i], operator[i+1] = operator[i+1], operator[i]
                    if operator[0] != '-':
                        operator.insert(0, '-')
                    elif operator[0] == '-':
                        del operator[0]
                    return True, False, operator
        return False, False, operator

    for i in range(1, len(operator)):
        if len(operator[i]) != 1:
            a, b, _operator = _dirac_sort(operator[i])
            if a:
                if b:
                    for j in reversed(range(len(_operator))):
                        operator.insert(i, _operator[j])
                    del operator[i+len(_operator)-1]
                    # if (operator[i-1] == '-') and (operator[i] == '-'):
                    #     operator[i] = '+'
                    #     del operator[i-1]
                    # elif (operator[i-1] == '+') and (operator[i] == '-'):
                    #     del operator[i-1]
                    if (operator[i] == '-') or (operator[i-1] == '-'):
                        operator = sign_sort(operator)
                    print(operator)
                    return dirac_sort(operator)
                else:
                    operator[i] = _operator
                    if operator[i][0] == '-':
                        del operator[i][0]
                        if operator[i-1] == '-':
                            operator[i-1] = '+'
                        elif operator[i-1] == '+':
                            operator[i-1] = '-'
                        else:
                            operator.insert(i, '-')
                    print(operator)
                    return dirac_sort(operator)
    return operator

def length_sort(operator):  
    length = []
    for i in range(1, len(operator)):
        if (operator[i] != '-') and (operator[i] != '+'):
            length.append([i, len(operator[i])])

    _length = deepcopy(length)
    _length.sort(key=lambda x: x[1])
    _operator = deepcopy(operator)
    for i in range(len(length)):
        operator[_length[i][0]-1] = _operator[length[i][0]-1]
        operator[_length[i][0]] = _operator[length[i][0]]
    return operator

def print_operator(operator):
    sub = str.maketrans("0123456789^", "₀₁₂₃₄₅₆₇₈₉†")
    _operator = deepcopy(operator)
    _operator = list(chain(*_operator))
    coeff = _operator[0]
    a = False
    if '-' in coeff:
        coeff = coeff[1:]; a = True
        for i in range(1, len(operator)):
            if operator[i] == '-': operator[i] = '+'
            elif operator[i] == '+': operator[i] = '-'

    if (operator[1] == '-'):
        if a: line = coeff
        else: line = '- ' + coeff
        _operator = _operator[2:]

    else:
        if a: line = '- '
        else: line = ''
        _operator = _operator[1:]

    for i in range(len(_operator)):
        if _operator[i] == '-':
            line += " - " + coeff
        elif _operator[i] == '+':
            line += " + " + coeff
        else:
            notation = _operator[i].translate(sub)
            line += " a" + notation
    return line

def print_operator(operator):
    sub = str.maketrans("0123456789^", "₀₁₂₃₄₅₆₇₈₉†")
    _operator = deepcopy(operator)
    coeff = _operator[0][0]
    _operator = list(chain(*_operator))
    if '-' in coeff:
        coeff = coeff[1:]
        for i in range(1, len(_operator)):
            if _operator[i] == '-': _operator[i] = '+'
            elif _operator[i] == '+': _operator[i] = '-'

    line = ''
    if (_operator[1] != '-') and (_operator[1] != '+'):
        line += coeff

    for i in range(1, len(_operator)):
        if _operator[i] == '-':
            line += " - " + coeff
        elif _operator[i] == '+':
            line += " + " + coeff
        else:
            notation = _operator[i].translate(sub)
            line += " a" + notation
    return line[1:]

def sort_operator(operator):
    operator = split_operator(operator)
    print("Recall:", print_operator(operator))
    operator = number_sort(operator)
    operator = dirac_sort(operator)
    operator = number_sort(operator)
    operator = length_sort(operator)
    print(operator)
    print("Result:", print_operator(operator))
    return operator

print("[Fermionic Operator Sorting]\n")
print("This script will sort the fermionic operators in the Hamiltonian")
print("in the order of the qubit operators.\n")

print("Rule: [value] [operator] [operator] ...\n(^ is indicates the dagger operator)")
input_operator = input("Input: ")
sort_operator(input_operator)
