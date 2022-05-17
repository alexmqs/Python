# 14
# Escreva um programa que converta uma temperatura digitada em °C par °F.

tempCelsius = float(input('Digite a temperatura: '))
tempFahrenheit = ((9 * tempCelsius) / 5) + 32

print(f'A temperatura de {tempCelsius}°C corresponde a {tempFahrenheit}°F.')
