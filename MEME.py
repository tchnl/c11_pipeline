###############################################
# MEME module for group 1, course 11 pipeline #
###############################################

import subprocess

def main():
    for i in range(4):
        MEME_input = "genes"+str(i)+".fa"
        #print MEME_input
        subprocess.call("cd ftp://cytosine.nl/sharing/students/MEME/bin/ ; ./meme <"+str(MEME_input)+"> -dna -oc . -nostatus -time 18000 -maxsize 60000 -mod zoops -nmotifs 3 -minw 6 -maxw 50 -revcomp -o ftp://thierry@cytosine.nl/home/thierry/c11_pipeline/", shell=True)

main()
