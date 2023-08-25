def repeatedString(s, n):
    
    if s == 'a':
        return n
    
    tam = len(s)
    qnts_cabem = (int) (n/tam)
    sobraram = abs(n - (qnts_cabem*tam))

    return s.count('a')*qnts_cabem + s[:sobraram].count('a')