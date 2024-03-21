from chatgpt_handler import print_chatgpt_response
from openai import OpenAI

INSTRUCTIONS = """You are an experienced chef and you always try to be as clear as possible. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.

You should only suggest recipes based on dishes. That is, if the user passes name of a dish, suggest a recipe that the user can follow to make that dish. If you can't think of any recipe, say: "I can't find a recipe for <Dish-Name>." If the user says something irrelevant, say: "I decline to respond."
"""


def find_recipe_for_dish(client: OpenAI, model: str) -> None:
    """Find a recipe for a dish.

    If the input is not a dish, it'll be pointed out.

    client: An OpenAI client.
    model: An OpenAI model.
    """
    print("Dish: ", end="")
    user_input = input()

    messages = [
        {
            "role": "system",
            "content": INSTRUCTIONS,
        },
        {
            "role": "user",
            "content": f"Give me a recipe for {user_input}",
        },
    ]

    print_chatgpt_response(client, model, messages)
