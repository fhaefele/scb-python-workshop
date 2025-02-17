![SCB Python Workshop](./img/python_learning_fluxai.png)
# SCB Python workshop
This is the repository for the Sound Communication and Behaviour Group's Python workshop 2025. You will find all teaching materials in this repository.


## Presentation
https://docs.google.com/presentation/d/1bH0J_6equk9mno7ffnL0q0_LL3T7o7mY8hCRrttJ4Bg/edit?usp=sharing

## Exercises
### Exercise 1 - Python basics
This exercise will teach you the basics of Python. You can find it here:


### Exercise 2 - Make venvs and share them
1. Make a virtual environment (venv) with conda and python version 3.12. 
    * Activate it and use `conda info` and/or `conda config --show channels` commands to display information about the environment’s package channels (i.e. repositories from which packages will be installed)
    * Add the conda-forge channel (more up-to-date and community-run). Use `conda config -h` (or `--help`) or https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html to learn how to do that . Once added, display the environment’s channel priority information, and make sure it is set to 'strict'.
2. Install the following packages:
    * spyder and spyder-notebook 
    * librosa
    * Scipy version 1.15.1
    * pip-chill
    * asciimatics, pycowsay and/or coolname (check out their pypi sites)
3. Export the environment to an `<environment>.yml` file. The file should work across platforms.
    * Try creating an environment file for your operating system and compare the two .yml files.
4. Share the file with someone in class and take their `<environment>.yml` file in return.
5. Make another venv using that environment file


### Exercise 3 - Make venvs and share them
1. Make a project folder called "exercise_2".
2. Write a Python module called `<module_name>.py` by opening a script in your favorite editor.
    * Define at least 3 functions in `<module_name>.py`. 
    * Each of the functions should have a variation of positional and keyword arguments.
    * Write docstrings for your functions.
3. Create a second script `<test>.py` in the same directory and import the module.
4. Execute all of your functions in `<test>.py`. Use a variation of arguments to test your functions. You should also print the docstring to the terminal using the `help(<module_name>.<your_function>)` command.
5. Now move the `<module_name>.py` file into a different directory and adjust the imports accordingly.
    * Move the file into a new directory within "exercise_2". 
    * Move the file into a different directory outside of "exercise_2". Use the sys module to append the new path/location of `<module_name>.py`. 

### Exercise 4 - Your first acoustic analysis project in Python
1. Make a new directory and unzip the zip-folder "find_the_wavs.zip" into it.
2. Make a new venv for this exercise and install the packages scipy, matplotlib, soundfile and sounddevice. (Within Spyder, verify that in Tools > Preferences > IPython console > Graphics Matplotlib uses Qt for Graphics Backend)
3. There are 14 audio files hidden in "find_the_wavs". Find all and put them into a single list. Sort the list based on the filenames.
    * Pick the recording #5 to continue this exercise.
4. Read the audiofile into an array.
    * Extract the following parameters: sampling rate, number of channels, total number of samples, duration, bit depth.
    * Compare the output array from soundfile and scipy. What is the difference and how can you convert one to the other?
    * Play the audio file at an appropriate sampling rate.
5. Plot the oscillogram of the recording with an appropriate time scale. 
6. Select a call segment to continue your analysis with. The segment should only contain a single vocalization. This segment will be used from here onwards.
7. Generate a plot that indicates which part of the recording segment contains 95% of the energy. You can use the cumulative energy to find the correct window.
8. [Optional] Extract the following basic parameters from the time domain signal: peak, peak-to-peak and RMS pressure, energy.
9. Transform the signal segment into the frequency domain. Additionally, estimate the power spectral density with Welch's method. Plot both into the same figure. Make sure you normalize both correctly to display [dB/Hz] on the y-axis.
10. [Optional] Extract the following basic parameters from the frequency domain signal: peak frequency, bandwidth and centroid frequency.
11. Plot a spectrogram of the whole recording.
12. [Optional] Convert the analysis pipeline into a series of functions such that you can loop over all 14 recordings and display all plots and extract all parameters. 
