# Name:     Thierry Marieke Tom 
# Date:     12-6-2014
# Function: Controle the workflow
# Bugs:     unknown

import log2_fdr_filter
import SortRatio

def main():
        defaultFilterFile = "LP_DEG_glc.txt"
        filter(defaultFilterFile)
        defaultSortFile = "LP_DEG_glc_filtered.txt"
        sort(defaultSortFile)
	
	
def filter (defaultFilterFile):
	x = log2_fdr_filter.main(defaultFilterFile)
	print(x)
def sort (defaultSortFile):
        x = SortRatio.main(defaultSortFile)
        print (x)
def fasta():
	print ("fasta")
	
def meme():
	print ("meme")

main()
