"""
docstring
"""


class Lala:
    """
    docstring
    """

    def __init__(self, laLa, lola):  # pylint: disable=invalid-name
        self._laLa = laLa  # pylint: disable=invalid-name
        self._lola = lola

    @property
    def laLa(self):  # pylint: disable=invalid-name
        """
        docstring
        """
        print(self._laLa)

    @property
    def lola(self):
        """
        docstring
        """
        print(self.lola)
