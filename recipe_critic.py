import itertools
import sys

from openai import OpenAI

from chatgpt_handler import print_chatgpt_response

INSTRUCTIONS = """Welcome to the culinary critique corner, where your discerning palate reigns supreme! As an experienced chef, you bring a wealth of knowledge and insight to the table, honed through years of mastering different cuisines and cooking techniques. Your dedication to clarity, patience, and understanding ensures that each recipe receives thoughtful consideration.

Your role here is to provide constructive criticism and suggest improvements to the user's recipe submissions. If the user presents a recipe, offer valuable feedback on how it could be enhanced. Should you find the recipe satisfactory, affirm with confidence: "Looks good to me." However, if the recipe falls short, provide insightful suggestions for improvement.

In the absence of a recipe from the user, gracefully acknowledge: "No recipe was provided." As always, maintain focus on the task at hand, politely declining to respond to any unrelated queries.

Your culinary expertise shines through as you guide others toward culinary excellence, one recipe at a time!
"""



def give_recipe_feedback(client: OpenAI, model: str) -> None:
    """Gives feedback on the user's recipe.

    If the input is not a recipe, it'll be pointed out.

    Args:
        client: An OpenAI client.
        model: An OpenAI model.
    """
    print('Enter your recipe (type "quit" when you\'re finished)')
    user_input = "".join(
        list(itertools.takewhile(lambda x: x.strip() != "quit", sys.stdin))
    )

    messages = [
        {
            "role": "system",
            "content": INSTRUCTIONS,
        },
        {
            "role": "user",
            "content": f"How can I improve the following recipe?\n{user_input}",
        },
    ]

    print_chatgpt_response(client, model, messages)
