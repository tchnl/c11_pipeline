###############################################
# MEME module for group 1, course 11 pipeline #
###############################################

import subprocess

def main():
##    for i in range(4):
##        MEME_input = "ftp://thierry@cytosine.nl/home/thierry/c11_pipeline/genes"+str(i)+".fa"
##        subprocess.call("cd ftp://thierry@cytosine.nl/sharing/students/MEME/bin ; ./meme <"+str(MEME_input)+"> -dna -oc . -nostatus -time 18000 -maxsize 60000 -mod zoops -nmotifs 3 -minw 6 -maxw 50 -revcomp -o ftp://thierry@cytosine.nl/home/thierry/c11_pipeline/", shell=True)
    
    MEME_input = "/home/thierry/c11_pipeline/genes0.fa"
    subprocess.call("cd /sharing/students/meme/bin/ ; ./meme /home/thierry/c11_pipeline/genes0.fa -oc /home/thierry/output/ -nostatus -time 18000 -maxsize 60000 -mod zoops -nmotifs 3 -minw 6 -maxw 50 ", shell=True)

main()
