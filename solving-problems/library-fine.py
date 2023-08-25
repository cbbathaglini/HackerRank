def libraryFine(d1, m1, y1, d2, m2, y2):
    print(f"d1= {d1} d2 = {d2} m1={m1} m2={m2} y1={y1} y2={y2}")
    if y1 > y2:
        return 10000
    
    if y1 == y2 and  m1 > m2:
        return abs(m2-m1)*500
    
    if y1 == y2 and  m1 == m2 and d1 > d2:
        return abs(d2-d1) * 15
        
    return 0