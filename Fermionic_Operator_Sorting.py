import numpy as np
import copy

def print_operator(operator):
    _operator = copy.copy(operator)
    _operator = [operator[0]]
    if len(operator) == 0:
            print("Error: Invalid Operator")
            exit()
    sub = str.maketrans("0123456789^", "₀₁₂₃₄₅₆₇₈₉†")
    line = ''

    for i in range(1, len(operator)):
        try:
            if operator[i][1] == "^":
                notation = operator[i].translate(sub)
                line += " a" + notation
            else:
                try:
                    if float(operator[i]):
                        if operator[i][0] == '-':
                            line += " -" + operator[i][1:]
                            _operator[i] = _operator[i][1:]
                            _operator.insert(0, '-')

                        else:
                            line += " " + operator[i]
                except:
                    print("Error: Invalid Operator")
                    exit()
        except:
            if len(operator[i]) == 1:
                if operator[i][0] == '-':
                    try:
                        if operator[i+1][0] == '-':
                            del operator[i+1]
                            operator[i] = '+'
                    except:
                        line += " - "
                elif operator[i][0] == '1':
                    line += "1"
                else:
                    notation = operator[i].translate(sub)
                    line += " a" + notation
            else:
                print("Error: Invalid Operator")
                exit()
    return line[1:], _operator

def number_sort(operator):
    for i in range(1, len(operator)-1):
        if len(operator[i]) == len(operator[i+1]) and (operator[i] != '-'):
            if len(operator[i]) == 2:
                if operator[i] < operator[i+1]:
                    operator[i], operator[i+1] = operator[i+1], operator[i]
                    operator.insert(0, '-')
                    return number_sort(operator)
                return operator
            elif len(operator[i]) == 1:
                if operator[i] > operator[i+1]:
                    operator[i], operator[i+1] = operator[i+1], operator[i]
                    operator.insert(0, '-')
                    return number_sort(operator)
                return operator
    return operator

def dirac_delta_sort(operator):
    _operator = copy.copy(operator)
    for i in range(1, len(operator)-1):
        if operator[i][0] == operator[i+1][0]:
            if len(operator[i]) < len(operator[i+1]):
                operator[i], operator[i+1] = operator[i+1], operator[i]
                del _operator[i]; del _operator[i]; del operator[0]
                operator.insert(0, '-')
                _operator += operator
                print(_operator)
                return dirac_delta_sort(_operator)
        if (operator[i][0] != operator[i+1][0]) and (operator[i][0] != '-'):
            if len(operator[i]) < len(operator[i+1]):
                operator[i], operator[i+1] = operator[i+1], operator[i]
                operator.insert(0, '-')
                print(operator)
                return dirac_delta_sort(operator)
    return operator

def sort_operator(operator):
    note, operator = print_operator(operator)
    print("Recall:", note)
    operator = number_sort(operator)
    operator = dirac_delta_sort(operator)
    operator = number_sort(operator)
    note, operator = print_operator(operator)
    print("Result:", note)

print("[Fermionic Operator Sorting]\n")
print("This script will sort the fermionic operators in the Hamiltonian")
print("in the order of the qubit operators.\n")

print("Rule: [value] [operator] [operator] ...\n(^ is indicates the dagger operator)")
input_operator = input("Input: ")

# Read the input operator
operator = input_operator.split()

# Sort the fermionic operators
# sort_operator(operator)

note, operator = print_operator(operator)
print("Recall:", note)
print("initial:", operator)
operator = number_sort(operator)
print("number_sort:", operator)
# operator = dirac_delta_sort(operator)
# print("dirac_delta_sort:", operator)