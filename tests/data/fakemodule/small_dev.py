"""
A small file documentation
"""


def a_static_function(a_parameter):
    """
    A small static function
    :param a_parameter: A small param
    :return: None
    """
    pass


def a_static_function_typed(a_parameter: int):
    """
    A small static function with arg typed
    :param a_parameter: int typed parameter
    :rtype: None
    """


def a_static_function_which_return(a_parameter):
    """
    A small static function which return int
    :param a_parameter: A small param
     :rtype: int
     :return A value
     """
    return 42


def a_static_function_which_return_type(a_parameter) -> int:
    """
    A small static function which return int
    :param a_parameter: A small param
     :rtype: int
     """
    return 42


def a_static_function_with_args(*args):
    """
     A small static function which *args
    :param args: The args
    :rtype: None
    """


def a_static_function_with_kwargs(**kwargs):
    """
    A small static function which **kwargs
    :param kwargs: The kwargs
    :rtype: None
    """


class ASmallClass:
    """
    A small class
    """

    def __init__(self, an_attribute):
        """
        Constructor of the small class
        :param an_attribute: a small attribute
        """
        self.an_attribute = an_attribute

    def a_function(self, a_parameter):
        """
        A small function of small class
        :param a_parameter: a small parameter
        :rtype: None
        """
        pass

    def a_function_add(self, a, b):
        """
        A small function to add
        :param a: operande a
        :param b: operande b
        :return: the sum of a and b
        """
        return a + b
