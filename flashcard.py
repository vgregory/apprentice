# class Flashcard should handle the different flashcards user wants to use. I
# want it to be an abstract class in order to make each subclass handle its own
# data properly, yet leaving to the app to handle them as simple flashcards.
from abc import ABCMeta


class Flashcard(metaclass=ABCMeta):
    """Handle different kinds of flashcards."""
    pass
