def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print str(m[i][j]) + " ",
        print
    print
    
def lcs_length(x, y):
    m = len(x) + 1 # +1 for zeroes
    n = len(y) + 1
    b = [["." for _ in range(n)] for _ in range(m)]
    c = [[None for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        c[i][0] = 0
    for i in range(n):
        c[0][i] = 0
    for i in range(1,m):
        for j in range(1,n):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '\\'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "|"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "<"
    return c, b

def put_together(c, b, x, y):
    rows = len(x) + 2 # +1 for zeroes, +1 for x
    cols = len(y) + 2
    matrix = [[None for _ in range(cols)] for _ in range(rows)]
    matrix[0][0] = "-"
    matrix[1][0] = "-"
    matrix[0][1] = "-  "
    for i in range(2, rows):
        matrix[i][0] = x[i-2]
    for i in range(2, cols):
        matrix[0][i] = str(y[i-2]) + "  "
    for i in range(1, rows):
        for j in range(1, cols):
            matrix[i][j] = str(c[i-1][j-1]) + " " + b[i-1][j-1]
    return matrix
    
def INC(A, i):
    """ Length of increasing subsequence in A ending at A[i] """
    for j in range(i - 1, -1, -1):
        if A[j] < A[i]:
            return 1 + INC(A, j)
    return 1

def DEC(A, i):
    """ Length of decreasing subsequence in A ending at A[i] """
    for j in range(i - 1, -1, -1):
        if A[j] > A[i]:
            return 1 + DEC(A, j)
    return 1

def LIS(A):
    return max([INC(A, i) for i in range(len(A))])

def DIS(A):
    return max([DEC(A, i) for i in range(len(A))])

# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def matrixchainorder(p):
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        m[i][i] = 0
    for l in range(1, n): # l is chain length
        for i in range(0, n-l):
            j = i + l # max is n-(n-1)-1 + n - 1 = n-1 
            m[i][j] = float("inf")
            for k in range(i, j):
                #q = cost/scalar mutliplications
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]: #always the case here
                    m[i][j] = q
                    s[i][j] = k + 1
    return m, s

if __name__ == '__main__':
    y = "10010101"
    x = "010110110"
    c, b = lcs_length(x, y)
    table = put_together(c, b, x, y)
    print_matrix(c)
    print_matrix(b)
    print_matrix(table)
    print INC([7,5,3,9,6,7], 3) # 2
    print DEC([7,5,3,9,6,7], 3) # 1
    print LIS([7,5,3,9,6,2]) # 2
    print DIS([7,5,3,9,6,2]) # 3
    p = [5, 10, 3, 12, 5, 50, 6]
    m, s = matrixchainorder(p)
    print_matrix(m)
    print_matrix(s)
    