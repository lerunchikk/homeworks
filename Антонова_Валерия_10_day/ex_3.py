text = "functional programming"
result = {symbol:text.count(symbol) for symbol in text if symbol != " " }
print(result)