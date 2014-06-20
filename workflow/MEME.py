###############################################
# MEME module for group 1, course 11 pipeline #
###############################################

import subprocess

def main(file, index):
    
    MEME_input = str(file)
    subprocess.call("cd <$path where meme is installed/bin> ; ./meme <$path to desktop>/workflow/"+str(MEME_input)+" -dna -oc <$path to desktop>/output"+str(index)+"/ -nostatus -time 18000 -maxsize 60000 -mod zoops -nmotifs 3 -minw 45 -maxw 55 -revcomp", shell=True)
    return True
