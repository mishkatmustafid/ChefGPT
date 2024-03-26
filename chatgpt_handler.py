from openai import OpenAI

MODEL = "gpt-3.5-turbo-instruct"
MAX_TOKENS = 2048


def print_chatgpt_response(client: OpenAI, prompt: str) -> None:
    """Prints ChatGPT response for a set of messages with typewriter effect.

    Args:
        client: An OpenAI client.
        prompt: The user prompt.
    """
    stream = client.completions.create(
        model=MODEL, prompt=prompt, stream=True, max_tokens=MAX_TOKENS
    )

    print("\nChefGPT: ", end="")
    for chunk in stream:
        chunk_message = chunk.choices[0].text or ""
        print(chunk_message, end="")

    print()
