###############################################
# MEME module for group 1, course 11 pipeline #
###############################################

import subprocess

def main(file, index):
    
    MEME_input = str(file)
    subprocess.call("cd /sharing/students/meme/bin/ ; ./meme "+str(MEME_input)+" -dna -oc /home/thierry/c11_pipeline/output"+str(index)+"/ -nostatus -time 18000 -maxsize 60000 -mod zoops -nmotifs 3 -minw 35 -maxw 45 -revcomp", shell=True)
    return True

##    MEME_input = "/home/thierry/c11_pipeline/genes0.fa"
##    subprocess.call("cd /sharing/students/meme/bin/ ; ./meme /home/thierry/c11_pipeline/genes0.fa -oc /home/thierry/output/ -nostatus -time 18000 -maxsize 60000 -mod zoops -nmotifs 3 -minw 35 -maxw 45 ", shell=True)
