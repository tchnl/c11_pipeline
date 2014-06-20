# Name:     Thierry Marieke Tom 
# Date:     20-6-2014
# Function: Workflow for MEME
# Bugs:     unknown

#####################################################################
#Importeren van de scripts om ze uit te lezen
#####################################################################

import BeginGUI
import log2_fdr_filter
import SortRatio
import convert
import FastaDevelop
import MEME




def main():
        input = BeginGUI.main()
        #inputDEFAULT = ["LP_DEG_glc.txt","LP_DEG_glc_filtered.txt","LP_genes.txt","LP_DEG_glc_filtered.txt","LP_genes_NEW.txt","WCFS1_glc_1_tss.fa","WCFS1_glc_2_tss.fa","NC8_glc_1_tss.fa","NC8_glc_2_tss.fa""2"]
        getDataGUI(input)

#####################################################################
#Data ophalen en verwerken van de GUI
#Waarbij de onderstaande nummers(index) worden meegegeven vanuit de GUI 
#1: alle zonder sort
#2: met sort alles 
#4: filter
#5: sort ration
#6: convert
#7: fasta 
#8: meme
#####################################################################

def getDataGUI(input):
        ### Kijken naar de input waarde(nummer of index) van de GUI om te bepalen wat er gadaan moet worden
        index = int(input[-1])
        if index == 1:
                defaultFilterFile = input[0]
                defaultConvertFile = input[1]
                defaultFastaFile1 = input[2]
                defaultFastaFile2 = input[3]
                defaultFastaFile3 = input[4]
                defaultFastaFile4 = input[5]
                defaultFastaFile5 = input[6]
                defaultFastaFile6 = input[7]
                defaultMEMEFile = input[8]
                
                filter(defaultFilterFile)
                converting(defaultConvertFile)
                fasta(defaultFastaFile1,defaultFastaFile2,defaultFastaFile3,defaultFastaFile4,defaultFastaFile5,defaultFastaFile6)
                meme(defaultMEMEFile)                
                print ("All files are created, without the sort algorithm")
                
        if index == 2:
                defaultFilterFile = input[0]
                defaultSortFile = input[1]
                defaultConvertFile = input[2]
                defaultFastaFile1 = input[3]
                defaultFastaFile2 = input[4]
                defaultFastaFile3 = input[5]
                defaultFastaFile4 = input[6]
                defaultFastaFile5 = input[7]
                defaultFastaFile6 = input[8]
                defaultMEMEFile = input[9]
                
                filter(defaultFilterFile)
                sort(defaultSortFile)
                converting(defaultConvertFile)
                fasta(defaultFastaFile1,defaultFastaFile2,defaultFastaFile3,defaultFastaFile4,defaultFastaFile5,defaultFastaFile6)
                meme(defaultMEMEFile) 
                print("All files are created, with the sort algorithm")
                
        if index == 4:
                file = input[0]
                defaultFilterFile = str (file)
                filter(defaultFilterFile)
                print ("File LP_DEG_glc_filtered.txt created")
                
        if index == 5:
                file = input[0]
                defaultSortFile = str (file)
                sort(defaultSortFile)
                print ("File LP_DEG_glc_filtered.txt created")
                
        if index == 6:
                file = input[0]
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
                fasta(defaultFastaFile1,defaultFastaFile2,defaultFastaFile3,defaultFastaFile4,defaultFastaFile5,defaultFastaFile6)
                print ("Files: genes1.txt, genes2.txt, genes3.txt, genes4.txt created")
                
        if index == 8:
                file = input[0]
                defaultMEMEFile = str (file)
                MemeOneFile(defaultMEMEFile)
                print ("Bestand is aangemaakt")
                
        
#####################################################################
#Uitvoeren van de gevraagde modules
#####################################################################
                
def filter (defaultFilterFile):
        x = log2_fdr_filter.main(defaultFilterFile)
  
def sort (defaultSortFile):
        x = SortRatio.main(defaultSortFile)
        
def converting (defaultConvertFile):
        x = convert.main(defaultConvertFile)
        
def fasta(file1,file2,file3,file4,file5,file6):
        x = FastaDevelop.main(file1,file2,file3,file4,file5,file6)
        

#MEME waarbij 4 keer meme wordt aangeroepen
def meme(defaultMEMEFile):
  for i in range(4):
                file =  str(defaultMEMEFile+str(i)+".fa")
                index = i
                x = MEME.main(file,idex)
#MEME gebruik voor 1 file
def MemeOneFile(defaultMEMEFile):
        int(i) = 1
        file =  str(defaultMEMEFile+str(i)+".fa")
        x = MEME.main(file,idex)
        

main()
