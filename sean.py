import numpy as np
import librosa
import os
import scipy
import glob
import random
import time
import subprocess



def change_pitch_speed_and_play(log_file_path = "./*.wav"):

    sound_files =  glob.glob(log_file_path)
    #rando_sound_file = random.choice(sound_files)
    sound_file = sound_files[0]

    sample_rate, samples = scipy.io.wavfile.read(sound_file)
    y_pitch_speed = samples.copy()
    # you can change low and high here
    length_change = 1.2 #np.random.uniform(low=0.5, high = 2)
    speed_fac = 1.0  / length_change
    tmp = np.interp(np.arange(0,len(y_pitch_speed),speed_fac),np.arange(0,len(y_pitch_speed)),y_pitch_speed)
    minlen = min(y_pitch_speed.shape[0], tmp.shape[0])
    y_pitch_speed *= 0
    y_pitch_speed[0:minlen] = tmp[0:minlen]
    
    return y_pitch_speed, sample_rate, os.path.basename(sound_file)


if __name__ == '__main__':
    path_to_watch = "./"
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    while 1:
        time.sleep (2)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added: 
            print("Added: ", ", ".join (added))
            file_path_to_save = "./data"
            y, sr,sound = change_pitch_speed_and_play(log_file_path=path_to_watch+added[0])
            scipy.io.wavfile.write(filename=file_path_to_save+"/formated_"+sound,rate=sr, data=y)

        if removed: print("Removed: ", ", ".join (removed))
        before = after

##script two is just a bash script that plays and pulls from a directory
# bash script to play file
# if name == main()
