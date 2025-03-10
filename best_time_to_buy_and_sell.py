import random

array_prices = [6,1,3,5,8,3,2] # Simulando que son 7 dias = una semana

def buy_day(array_data, indice):
    while indice < 3 and indice < len(array_data) - 1:
        if array_data[indice] < array_data[indice + 1]:
            buy_day = array_data[indice]
        indice += 1
    return buy_day

def sell_day(array_data, indice):
    major = array_data[indice]
    for price in array_data:
        if price > major:
            major = price
    return major

def profit(buy, sell):
    return sell - buy


    
buy = buy_day(array_prices, 0)
sell = sell_day(array_prices, 0)

total = profit(buy, sell)
print ('buy day: ', buy)
print ('sell day:', sell)
print ('profit', total)

