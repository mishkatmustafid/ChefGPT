import sys

from openai import OpenAI

from dish_generator import find_dish_from_ingredients
from recipe_critic import give_recipe_feedback
from recipe_generator import generate_recipe_for_dish

MODEL = "gpt-3.5-turbo"

MENU = """
┏┓┓   ┏┏┓┏┓┏┳┓
┃ ┣┓┏┓╋┃┓┃┃ ┃ 
┗┛┛┗┗ ┛┗┛┣┛ ┻ 
1. Get dish from ingredients
2. Get recipe for a dish
3. Get feedback on a recipe
Enter an invalid number to quit.

Choose an option: """


def chef_gpt():
    """A chatbot for our culinary needs."""
    client = OpenAI()
    specialization = sys.argv[1] if len(sys.argv) > 1 else ""

    while True:
        print(MENU, end="")

        choice = int(input())
        print()

        if choice == 1:
            find_dish_from_ingredients(client, MODEL, specialization)
        elif choice == 2:
            generate_recipe_for_dish(client, MODEL, specialization)
        elif choice == 3:
            give_recipe_feedback(client, MODEL, specialization)
        else:
            break


if __name__ == "__main__":
    chef_gpt()
