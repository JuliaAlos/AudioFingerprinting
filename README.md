# Fingerprint audio files & identify what's playing

```bash
sudo apt-get install python-tk

sudo apt install ffmpeg

sudo apt-get install portaudio19-dev python3-pyaudio

pip install matplotlib termcolor scipy pydub PyAudio
```

## How to set up 

1. Run `$ make clean reset` to clean & init database struct
1. Run `$ make tests` to make sure that everything is properly configurated
1. Copy some `.mp3` audio files into `mp3/` directory
1. Run `$ make fingerprint-songs` to analyze audio files & fill your db with hashes
1. Start play any of audio file (from any source) from `mp3/` directory, and run (parallely) `$ make recognize-listen seconds=5`

## Generate MP3 files fingerprints
```bash
python collect-fingerprints-of-songs.py
```
```bash
python get-database-stat.py
```
## Recognizing audio from microphone
```bash
python recognize-from-microphone.py -s 5
```


## Thanks to
- [How does Shazam work](http://coding-geek.com/how-shazam-works/)
- [Audio fingerprinting and recognition in Python](https://github.com/worldveil/dejavu) - thanks for fingerprinting login via pynum
- [Audio Fingerprinting with Python and Numpy](http://willdrevo.com/fingerprinting-and-audio-recognition-with-python/)
- [Shazam It! Music Recognition Algorithms, Fingerprinting, and Processing](https://www.toptal.com/algorithms/shazam-it-music-processing-fingerprinting-and-recognition)
- [Creating Shazam in Java](http://royvanrijn.com/blog/2010/06/creating-shazam-in-java/)
