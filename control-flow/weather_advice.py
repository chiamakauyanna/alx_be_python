current_weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# match current_weather:
#   case 'sunny':
#     print('Wear a t-shirt and sunglasses.')
#   case 'rainy':
#     print("Don't forget your umbrella and a raincoat.")
#   case 'cold':
#     print("Make sure to wear a warm coat and a scarf.")
#   case _:
#     print("Sorry, I don't have recommendations for this weather.")

if current_weather == 'sunny':
  print('Wear a t-shirt and sunglasses.')
elif current_weather == 'rainy':
  print("Don't forget your umbrella and a raincoat.")
elif current_weather == 'cold':
  print("Make sure to wear a warm coat and a scarf.")
else:
  print("Sorry, I don't have recommendations for this weather.")