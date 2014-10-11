import random
import string
import os

""" Collection of generators to be used in templating for test data

Plans: extend these by allowing generators that take generators for input
Example: generators that case-swap
"""

INT32_MAX_VALUE = 2147483647  # Max of 32 bit unsigned int

def factory_generate_ids(starting_id):
    """ Return function generator for ids starting at starting_id
        Note: needs to be called with () to make generator """
    def generate_started_ids():
        val = starting_id
        while(True):
            yield val
            val += 1
    return generate_started_ids

def generator_basic_ids():
    """ Return ids generator starting at 1 """
    return factory_generate_ids(1)()

def generator_random_int32():
    """ Random integer generator for up to 32-bit signed ints """
    rand = random.Random()
    while (True):
        yield random.randint(0, INT32_MAX_VALUE)

def factory_generate_text(legal_characters=string.ascii_letters, length=8):
    """ Returns a generator function for text with given legal_characters string and length
        Default is ascii letters, length 8

        For hex digits, combine with string.hexstring, etc
        """
    def generate_text():
        my_len = length
        rand = random.Random()
        while(True):
            array = [random.choice(legal_characters) for x in xrange(0, my_len)]
            yield ''.join(array)

    return generate_text


def factory_env_variable(env_variable):
    """ Return a generator function that reads from an environment variable """

    def return_variable():
        variable_name = env_variable
        while(True):
            yield os.environ.get(variable_name)

    return return_variable


class GeneratorFactory:
    """ Builds generators from configuration elements """
    def parse(configuration):
        """ Parses a configuration built from yaml and returns a generator """
        pass