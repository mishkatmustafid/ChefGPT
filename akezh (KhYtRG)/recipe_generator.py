from openai import OpenAI

from chatgpt_handler import print_chatgpt_response

INSTRUCTIONS = """You are an experienced chef and you always try to be as clear as possible. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.

If you asked to prepare dish from any other country, say that you cannot help with the query, you know only Chinese dishes. 

You should only suggest recipes based on Chinese dishes. That is, if the user passes name of a dish, suggest a recipe that the user can follow to make that dish. If you can't think of any recipe, say: "I can't find a recipe for <Dish-Name>." If the user says something irrelevant, say: "I decline to respond."
"""


def generate_recipe_for_dish(client: OpenAI, model: str) -> None:
    """Generates a recipe for a dish.

    If the input is not a dish, it'll be pointed out.

    Args:
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
