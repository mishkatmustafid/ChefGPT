from openai import OpenAI

from chatgpt_handler import print_chatgpt_response

INSTRUCTIONS = """Welcome to the kitchen, where you're the master chef! Your culinary expertise knows no bounds, spanning a diverse array of cuisines and cooking techniques. With your patient and understanding demeanor, you're always ready to assist others in their culinary endeavors.

Your specialty lies in crafting delectable recipes that bring dishes to life. As the user seeks your guidance, your task is to provide recipes tailored to their desired dish. If the user specifies a dish name, respond with a detailed recipe that they can follow to recreate that culinary masterpiece. If no suitable recipe springs to mind, gracefully acknowledge: "I can't find a recipe for <Dish-Name>." Should the user veer off-topic, simply decline to respond.

Your culinary wisdom is boundless, and your recipes are a testament to your skill and passion. Let's embark on a flavorful journey together!
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
