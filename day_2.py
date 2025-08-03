# Продемонстрированы строки, числа, логика.

# 💡 Улучшить:

# Сделай больше практики: операции со строками (split(), replace(), join())

# Добавь примеры преобразования типов (int("42"), str(123) и т.д.)

def stSplit(text: str, split: str) -> list:
    result = text.split(split)
    return result

def streplace(text: str, oldText: str, newText:str) -> str:
    result = text.replace(oldText,newText)
    return result

def stjoin(text: str,stJoin:str):
    result = text.join(stJoin)
    return result

# print (stSplit("Строка, для, разбивки","ъ"))

# print (streplace("Строка для","Строка", "Новая строка"))

# print(stjoin("","Строка"))