import abc
class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass
    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(self,cls,c):
        if cls in MediaLoader:
            attrs = set(dir(c))
            if set(cls.__abstractmethod__) <= attrs:
                return True
        return NotImplemented


        