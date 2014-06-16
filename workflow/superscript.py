# Name:     Thierry Marieke Tom 
# Date:     12-6-2014
# Function: Controle the workflow
# Bugs:     unknown
import sys
sys.path.insert(0, "/home/thierry/c11_pipeline")
import log2_fdr_filter
import SortRatio
import convert
import FastaDevelop
import MEME



def main():
        defaultFilterFile = str ("/home/thierry/c11_pipeline/LP_DEG_glc.txt")
        filter(defaultFilterFile)
        defaultSortFile = "LP_DEG_glc_filtered.txt"
        #sort(defaultSortFile)
        defaultConvertFile = "LP_genes.txt"
        #converting(defaultConvertFile)
        defaultFastaFile1 = "LP_DEG_glc_filtered.txt"
        defaultFastaFile2 = "LP_genes_NEW.txt"
        defaultFastaFile3 = "WCFS1_glc_1_tss.fa"
        defaultFastaFile4 = "WCFS1_glc_2_tss.fa"
        defaultFastaFile5 = "NC8_glc_1_tss.fa"
        defaultFastaFile6 = "NC8_glc_2_tss.fa"
        #fasta(defaultFastaFile1,defaultFastaFile2,defaultFastaFile3,defaultFastaFile4,defaultFastaFile5,defaultFastaFile6)
        defaultMEMEFile = "genes"
        #meme(defaultMEMEFile)
        
        
  
  
def filter (defaultFilterFile):
  x = log2_fdr_filter.main(defaultFilterFile)
  print(x)
def sort (defaultSortFile):
        x = SortRatio.main(defaultSortFile)
        print (x)
def converting (defaultConvertFile):
        x = convert.main(defaultConvertFile)
        print (x)
def fasta(file1,file2,file3,file4,file5,file6):
        x = FastaDevelop.main(file1,file2,file3,file4,file5,file6)
        print (x)
def meme(defaultMEMEFile):
  for i in range(4):
                file =  str(defaultMEMEFile+str(i)+".fa")
                index = i
                x = MEME.main(file,idex)

main()
