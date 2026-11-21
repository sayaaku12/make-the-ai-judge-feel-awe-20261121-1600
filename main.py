"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt. The house judge is a
relaxation judge: the text must slow the reader down and settle them,
showing calm through a concrete image rather than instructing it.
"""

import os

def build_text() -> str:
    """Compose the entry text: a slow tide image, plain concrete words."""
    return (
        "The tide comes in over the flat sand, slow as dusk, "
        "and the water finds every hollow and fills it without hurry. "
        "Far out, the light thins to a single line. "
        "Nothing asks anything of you here. "
        "The sea keeps its own time, and for a while, so do you."
    )


def validate_text(text: str) -> str:
    """Gate: 1-280 Unicode code points, UTF-8, not only whitespace."""
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def write_entry(text: str) -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    write_entry(validate_text(build_text()))


if __name__ == "__main__":
    main()
