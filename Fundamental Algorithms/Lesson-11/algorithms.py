def division_ring(a, b, Z_length):
    """ Performs the division of a/b in the ring Z of length Z_length    
    """
    for x in range(Z_length):
        if (b * x) % Z_length == a:
            return x
    return None

if __name__ == '__main__':
    print division_ring(211, 507, 1000)
    s = set()
    i = 1
    while i < 100000:
        x = pow(2,i) % 1000
        print "\\\ $2^"+str(i)+" = "+str(x)+" \\bmod{1000}$"
        if x in s:
            print "FOUND"
        s.add(x)
        i *= 2
        
        
    
    
    
    
    