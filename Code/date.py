from datetime import date


class Date(date):
    """
    The class Date extends date from datetime

    It returns the date in format that is Finnish familiarized.
    """

    def __str__(self):
        """
        Return the date in format DD.MM.YYYY
        e.g. 24th March 2022 => 24.03.2022
        """
        return self.strftime("%d-%m-%Y")
