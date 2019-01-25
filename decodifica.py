
import numpy
import sounddevice
import scipy.io.wavfile

def complex_to_stereo(data):
    return numpy.array([data.real, data.imag]).T

def stereo_to_complex(data):
    return data[:,0] + 1j*data[:,1]

def mono_to_stereo(data):
    return numpy.array([data, data]).T

def rescale(data):
    return data/numpy.max(numpy.abs(data))

def play(data):
    sampling_frequency = 44100 #Hz
    sounddevice.play(rescale(data), sampling_frequency, blocking=True)

def write_file(path, data):
    data = numpy.int16(rescale(data) * 32767)
    sampling_frequency = 44100 #Hz
    scipy.io.wavfile.write(path, sampling_frequency, data)

# import the file
sampling_frequency, audio = scipy.io.wavfile.read('audio_squalo.wav')

# listen to the file
play(audio)

data = stereo_to_complex(audio)

original_data = ??? # SCRIVI SOLO QUI

original_audio = complex_to_stereo(original_data)

# listen to the original file
play(original_audio)


