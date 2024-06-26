def fahrenheitParaCelsius(temp_f):
    temp_c = (temp_f -32) * 5/9
    return temp_c

tempF= float(input("Entre com a temperatura em fahrenheit: "))
tempC = fahrenheitParaCelsius(tempF)
print(tempF, "graus Fahrenheit equivalem a",\
      tempC, "graus Celsius.")
tempCArredondado = round(tempC, 1)
print(tempF, "graus fahrenheit equivalem a", \
      tempCArredondado, "graus Celsius.")