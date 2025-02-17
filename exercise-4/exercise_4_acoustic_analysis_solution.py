import wave
from pathlib import Path

import matplotlib.pyplot as plt  # pip install PyQt6
import numpy as np
import scipy.fft
import scipy.io
import scipy.signal
import sounddevice as sd
import soundfile as sf

# %% Find all files in a directory and add them to a list
search_dir = "/path/to/find_the_wavs"
if not Path(search_dir).is_dir():
    raise ValueError(f"Can't find the {search_dir=}!")

p = Path(search_dir).rglob("*.wav")  # same as p = Path(search_dir).glob('**/*wav')
wavs = [x for x in p]

# %% sort the list in-place by the using a lambda function.
# the lambda function returns the filename as the sorting key.
# only works because each entry is a Path object
# which has properties according to:
# https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name
wavs.sort(key=lambda x: x.name)

# print all files to the terminal in sorted order
for idx, val in enumerate(wavs):
    print(f"{idx:02}: {val}")

# %% read the 5th audio file
fs, rec_scipy = scipy.io.wavfile.read(wavs[4])
rec_sf, _ = sf.read(wavs[4])

# %% Extract fs, nchannels, nsamples, duration, bit depth
ainfo = sf.info(wavs[4])
print(f"fs : {ainfo.samplerate}")
print(f"nchannels : {ainfo.channels}")
print(f"nsamples : {rec_sf.shape[0]}")
print(f"duration : {ainfo.duration}")
print(f"bit depth : {ainfo.subtype_info} aka 16-bits")

# now you can get the same information using the built-in module wave
with wave.open(str(wavs[4]), "rb") as w:
    ainfo_wave = w.getparams()
print(f"fs : {ainfo_wave.framerate}")
print(f"nchannels : {ainfo_wave.nchannels}")
print(f"nsamples : {ainfo_wave.nframes}")
print(f"duration : {float(ainfo_wave.nframes) / float(ainfo_wave.framerate)}")
print(f"bit depth : {ainfo_wave.sampwidth * 8} aka 16-bits")

# you can also get the same information from the scipy module
print(f"fs : {fs}")
print(f"nchannels : {'1' if rec_scipy.ndim == 1 else f'{rec_scipy.shape[1]}'}")
print(f"nsamples : {rec_scipy.shape[0]}")
print(f"duration : {float(rec_scipy.shape[0]) / fs}")
print(f"bit depth : {rec_scipy.dtype} aka 16-bits")


# %% what is the difference between sf.read() and scipy.io.wavfile.read()?
print("soundfile | scipy")
print(f"vectors : {rec_scipy[:5]=} | {rec_sf[:5]=}")
print(f"type : {rec_scipy.dtype=} | {rec_sf.dtype=}")
# Scipy reads the vector natively, meaning in 16-bit signed integers
# whereas soundfile scales it to +/-1.
# we can get the same if we scale scipy or soundfile
print(f"{np.sum(rec_sf-rec_scipy.astype(float)/2**15)=}")

# lets play the sound file.
sd.play(rec_sf, fs)
sd.wait()  # blocks the interpreter until finished playing

# %% Which recording has most channels and which is the longest?
nch = []
dur = []
for x in wavs:
    a = sf.info(x)
    nch.append(a.channels)
    dur.append(a.duration)

print(f"Most channels (n = {max(nch)}) in {wavs[np.argmax(nch)]}")
print(f"Longest recording (dur = {max(dur)}) in {wavs[np.argmax(dur)]}")


# %% so from now on we work on the rec #5
# and for plotting we utilize matplotlib
rec = rec_sf

t = np.linspace(0.0, float(rec_scipy.shape[0]) / fs, rec.shape[0])

# plot the oscillogram
plt.figure(1)
plt.clf()
plt.plot(t, rec)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

# %% Lets select one segment from the call using ginput
# if you are using inline plots run %matplotlib qt before in your console
# plt.figure(1)
# plt.clf()
# plt.plot(rec)
# tmp_x,tmp_y = plt.ginput(2) # we use this to select our interval.
# print(tmp_x,tmp_y)
# print(f"start sample : {round(tmp_x[0])}") # remember to convert to samples
# print(f"stop sample : {round(tmp_y[1])}")
# you can now move back to inline plots with %matplotlib inline

