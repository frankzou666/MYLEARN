

import tensorflow as tf
import librosa
import python_speech_features
import matplotlib.pyplot as plt
from scipy.signal.windows import hann, hamming
import numpy  as np


n_mfcc = 22
n_mels = 40
n_fft = 16384
hop_length = 2205
fmin = 0
fmax = None
rate = 44000


def get_chromagram(audio_file):
    y, sr = librosa.load(audio_file, sr=rate)
    winlen=n_fft / sr
    winstep=hop_length/sr
    mfcc_speech = python_speech_features.mfcc(signal=y, samplerate=sr, winlen=winlen, winstep=winstep,
                                          numcep=n_mfcc, nfilt=n_mels, nfft=n_fft, lowfreq=fmin, highfreq=fmax,
                                          preemph=0.0, ceplifter=0, appendEnergy=False, winfunc=hamming)
    return mfcc_speech


def get_next_chromagram(audio_file):
    print('filename %s ' % (audio_file))

    y, sr = librosa.core.load(audio_file)
    chroma_stft = librosa.feature.chroma_stft(y=y, hop_length=hop_length, n_fft=n_fft)

    return chroma_stft


def extract_feature_vector(chroma_data):
    num_features, num_samples = np.shape(chroma_data)

    print("Num features %d num samples %d " % (num_features, num_samples))

    freq_vals = tf.argmax(chroma_data)
    hist, bins = np.histogram(freq_vals, bins=range(num_features + 1))

    return hist.astype(float) / num_samples


def read_file(file):
    file_contents = tf.io.read_file(file)
    return file, file_contents




def main():
    filename = tf.io.match_filenames_once('C:\\1\\wav\\*.wav')
    filenameds = tf.data.Dataset.from_tensor_slices(filename)
    filenamecontent = filenameds.map(read_file)
    for file, file_contents in filenamecontent.take(2):
        print("filename %s " % (file_contents))

    def get_dataset():
        filename_contents_ds_enum = filenameds.enumerate()

        xs = []
        for file_obj in filename_contents_ds_enum.as_numpy_iterator():
            chroma_data = get_next_chromagram(file_obj[1][0])

            x = [extract_feature_vector(chroma_data)]
            x = np.matrix(x)

            if len(xs) == 0:
                xs = x
            else:
                xs = np.vstack((xs, x))

        return xs

    X = get_dataset()
    print(X)
    print(X.shape)

def main3():
    y = get_chromagram('C:\\1\\wav\\Alarm05.wav')
    print(y)


if __name__ == '__main__':
    main()