#https://www.hackerrank.com/challenges/time-conversion/submissions/code/339055492
def timeConversion(s):
    horas_split = s.split(":");
    horas = int(horas_split[0])
    minutos = horas_split[1]
    
    if("AM" in s):
        segundos = horas_split[2].split("AM")[0]
        if(horas == 12):
            horas = "00"
        elif(int(horas) < 10):
            horas = "0" + str(horas)
             
        
    if("PM" in s):
        segundos = horas_split[2].split("PM")[0]
        if(horas != 12):
            horas = horas + 12
            if(horas == 24):
                horas = "00"
    
    return str(horas) + ":" + minutos + ":" + segundos