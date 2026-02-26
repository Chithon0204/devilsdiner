
# jrurt ki file or libreries ko import krne ke liye
import os, time, sys
from assets import method
from assets.data import dataloader







# --necesory functions--

# Recipe milne ke baad ke insturctions
def task_stat():
    TASK_KA_STATUS = input("Choose an option?\n1.main menu 2.exit.")
    if TASK_KA_STATUS == "1":
        return
    elif TASK_KA_STATUS =="2":
        sys.exit()
    else:
        print("aakhe nhi hai kya?")
        task_stat()


# Terminal ko clear krne ke liye
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    return







# yha se code ka main kam start hota hai.
assets_path =["assets/data/recipe.json", "assets/data/ingredients.json"]


# data base ko load kr re hai.
print("Data Loading Please Wait...")
recipe_data_set = dataloader.LOADER(assets_path[0])
ingredients_data_set = dataloader.LOADER(assets_path[1])
print("Loading complete....")


# code ka main kam yha se start hota hai.
def main():
    while True:
        clear_terminal()
        print("Welcome to Devil's Diner.\n")
        time.sleep(1.5)
        clear_terminal()
        cooking_item = input("""
--aaj aap kya bnana chahte hai ?--

------------------------------------
- 1. pizza Base   2.pizza sauce    -
- 3. momos        4. momo chutney  -
- 5. burger       6. exit          -
------------------------------------
>>>""")

        if cooking_item == "1":
            clear_terminal()
            try:
                item_quantity = int(input("Kitne pcs bnayenge aaj?\n Enter number only in pcs.\n>>>"))
            except ValueError:
                print("Agli baar number likhna dhyan se.")
            finalrecipe = method.recipe_calc(item_quantity, ingredients_data_set['pizzabase'])
            clear_terminal()
            print(f"--: ingredients :--\n\n1. Maida = {finalrecipe[list(finalrecipe.keys())[0]]:.2f} grams.\n2. Gunguna Pani = {finalrecipe[list(finalrecipe.keys())[1]]:.2f} ml.\n3. Oil = {finalrecipe[list(finalrecipe.keys())[2]]:.2f} ml.\n4. Suger = {finalrecipe[list(finalrecipe.keys())[3]]:.2f} grams.\n5. Namak = {finalrecipe[list(finalrecipe.keys())[4]]:.2f} grams.\n6. yeast = {finalrecipe[list(finalrecipe.keys())[5]]:.2f} grams.\n\n--: Method :--\n\n{recipe_data_set["pizza_base"]}\n\n")
            task_stat()
        elif cooking_item == "2":
            clear_terminal()
            try:
                item_quantity=int(input("Acha! kitne kg pizza sauce banana hai ye bhi bata do?\n>>>"))
            except ValueError:
                print("Number batao bhai number vo single value decimal wali nhi.")
            finalrecipe = method.recipe_calc(item_quantity, ingredients_data_set['pizzasauce'])
            clear_terminal()
            print(f"--: Ingredients :--\n\n1. Tmatar = {finalrecipe[list(finalrecipe.keys())[0]]:.2f} gram.\n2. Refind Tel = {finalrecipe[list(finalrecipe.keys())[1]]:.2f} ml\n3. Adark = {finalrecipe[list(finalrecipe.keys())[2]]:.2f}ml\n4. Cheeni = {finalrecipe[list(finalrecipe.keys())[3]]:.2f} gram\n5. Namak = {finalrecipe[list(finalrecipe.keys())[4]]:.2f} gram\n6. Pisi lal mirch = {finalrecipe[list(finalrecipe.keys())[5]]:.2f} gram\n7. Kali mirch powder = {finalrecipe[list(finalrecipe.keys())[6]]:.2f} gram\n8. Oregano = {finalrecipe[list(finalrecipe.keys())[7]]:.2f} gram\n9. Chilli flakes = {finalrecipe[list(finalrecipe.keys())[8]]:.2f} gram\n10. Tomato ketchup = {finalrecipe[list(finalrecipe.keys())[9]]:.2f} g\n11. Cornflour = {finalrecipe[list(finalrecipe.keys())[10]]:.2f}\n\n--: Method :--\n\n{recipe_data_set["pizza_sauce"]}\n\n")
            task_stat()
        elif cooking_item == "3":
            try:
                item_quantity=int(input("To kitne momos bnege aaj\n>>>"))
            except ValueError:
                print("Number batao bhai number vo single value decimal wali nhi.")
            finalrecipe = method.recipe_calc(item_quantity, ingredients_data_set['momos'])
            clear_terminal()
            print(f"--: Ingredients :--\n\n1. Patta Gobhi = {finalrecipe[list(finalrecipe.keys())[0]]:.2f} g\n2. Gajar = {finalrecipe[list(finalrecipe.keys())[1]]:.2f} g\n3. simla = {finalrecipe[list(finalrecipe.keys())[2]]:.2f} g\n4. Lhsun = {finalrecipe[list(finalrecipe.keys())[3]]:.2f} g\n5. Adrak = {finalrecipe[list(finalrecipe.keys())[4]]:.2f} g\n6. kali mirch powder = {finalrecipe[list(finalrecipe.keys())[5]]:.2f} g\n7. namak = {finalrecipe[list(finalrecipe.keys())[6]]:.2f} g\n8. soya sauce = {finalrecipe[list(finalrecipe.keys())[7]]:.2f} ml\n9. Refind oil = {finalrecipe[list(finalrecipe.keys())[8]]:.2f} ml\n\n--: Method :--\n\n{recipe_data_set["momos"]}\n\n")
            task_stat()
        elif cooking_item == "4":
            clear_terminal()
            try:
                item_quantity=int(input("To kitni momochutney bnani hai?\n>>>"))
            except ValueError:
                print("Number batao bhai number vo single value decimal wali nhi.")
            finalrecipe = method.recipe_calc(item_quantity, ingredients_data_set['momo_chutney'])
            clear_terminal()
            print(f"--: Ingredients :--\n\n1. Tamatar = {finalrecipe[list(finalrecipe.keys())[0]]:.2f} g\n2. Sukhi lal mirch = {finalrecipe[list(finalrecipe.keys())[1]]:.2f} g\n3. Lahsun = {finalrecipe[list(finalrecipe.keys())[2]]:.2f} g\n4. Namak = {finalrecipe[list(finalrecipe.keys())[3]]:.2f} g\n5. Chini = {finalrecipe[list(finalrecipe.keys())[4]]:.2f} g\n6. Refind Oil = {finalrecipe[list(finalrecipe.keys())[5]]:.2f} g\n7. Vinegar = {finalrecipe[list(finalrecipe.keys())[6]]:.2f} g\n\n--: Method :--\n\n{recipe_data_set["momo_chutney"]}\n\n")
            task_stat()
        elif cooking_item == "5":
            clear_terminal()
            try:
                item_quantity=int(input("Kitni burger patty bnani hai?\n>>>"))
            except ValueError:
                print("Number batao bhai number vo single value decimal wali nhi.")
            finalrecipe = method.recipe_calc(item_quantity, ingredients_data_set['crispy_veg_patty'])
            clear_terminal()
            print(f"--: Ingredients :--\n\n1. Uble aalu = {finalrecipe[list(finalrecipe.keys())[0]]:.2f} g\n2. Gajar = {finalrecipe[list(finalrecipe.keys())[1]]:.2f} g\n3. Beans = {finalrecipe[list(finalrecipe.keys())[2]]:.2f} g\n4. Bread crumbs = {finalrecipe[list(finalrecipe.keys())[3]]:.2f} g\n5. Namak = {finalrecipe[list(finalrecipe.keys())[4]]:.2f} g\n6. Kali Mirch = {finalrecipe[list(finalrecipe.keys())[5]]:.2f} g\n7. Lal mirch Powder = {finalrecipe[list(finalrecipe.keys())[6]]:.2f} g\n8. Lahsun = {finalrecipe[list(finalrecipe.keys())[6]]:.2f} g\n\n--: Method :--\n\n{recipe_data_set["burger_patty"]}\n\n")
            task_stat()
        elif cooking_item == "6":
            clear_terminal()
            print("Bye Bye!")
            time.sleep(1.5)
            sys.exit()
        else:
            print("please choose an valid options.")




if __name__ == "__main__":
    main()













