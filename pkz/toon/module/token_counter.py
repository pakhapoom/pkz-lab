import tiktoken


class TokenCounter:
    def __init__(self, encoding_name: str = "o200k_base"):
        """
        Initialize a TokenCounter with a specific encoding.
        Please refer to https://platform.openai.com/tokenizer for more details about GPT's tokenizers.

        Args:
            encoding_name: The tiktoken encoding to use. Common options:
                - "o200k_base": Used by GPT-4o, and GPT-4.1
                - "cl100k_base": Used by GPT-4, GPT-3.5-turbo, text-embedding-ada-002
                - "p50k_base": Used by Codex models, text-davinci-002, text-davinci-003
                - "r50k_base": Used by older GPT-3 models (davinci, etc.)
        """
        self.encoding = tiktoken.get_encoding(encoding_name)
        self.encoding_name = encoding_name

    @classmethod
    def for_model(cls, model_name: str) -> "TokenCounter":
        """
        Create a TokenCounter with the appropriate encoding for a specific model.

        Args:
            model_name: The name of the model (e.g., "gpt-4", "gpt-3.5-turbo")

        Returns:
            A TokenCounter instance configured for the specified model
        """
        encoding = tiktoken.encoding_for_model(model_name)
        counter = cls.__new__(cls)
        counter.encoding = encoding
        counter.encoding_name = encoding.name
        return counter

    def count(self, text: str) -> int:
        """
        Count the number of tokens in the given text.

        Args:
            text: The string to count tokens for

        Returns:
            The number of tokens in the text
        """
        return len(self.encoding.encode(text))

    def __call__(self, text: str) -> int:
        """
        Allow the TokenCounter to be called directly as a function.

        Args:
            text: The string to count tokens for

        Returns:
            The number of tokens in the text
        """
        return self.count(text)
