def appendAndDelete(s, t, k):
    print(f"s: {s} | t:  {t}")
    diff_position = -1
    len_final,len_s = len(s), len(s)
    len_t = len(t)
    diff_letters = len_t - len_s
    if len_s > len_t:
        len_final = len_t
        diff_letters = len_s - len_t
    for i in range(len_final):
        if s[i] != t[i]:
            diff_position = i
            break
    
    if diff_position != -1:
        remocao = len(s[i:len_s]) # remocao
        adicao = len(t[i:len_t])
        print(f"remocao: {remocao} | adicao:  {adicao}")
        if k == remocao + adicao:
            return "Yes"
    else:
        print(f" {len_s} == {len_t}")
        print(f" {len_s+1} + {len_t} = {k}")
        if (len_s == len_t) and (len_s+1)+ len_t == k:
            return "Yes"
        if diff_letters != 0:
             remocao = len(s[len_final:len_s]) # remocao
             adicao = len(t[len_final:len_t])
             print(f"2 - remocao: {remocao} | adicao:  {adicao}")
             if k == remocao + adicao:
                return "Yes"
             if (k-(remocao+adicao))%2 == 0:
                return "Yes"
             
    return "No"



def teste1():
    s = "hackerhappy";
    t = "hackerrank";
    k = 9;
    result = appendAndDelete(s, t, k);
    if result == "Yes": return print("OK - Return Yes")

def teste2():
    s = "aba";
    t = "aba";
    k = 7;
    result = appendAndDelete(s, t, k);
    if result == "Yes": return print("OK - Return Yes")

def teste3():
    s = "hackerhappy";
    t = "hackerrappy";
    k = 10;
    result = appendAndDelete(s, t, k);
    if result == "Yes": return print("OK - Return Yes")

def teste4():
    s = "hackerhappy";
    t = "hackerrappy";
    k = 5;
    result = appendAndDelete(s, t, k);
    if result == "No": return print("OK - Return No")

def teste5():
    s = "a";
    t = "ab";
    k = 1;
    result = appendAndDelete(s, t, k);
    if result == "Yes": return print("OK - Return Yes")


def teste6():
    s = "a";
    t = "ab";
    k = 2;
    result = appendAndDelete(s, t, k);
    if result == "No": return print("OK - Return No")


def teste7():
    s = "aaaaaaaaaa";
    t = "aaaaa";
    k = 7;
    result = appendAndDelete(s, t, k);
    if result == "Yes": return print("OK - Return Yes")

def teste8():
    s = "zzzzz";
    t = "zzzzzzz";
    k = 4;
    result = appendAndDelete(s, t, k);
    if result == "Yes": return print("OK - Return Yes")

teste1()
teste2()
teste3()
teste4()
teste5()
teste6()
teste7()
teste8()