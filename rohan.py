# Program to check if the temperature is suitable for light clothes

# Input the current temperature
temperature = float(input("Enter the current temperature in °C: "))

# Decision-making based on the temperature
if temperature >= 22:
    print("The weather is warm! You can wear light and soft clothes comfortably.")
elif 15 <= temperature < 22:
    print("The weather is cool. You can wear light clothes, but consider adding a light jacket.")
else:
    print("It's cold! Avoid light clothes and wear something warmer to stay protected.")

print("Dress wisely and stay comfortable!")
