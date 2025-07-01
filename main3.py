weather = (1,0,0,0,1,1,0)
sunnu = 0
rainy = 0
for i in range(0,7):
    if weather[i] == 0:
        rainy += 1
    else:
        sunnu += 1
    
if sunnu > rainy:
    print("The weather is sunnu")
elif sunnu < rainy:
    print("The weather is rainy")
else:
    print("The weather is uncertain")