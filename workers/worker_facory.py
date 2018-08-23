import abc


class Worker(metaclass=abc.ABCMeta):
    """
    Interface for checking parameters from list
    """
    @abc.abstractclassmethod
    def __init__(self, threshold, directory):
        self.threshold = threshold
        self.directory = directory

    @abc.abstractclassmethod
    def _getinfo(self):
        pass

    @abc.abstractclassmethod
    def check(self):
        pass