# %% we use these values to continue
# start :  59569
# stop : 68782
call = rec[59569:68782]
t_call = np.linspace(0.0, float(call.shape[0]) / fs, call.shape[0])

# %% lets compute the 95% energy
csig = np.cumsum(call**2)
csig = csig / np.max(csig)
idx_95energy = (csig > 0.025) & (csig < 0.975)

# make a combined figure to show the segment including the energy window
plt.figure(2)
plt.clf()
plt.subplot(3, 1, 1)
plt.plot(t_call, call, label="segment")
plt.ylabel("Amplitude")
xt = plt.xticks()
plt.xticks(xt[0], labels=[])
plt.xlim([t_call[0], t_call[-1]])
plt.subplot(3, 1, 2)
plt.plot(t_call, csig)
plt.plot(t_call[idx_95energy], csig[idx_95energy])
plt.hlines([0.025, 0.975], xmin=t_call[0], xmax=t_call[-1], colors="r", linewidth=0.5)
plt.xticks(xt[0], labels=[])
plt.xlim([t_call[0], t_call[-1]])
plt.subplot(3, 1, 3)
plt.plot(t_call, call[:], label="segment")
plt.plot(t_call[idx_95energy], call[idx_95energy], label=r"95% energy")
plt.legend(loc="upper right")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.xlim([t_call[0], t_call[-1]])
plt.show()

# %% [optinal]: extract parameters from time domain
p0 = 20e-6
p_peak = 20 * np.log10(np.max(call) / p0)
p_peak2peak = 20 * np.log10((np.max(call) - np.min(call)) / p0)
p_rms = 20 * np.log10(np.sqrt(np.mean(call[idx_95energy] ** 2)) / p0)
energy = p_rms + 10 * np.log10(len(call[idx_95energy]) / fs)
print(f"{p_peak=}")
print(f"{p_peak2peak=}")
print(f"{p_rms=}")
print(f"{energy=}")


# %% Transform the signal into the frequency domain
# FFT
nfft = call.shape[0]
call_fft = scipy.fft.fft(call, nfft)[: nfft // 2]
fx = scipy.fft.fftfreq(nfft, 1 / fs)[: nfft // 2]
# ^its not exactly same with np.linspace but also works
call_fft = 20 * np.log10(2 / nfft * np.abs(call_fft)) - 10 * np.log10(
    fs / nfft
)  # scale properly to [dB/Hz]

# PSD welch
fxx, Pxx = scipy.signal.welch(
    call,
    fs,
    window=np.hanning(256),
    noverlap=128,
    nfft=nfft,
    detrend=False,
    return_onesided=True,
)
Pxx = 10 * np.log10(Pxx)  # scale for dB/Hz

plt.figure(3)
plt.clf()
plt.plot(fx / 1e3, call_fft, label="FFT")
plt.plot(fxx / 1e3, Pxx, label="PSD welch")
plt.xlabel("frequency [kHz]")
plt.ylabel("Amplitude [dB/Hz]")
plt.grid()
plt.show()

# %% [optinal]: extract parameters from frequency domain
f_peak = fxx[np.argwhere(Pxx == np.max(Pxx))]
f_minus3dB = fxx[np.argwhere(Pxx > np.max(Pxx) - 3)]  # -3dB
f_min = f_minus3dB[0]
f_max = f_minus3dB[-1]
f_minus3dB_bandwidth = f_max - f_min
# For f_centroid: Pxx needs to be linear
f_centroid = np.sum(np.multiply(fxx, (10 ** (Pxx / 10)) ** 2)) / np.sum(
    (10 ** (Pxx / 10)) ** 2
)
print(f"{f_peak=}")
print(f"{f_minus3dB_bandwidth=}")
print(f"{f_centroid=}")

# %% Plot a spectrogram of the whole recording
SFT = scipy.signal.ShortTimeFFT(
    np.hanning(1024),
    hop=512,
    fs=fs,
    mfft=nfft,
    scale_to="magnitude",
)

Sxx = SFT.spectrogram(rec, detr="constant")
plt.figure(5)
plt.clf()
plt.pcolormesh(SFT.t(rec.shape[0]), SFT.f / 1e3, 10 * np.log10(Sxx), shading="gouraud")
plt.colorbar()
plt.clim(-70, None)
plt.ylabel("Frequency [kHz]")
plt.xlabel("Time [s]")
plt.show()
