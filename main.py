def reversString (words: str) -> None:
    print(words[::-1] )

def temperature(t:int, typeOfTemr: str)->int:
    result = 0
    if typeOfTemr == "F":
        result = (t * 1.8) + 32
    elif typeOfTemr == "C":
        result = (t - 32) / 1.8
    else:
        raise "Не верно задан параметр"
    return result

def calculator(a: int, b: int, c:int)-> int:
    if c == 0:
        result= a + b
    elif c == 1:
        result = a* b
    elif c == 2:
        result = a // b
    else:
        raise "Не выбра параметр операции"

    return result
