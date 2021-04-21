def vector_size_check(*vector_variables):
    print("Expected Value : ",end='')
    for i in range(len(vector_variables)-1):
        if( len(vector_variables[i]) != len(vector_variables[i+1])):
            return False
        else:
            return True
'''
def vector_size_check(*vector_variables):
    print("Expected Value: ", end='')
    return all(len(vector_variables[0]) == x for x in [len(vec) for vec in vector_variables[1:]])
'''
# 실행결과
print(vector_size_check([1,2,3],[2,3,4],[5,6,7]))
print(vector_size_check([1, 3], [2,4], [6,7]))
print(vector_size_check([1, 3, 4], [4], [6,7]))

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        return ArithmeticError

    return [sum(i) for i in zip(*vector_variables)]

# 실행결과
print(vector_addition([1, 3], [2, 4], [6, 7])) # Expected value: [9, 14]
print(vector_addition([1, 5], [10, 4], [4, 7])) # Expected value: [15, 16]
print(vector_addition([1, 3, 4], [4], [6,7])) # Expected value: ArithmeticError

from functools import reduce
def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        return ArithmeticError
    
    return [reduce(lambda x, y : x-y, vec) for vec in zip(*vector_variables)] 

# 실행결과
print(vector_subtraction([1, 3], [2, 4])) # Expected value: [-1, -1]
print(vector_subtraction([1, 5], [10, 4], [4, 7])) # Expected value: [-13, -6]


def scalar_vector_product(alpha, vector_variable):
    return [alpha*i for i in vector_variable]

# 실행결과
print (scalar_vector_product(5,[1,2,3])) # Expected value: [5, 10, 15]
print (scalar_vector_product(3,[2,2])) # Expected value: [6, 6]
print (scalar_vector_product(4,[1])) # Expected value: [4]


def matrix_size_check(*matrix_variables):
    return all([len(set(len(matrix[0]) for matrix in matrix_variables)) == 1]) and all([len(matrix_variables[0]) == len(matrix) for matrix in matrix_variables])

# 실행결과
matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]


print (matrix_size_check(matrix_x, matrix_y, matrix_z)) # Expected value: False
print (matrix_size_check(matrix_y, matrix_z)) # Expected value: True
print (matrix_size_check(matrix_x, matrix_w)) # Expected value: True

'''
from functools import reduce
def is_matrix_equal(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        return False

    list_ = []
    for matrix in matrix_variables:
        for i in zip(*matrix):
            list_.append(sum(i))
        
    return all(list_[0] == size for size in list_[1:])
'''

def is_matrix_equal(*matrix_variables):
    return all([all([len(set(row)) == 1 for row in zip(*matrix)]) for matrix in zip(*matrix_variables)])

# 실행결과    
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]

print (is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False
print (is_matrix_equal(matrix_x, matrix_x)) # Expected value: True


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[ sum(x) for x in zip(*matirx)]for matirx in zip(*matrix_variables)]

# 실행결과
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]
print (matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]

def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[x[0] - sum(x[1:]) for x in zip(*matrix)]for matrix in zip(*matrix_variables)]

# 실행결과
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_subtraction(matrix_x, matrix_y)) # Expected value: [[0, -3], [0, 1]]
print (matrix_subtraction(matrix_x, matrix_y, matrix_z)) # Expected value: [[-2, -7], [-5, -2]]


def matrix_transpose(matrix_variable):
    v = [matrix for matrix in zip(*matrix_variable)]
    print(*v)
    print(type(v))
    return [[x for x in matrix] for matrix in zip(*matrix_variable)]

# 실행결과
matrix_w = [[2, 5], [1, 1], [2, 2]]
matrix_transpose(matrix_w)


def scalar_matrix_product(alpha, matrix_variable):
    return [[alpha*x for x in matrix] for matrix in matrix_variable]

# 실행결과
matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

print(scalar_matrix_product(3, matrix_x)) #Expected value: [[6, 6], [6, 6], [6, 6]]
print(scalar_matrix_product(2, matrix_y)) #Expected value: [[4, 10], [4, 2]]
print(scalar_matrix_product(4, matrix_z)) #Expected value: [[8, 16], [20, 12]]
print(scalar_matrix_product(3, matrix_w)) #Expected value: [[6, 15], [3, 3], [6, 6]]


def is_product_availability_matrix(matrix_a, matrix_b):
    return len([col_vector for col_vector in zip(*matrix_a)]) == len(matrix_b)

# 실행결과
matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(is_product_availability_matrix(matrix_y, matrix_z)) # Expected value: True
print(is_product_availability_matrix(matrix_z, matrix_x)) # Expected value: True
print(is_product_availability_matrix(matrix_z, matrix_w)) # Expected value: False //matrix_w가없습니다
print(is_product_availability_matrix(matrix_x, matrix_x)) # Expected value: True


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)]for row_a in matrix_a]

# 실행결과
matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]
#print(matrix_product(matrix_z, matrix_w)) # Expected value: False