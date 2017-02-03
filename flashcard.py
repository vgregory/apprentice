# class Flashcard should handle the different flashcards user wants to
# use.
import datetime


class Flashcard:
    """Handle different kinds of flashcards.

    This class should not be used directly. Instead, should use its
    children.
    """
    def __init__(self, dictionary=None):
        """Initialize generic flashcard."""
        if dictionary:
            # From dictionary
            self._creation_date = Flashcard.dict_to_date(
                dictionary['_creation_date'])
            self._last_review = Flashcard.dict_to_date(
                dictionary['_last_review'])
            self._interval = dictionary['_interval']
        else:
            # From scratch
            self._creation_date = datetime.date.today()
            self._last_review = datetime.date.today()
            self._interval = 0

    @property
    def date_created(self):
        """Defined as property so to avoid unwanted change."""
        return self._creation_date

    @property
    def due_to_date(self):
        """Return date of next review.

        Flashcards not reviewed in due time are always set for today.
        """
        timedelta = datetime.timedelta(self._interval)
        if self._last_review + timedelta <= datetime.date.today():
            return datetime.date.today()
        else:
            return self._last_review + timedelta

    def schedule(self, new_interval):
        """Schedule flashcard to a new date."""
        self._last_review = datetime.date.today()
        self._interval = new_interval

    def to_dict(self):
        """Convert object to a dict useful for json.

        This method should be overwritten by each child of this class.
        """
        object_dict = {
            "_creation_date": Flashcard.date_to_dict(self._creation_date),
            "_last_review": Flashcard.date_to_dict(self._last_review),
            "_interval": self._interval
        }
        return object_dict

    @staticmethod
    def date_to_dict(date):
        """ Convert datetime.date object to a dictionary."""
        dictionary = {
            "year": date.year,
            "month": date.month,
            "day": date.month
        }
        return dictionary

    @staticmethod
    def dict_to_date(dictionary):
        """Convert a dictionary to datetime.date object."""
        date = datetime.date(
            dictionary['year'],
            dictionary['month'],
            dictionary['day']
        )
        return date
