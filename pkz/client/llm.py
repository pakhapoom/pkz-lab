from openai import OpenAI
from pkz.client.config import config


def get_typhoon_client() -> OpenAI:
    client = OpenAI(
        base_url=config.TYPHOON_ENDPOINT,
        api_key=config.TYPHOON_API_KEY,
    )
    return client

def generate(
    client: OpenAI,
    user_prompt: str,
    system_prompt: str = None,
    # model: str = "typhoon-v2.5-30b-a3b-instruct",
    model: str = "typhoon-v2.1-12b-instruct",
    **kwargs,
) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        **kwargs,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    client = get_typhoon_client()
    response = generate(
        client=client, 
        user_prompt="Hello, how are you?", 
        system_prompt="You are a helpful assistant.",
        max_tokens=512, 
        temperature=0.1,
    )
    print(response)
