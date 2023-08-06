
def ano_eh_bissexto(year,eh_bissexto):
    if not eh_bissexto:
        return "13.09."+str(year)
    
    return "12.09."+str(year)


def dayOfProgrammer(year):
    ehBissexto = False
    if year == 1918:
        return "26.09.1918"
    
    if year < 1918:
        if year %4 == 0:
            ehBissexto = True
    elif year > 1918:    
        if (year%4==0 and year%100!=0) or (year%400==0):
                ehBissexto = True

    return ano_eh_bissexto(year, ehBissexto)
        

year = 2016
result = dayOfProgrammer(year)
print(f"Result: {result}")
