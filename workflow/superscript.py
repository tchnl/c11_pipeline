# Name:     Thierry Marieke Tom 
# Date:     12-6-2014
# Function: Controle the workflow
# Bugs:     unknown

#import BeginGUI
import log2_fdr_filter
import SortRatio
import convert
import FastaDevelop
import MEME

#1: alle zonder sort
#2: met sort alles 
#4: filter
#5: sort ration
#6: convert
#7: fasta 
#8: meme
#list einde list

def main():
        #input = BeginGUI.main()
        input = ["string1","string2","string3","string3","string3","string3","7"]
        getDataGUI(input)


        defaultFilterFile = str ("LP_DEG_glc.txt")
        #filter(defaultFilterFile)
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


def getDataGUI(input):
        index = int(input[-1])
        if index == 1:
                print ("All files are created, without the sort algorithm")
        if index == 2:
                print("All files are created, with the sort algorithm")
        if index == 4:
                file = input[0]
                file = "LP_DEG_glc.txt"
                defaultFilterFile = str (file)
                filter(defaultFilterFile)
                print ("File LP_DEG_glc_filtered.txt created")
        if index == 5:
                file = input[0]
                file = "LP_DEG_glc_filtered.txt"
                defaultSortFile = str (file)
                sort(defaultSortFile)
                print ("File LP_DEG_glc_filtered.txt created")
                
        if index == 6:
                file = input[0]
                file = "LP_genes.txt"
                defaultConvertFile = str (file)
                converting(defaultConvertFile)
                print ("File LP_genes_NEW.txt created")
                
        if index == 7:
                defaultFastaFile1 = input[0]
                defaultFastaFile2 = input[1]
                defaultFastaFile3 = input[2]
                defaultFastaFile4 = input[3]
                defaultFastaFile5 = input[4]
                defaultFastaFile6 = input[5]
                defaultFastaFile1 = "LP_DEG_glc_filtered.txt"
                defaultFastaFile2 = "LP_genes_NEW.txt"
                defaultFastaFile3 = "WCFS1_glc_1_tss.fa"
                defaultFastaFile4 = "WCFS1_glc_2_tss.fa"
                defaultFastaFile5 = "NC8_glc_1_tss.fa"
                defaultFastaFile6 = "NC8_glc_2_tss.fa"
                fasta(defaultFastaFile1,defaultFastaFile2,defaultFastaFile3,defaultFastaFile4,defaultFastaFile5,defaultFastaFile6)
                print ("Files: genes1.txt, genes2.txt, genes3.txt, genes4.txt created")
        if index == 8:
                file = input[0]
                file = "genes1.fa"
                defaultMEMEFile = str (file)
                MEME(defaultMEMEFile)
                print ("Bestand is aangemaakt")
                
        
        
                
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
