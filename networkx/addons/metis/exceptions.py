
__all__ = ['MetisError']

class MetisError(Exception):
    """An error type generated from METIS"""
    def __init__(self, rstatus):
        super(MetisError, self).__init__(rstatus)
