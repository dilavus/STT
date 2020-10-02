import soundfile as sf
import speech_recognition as sr
import os
import random


# from datetime import datetime, timedelta


def ddhhmmss(seconds):
    """Convert seconds to a time string "[[[DD:]HH:]MM:]SS".
    """
    dhms = ''
    for scale in 86400, 3600, 60:
        result, seconds = divmod(seconds, scale)
        if dhms != '' or result > 0:
            dhms += '{0:02d}:'.format(result)
    dhms += '{0:02d}'.format(seconds)
    return dhms


input_dir = "D:\\projects\\STT"


def convert_mpeg():
    for filename in os.listdir(input_dir):
        actual_filename = filename[:-4]
        if filename.endswith(".mp4"):
            os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}.wav -y'.format(filename, actual_filename))
        else:
            continue


def random_secs_duration():
    num = random.randrange(1, 5 ** 2)
    if num > 20:
        return 20
    else:
        return num


def random_secs(secs):
    # arbitrary number of seconds
    s = secs
    # hours
    hours = s // 3600
    # remaining seconds
    s = s - (hours * 3600)
    # minutes
    minutes = s // 60
    # remaining seconds
    seconds = s - (minutes * 60)
    num = random.randrange(1, 5 ** 2)
    if num > 24:
        num -= 1
    return '{:02}:{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds), int(num))


def transcriber(timestamp):
    print(timestamp)
    r = sr.Recognizer()
    harvard = sr.AudioFile('42.wav')
    f = sf.SoundFile('42.wav')
    all_time = len(f) / f.samplerate
    offset = 0

    while offset < all_time:
        with harvard as source:
            r.adjust_for_ambient_noise(source)
            duration_random = random_secs_duration()
            if duration_random < 5:
                duration_random = 10
            audio = r.record(source, offset=offset, duration=duration_random)

            try:
                recognize = r.recognize_google(audio, language='ru')
                text = '{} {}'.format(random_secs(offset), recognize)
            except Exception:
                text = '{} <...>'.format(random_secs(offset))
            print(text)
            offset += duration_random


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # tcr_time = input("Enter TCR in format(00:00:00:00): ")
    # print(ddhhmmss(5657788))
    convert_mpeg()
    transcriber('00:00:00:00')
    print('End to transcribe')

## TODO   1. To make loop for processing .wav files
## TODO   2. Writing to .txt file
