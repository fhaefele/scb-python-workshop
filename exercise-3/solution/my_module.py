import time


def sleep_for_some_time(t: float) -> None:
    """
    Pauses execution for a specified amount of time.

    Parameters:
    -----------
    t : float
        The duration (in seconds) for which the program should sleep.

    Returns:
    --------
    None

    Example:
    --------
    >>> sleep_for_some_time(2.5)
    Sleeping for t=2.5 s.
    (Pauses execution for 2.5 seconds)
    """
    print(f"Sleeping for {t=} s.")
    time.sleep(t)


def print_a_word_x_times(word: str, x: int) -> None:
    """
    Prints a given word a specified number of times.

    Parameters:
    -----------
    word : str
        The word to be printed.
    x : int
        The number of times the word should be printed.

    Returns:
    --------
    None

    Example:
    --------
    >>> print_a_word_x_times("Hello", 3)
    Hello
    Hello
    Hello
    """
    for _ in range(x):
        print(word)


def speak_like_master_yoda(text: str) -> str:
    """
    Rearranges words in a sentence to mimic Yoda's speech pattern.

    Parameters:
    -----------
    text : str
        The input sentence.

    Returns:
    --------
    str
        The modified sentence with words reversed in order.

    Example:
    --------
    >>> speak_like_master_yoda("You must learn Python")
    'Python learn must you'
    """
    sp = text.split(" ")[::-1]
    sp[0] = sp[0].capitalize()
    sp[-1] = sp[-1].lower()
    return " ".join(sp)
