fruits = ["Apple","kiwi","pineapple"]
vegetables = ["tomato","carrot","cabbage"]
beverages = ["cola","mirinda","thumbsup"]

fruits.append ("orange")
print(fruits)

vegetables.insert (1,"beetroot")
print(vegetables)

beverages.remove ("thumbsup")
print (beverages)

inventory = [fruits, vegetables,beverages]
print(inventory)

print(fruits[0:2])

print(vegetables[-1])

fruits_lengths = [len(fruit) for fruit in fruits]
print (fruits_lengths)

if "water" in beverages:

    print ("yes, 'water' is in the beverages list")

else:
    print("No, 'water' is not in the beverages list")   
    

tuple_list = (fruits[0], vegetables[0], beverages[0]) 
print(tuple_list) 