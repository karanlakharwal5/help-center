# simple_utils.py - A utility library


def reverse_string(text: str) -> str:
    """Reverse the characters in a string.

    Args:
        text: The input string to reverse.

    Returns:
        The reversed string.
    """
    return text[::-1]


def count_words(sentence: str) -> int:
    """Count the number of words in a sentence.

    Words are delimited by whitespace. Returns 0 for an empty string.

    Args:
        sentence: The input sentence.

    Returns:
        The number of words.
    """
    if not sentence.strip():
        return 0
    return len(sentence.split())


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        Temperature in degrees Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def calculate_average(numbers: list[float]) -> float:
    """Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers: A list of numeric values.

    Returns:
        The average of the provided numbers.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")
    return sum(numbers) / len(numbers)


def parse_user_input(data: str) -> dict:
    """Parse a comma-delimited string into a user info dictionary.

    Expected format: ``name,age,email``

    Args:
        data: A comma-separated string with name, age, and email fields.

    Returns:
        A dictionary with keys ``name`` (str), ``age`` (int), and ``email`` (str).

    Raises:
        ValueError: If the input does not contain at least three comma-separated
            fields or if the age field cannot be converted to an integer.
    """
    parts = data.split(",")
    if len(parts) < 3:
        raise ValueError(
            f"Expected at least 3 comma-separated fields, got {len(parts)}."
        )
    try:
        age = int(parts[1].strip())
    except ValueError as exc:
        raise ValueError(
            f"Age field '{parts[1].strip()}' is not a valid integer."
        ) from exc
    return {"name": parts[0].strip(), "age": age, "email": parts[2].strip()}


class DataProcessor:
    """Manage and transform a collection of numeric items."""

    def __init__(self) -> None:
        """Initialise the processor with an empty item list."""
        self.data: list = []

    def add(self, item) -> None:
        """Append an item to the internal data list.

        Args:
            item: The item to add.
        """
        self.data.append(item)

    def process(self) -> list:
        """Return a new list with each stored item multiplied by 2.

        Returns:
            A list of each element doubled.
        """
        return [item * 2 for item in self.data]
