def viralAdvertising(n):
    shared= 5
    cumulative = shared//2
    if n > 1:
        for i in range(1,n):
            shared = shared//2 * 3
            cumulative += shared//2
                    
    return cumulative