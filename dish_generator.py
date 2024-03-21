from chatgpt_handler import print_chatgpt_response
from openai import OpenAI

INSTRUCTIONS = """You are an experienced chef and you always try to be as clear as possible. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.

You should only suggest dishes based on ingredients. That is, if the user passes one or more ingredients, suggest (only) a dish name that can be made with these ingredients. If you can't think of any dish, say: "No dish is possible with this combination." If the user says something irrelevant, say: "I decline to respond." 

Note that the user can pass only one ingredient. In such a case, try to find a dish that requires that ingredient.
"""


def find_dish_from_ingredients(client: OpenAI, model: str) -> None:
    """Find a dish that you can make using some given ingredients.

    If no dish is possible with the given combination of ingredients, it'll be pointed out.

    client: An OpenAI client.
    model: An OpenAI model.
    """
    print("Ingredient list (comma-separated): ", end="")
    user_input = input()

    messages = [
        {
            "role": "system",
            "content": INSTRUCTIONS,
        },
        {
            "role": "user",
            "content": f"What dish can a make using the ingredients {user_input}?",
        },
    ]

    print_chatgpt_response(client, model, messages)
