# %% Add your imports here

# %% 3.) Find all 15 wav files in the directory "find_the_wavs" and add them to a list


# %% sort the based on the file names


# %% 4.) Read a random audio file


# %% 4a) Extract fs, nchannels, nsamples, duration, bit depth


# %% 4b) What is the difference between soundfile.read() and scipy.io.wavfile.read()?


# %% 4c) Play the audio file at an appropriate sampling rate.


# %% 5.) [Optional] Which recording has most channels and which is the longest?


# %% 6.) Plot the oscillogram of the recording #5 with an appropriate time scale.


# %% 7.) Select only a single call from the recording. The segment should only contain a single vocalization. 
# Lets select one segment from the call using ginput or by zooming and then requesting xl = plt.xlim()
# if you are using inline plots run %matplotlib qt before in your console
# If you want to go back to inline plots run: %matplotlib inline
# Keep in mind, that inline plots are not interactive. For always interactive plots (Matlab style)
# you should keep %matplotlib qt set. If you get an error makes ure you install the package PyQT6 in you venv.


# %% 8.) Make a plot indicating the 95% energy window. Start by by computing the cumulative energy.
# and then compute the 95% energy window, ie. a boolean vector indicating which part of the signal
# is within the window. Then make a combined figure to show the segment including the energy window. 


# %% 9.) [Optional]: Extract the following basic parameters from the time domain signal: 
# peak, peak-to-peak and RMS pressure, energy.


# %% 10.) Transform the signal into the frequency domain. Start by making a simple FFT of the signal.
# Compute also the power spectral density estimate using Welch's method. Normalize both such that they
# have the unit [dB/Hz]. Plot them both into a single plot.


# %% 11.) [Optional]: Extract the following basic parameters from the frequency domain signal: 
# peak frequency, bandwidth and centroid frequency.


# %% 12.) Plot a spectrogram of the whole recording

