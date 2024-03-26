from openai import OpenAI


def print_chatgpt_response(
    client: OpenAI, model: str, messages: list[dict[str, str]]
) -> None:
    """Prints ChatGPT response for a set of messages with typewriter effect.

    Args:
        client: An OpenAI client.
        model: An OpenAI model.
        messages: The context.
    """
    stream = client.chat.completions.create(model=model, messages=messages, stream=True)  # type: ignore

    print("\nChefGPT: ", end="")
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")

    print()
