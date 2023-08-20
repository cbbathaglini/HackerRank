#TIME LIMIT
def climbingLeaderboard(ranked, player):
    ranked_without_duplicate = []
    arr_results = []
    first = True
    for p in range(len(player)):
        maior = -1
        for r in range(len(ranked)):
            if first and ranked[r] not in ranked_without_duplicate: 
                ranked_without_duplicate.append(ranked[r])
            if player[p] >= ranked[r]:
                maior = ranked[r]
                break
            
        first = False
        if maior == -1:
            arr_results.append(len(ranked_without_duplicate)+1)
            
        if maior in ranked_without_duplicate:
            arr_results.append(ranked_without_duplicate.index(maior)+1)
        
    print(f"ranked_without_duplicate: {ranked_without_duplicate}")

    return arr_results