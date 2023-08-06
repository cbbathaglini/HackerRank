#https://www.hackerrank.com/challenges/birthday-cake-candles/submissions/code/339046333
def birthdayCakeCandles(candles):
    maior = max(candles)
    frequencia = candles.count(maior)
    return frequencia