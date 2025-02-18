import my_module

# or
from my_module import print_a_word_x_times, sleep_for_some_time, speak_like_master_yoda

my_module.print_a_word_x_times("Hello Master Yoda!", 3)
my_module.sleep_for_some_time(3)
master_yoda_says = my_module.speak_like_master_yoda("You must learn Python")
print(f"Master Yoda: '{master_yoda_says}'")

# or when you import the function directly
print_a_word_x_times("Hello Master Yoda!", 3)
sleep_for_some_time(3)
master_yoda_says = speak_like_master_yoda("You must learn Python")
print(f"Master Yoda: '{master_yoda_says}'")

# and we can also look at the docstrings for help
help(my_module.print_a_word_x_times)
help(my_module.sleep_for_some_time)
help(my_module.speak_like_master_yoda)

# If you move my_module to for example "exercise-3/new_home_of_my_module"
# then the imports have to be adjusted accordingly including the function calls
import new_home_of_my_module.my_module

# If you move my_module anywhere else outside of exercise-3
# then you need to append that location to the Python path
import sys
sys.path.append('/path/to/new/location/of_module/') 

# thats the "super directory" where my_module.py is now
# to make it a bit more visual, lets rename my_module.py to my_module2.py
# and then import and execute new functions there.
import my_module2
my_module2.print_a_word_x_times("Hello Master Yoda!", 5)