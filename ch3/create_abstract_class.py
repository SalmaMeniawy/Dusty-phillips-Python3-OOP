import abc
class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass
    @abc.abstractproperty
    def ext(self):
        pass
    
        