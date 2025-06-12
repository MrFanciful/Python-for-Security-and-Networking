from optparse import OptionParser

class Parameters:
    """Global parameters"""
    def __init__(self, **kwargs):
        self.param1 = kwargs.get('param1')
        self.param2 = kwargs.get('param2')

def view_parameters(input_parameters):
    print(input_parameters.param1)
    print(input_parameters.param2)

parser = OptionParser()