def T(n):
    if n == 1:
        return 1
    elif n % 3 != 0:
        raise Exception("n should be divisible by 3")
    else:
        return 9*T(n/3) + n*n
    
def subtract_n_digit_numbers(A, B):
    N = len(A)
    if N != len(B):
        raise Exception("A and B must have the same length")
    C = [None for _ in range(N)]
    for i in range(0, N):
        x = A[i] - B[i]
        if x >= 0:
            C[i] = x
        else:
            C[i-1] -= 1 #non-negative result so that works
            C[i] = 10 + x
    return C    

if __name__ == "__main__":
    print T(3)
    print T(9)
    print T(27)
    print T(81)
    print T(243)
    
    A = [2,9,4,3,2]
    B = [1,5,3,7,1]
    C = subtract_n_digit_numbers(A, B)
    print C
