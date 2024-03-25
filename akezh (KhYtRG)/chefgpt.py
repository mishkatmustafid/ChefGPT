from openai import OpenAI

from dish_generator import find_dish_from_ingredients
from recipe_critic import give_recipe_feedback
from recipe_generator import generate_recipe_for_dish

MODEL = "gpt-3.5-turbo"

MENU = """
┏┓┓   ┏┏┓┏┓┏┳┓
┃ ┣┓┏┓╋┃┓┃┃ ┃  (Chinese version)
┗┛┛┗┗ ┛┗┛┣┛ ┻ 
1. Get dish from ingredients
2. Get recipe for a dish
3. Get feedback on a recipe
9. Exit
Enter 9 to quit.

Choose an option: """


def chef_gpt():
    """A chatbot for our culinary needs."""
    client = OpenAI()

    while True:
        print(MENU, end="")

        choice = int(input())
        print()

        if choice == 1:
            find_dish_from_ingredients(client, MODEL)
        elif choice == 2:
            generate_recipe_for_dish(client, MODEL)
        elif choice == 3:
            give_recipe_feedback(client, MODEL)
        elif choice == 9:
            break
        else:
            print("You have not chosen an option, please, enter the number 1-3")
            continue


if __name__ == "__main__":
    chef_gpt()
