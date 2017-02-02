# class Flashcard should handle the different flashcards user wants to
# use.
import datetime


class Flashcard:
    """Handle different kinds of flashcards.

    This class should not be used directly. Instead, should use its
    children.
    """
    def __init__(self, json_dict=None):
        """Initialize generic flashcard."""
        if json_dict:
            # From given json dictionary
            self._creation_date = datetime.date(
                json_dict['_creation_date']['year'],
                json_dict['_creation_date']['month'],
                json_dict['_creation_date']['day']
            )
            self._last_review = datetime.date(
                json_dict['_last_review']['year'],
                json_dict['_last_review']['month'],
                json_dict['_last_review']['day']
            )
            self._interval = json_dict['_interval']
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
        """Schedule flashcard to a new """
        self._last_review = datetime.date.today()
        self._interval = new_interval

    def to_dict(self):
        """Convert object to a dict useful for json.

        This method should be overwritten by each child of this class.
        """
        class_name = type(self).__name__
        object_dict = {
            "_creation_date": {
                "year": self._creation_date.year,
                "month": self._creation_date.month,
                "day": self._creation_date.day
            },
            "_last_review": {
                "year": self._last_review.year,
                "month": self._last_review.month,
                "day": self._last_review.day
            },
            "_interval": self._interval
        }
        return {class_name: object_dict}
