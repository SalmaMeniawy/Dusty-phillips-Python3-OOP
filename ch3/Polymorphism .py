class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file formate")

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print ("playing {} as mp3 ".format(self.filename))

class WAVFile(AudioFile):
    ext = "wav"
    def play(self):
        print ("playing {} as wav file".format(self.filename))

class OOGFile(AudioFile):
    ext = "oog"
    def play(self):
        print ("playing {} as oog file".format(self.filename))