#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    for i in m_a:
        if type(i) is not list:
            raise TypeError('m_a must be a list of lists')
    for i in m_b:
        if type(i) is not list:
            raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError('m_a can\'t be empty')
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError('m_b can\'t be empty')
    for i in m_a:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError('m_a should contain only integers or\
 floats')
    for i in m_b:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError('m_b should contain only integers or\
 floats')
    size1 = len(m_a[0])
    for i in m_a:
        if len(i) != size1:
            raise TypeError('each row of m_a must be of the same size')
    size2 = len(m_b[0])
    for i in m_b:
        if len(i) != size2:
            raise TypeError('each row of m_b must be of the same size')
    if size1 != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    result = []
    n_row_a = len(m_a)
    n_col_a = len(m_a[0])
    n_col_b = len(m_b[0])
    for m in range(n_row_a):
        row = []
        for p in range(n_col_b):
            c = 0
            for n in range(n_col_a):
                c += m_a[m][n] * m_b[n][p]
            row.append(c)
        result.append(row)
    return result
