
import json
import requests

def dish_fetch(num):
    response = requests.get("https://api-colombia.com/api/v1/TypicalDish")
    dishes = json.loads(response.content)
    
    dish = dishes[num - 1]
    
    return {
        "name": dish["name"],
        "description": dish["description"],
        "ingredients": dish["ingredients"]
    }

def main():
    num = int(input("Ingrese un numero del 1 al 68 para ver nuestra carta : "))
    dish = dish_fetch(num)
    
    print("\nNombre:", dish["name"])
    print("Descripción:", dish["description"])
    print("Ingredientes:", dish["ingredients"])

if __name__ == "__main__":
    main()