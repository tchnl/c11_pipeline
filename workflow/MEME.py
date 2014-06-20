###############################################
# MEME module for group 1, course 11 pipeline #
###############################################

import subprocess

def main(file, index):
    
    MEME_input = str(file)
    subprocess.call("cd <$path where meme is installed/bin> ; ./meme <$path to desktop>/c11_pipeline/workflow/"+str(MEME_input)+" -dna -oc /home/marieke/c11_pipeline/output"+str(index)+"/ -nostatus -time 18000 -maxsize 60000 -mod zoops -nmotifs 3 -minw 35 -maxw 45 -revcomp", shell=True)
    return True
