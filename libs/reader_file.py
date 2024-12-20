from libs.reader import BaseReader
import os
from pydub import AudioSegment
from pydub.utils import audioop
import numpy as np
from hashlib import sha1

class FileReader(BaseReader):
  def __init__(self, filename):
    # super(FileReader, self).__init__(a)
    self.filename = filename

  """
  Reads any file supported by pydub (ffmpeg) and returns the data contained
  within. If file reading fails due to input being a 24-bit wav file,
  wavio is used as a backup.

  Can be optionally limited to a certain amount of seconds from the start
  of the file by specifying the `limit` parameter. This is the amount of
  seconds from the start of the file.

  returns: (channels, samplerate)
  """
  # pydub does not support 24-bit wav files, use wavio when this occurs
  def parse_audio(self, limit=None):  # Add limit parameter
        songname, extension = os.path.splitext(os.path.basename(self.filename))

        try:
            audiofile = AudioSegment.from_file(self.filename)

            if limit is not None:  # Check if limit is provided
                audiofile = audiofile[:limit * 1000]  # Limit to the specified duration in milliseconds

            data = np.frombuffer(audiofile.raw_data, np.int16)

            channels = []
            for chn in range(audiofile.channels):
                channels.append(data[chn::audiofile.channels])

            fs = audiofile.frame_rate
            return {
                "songname": songname,
                "extension": extension,
                "channels": channels,
                "Fs": fs,
                "file_hash": self.parse_file_hash()
            }
        except (audioop.error, Exception) as e:
            print(f"Error parsing audio: {e}")
            return None  # Return None or an empty structure on error

  def parse_file_hash(self, blocksize=2**20):
    """ Small function to generate a hash to uniquely generate
    a file. Inspired by MD5 version here:
    http://stackoverflow.com/a/1131255/712997

    Works with large files.
    """
    s = sha1()

    with open(self.filename , "rb") as f:
      while True:
        buf = f.read(blocksize)
        if not buf: break
        s.update(buf)

    return s.hexdigest().upper()
