class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file formate")

