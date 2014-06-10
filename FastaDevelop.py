def main():
    best1 =  input("Bestandsnaam gefilterde ratios: ")             # "data.txt"
    best2 =  input("Bestandsnaam orthologen: ")                    # "LP_genes_NEW.txt"
    best3 =  input("Bestandsnaam sequenties stam 1 replicate 1: ") # "WCFS1_glc_1_tss.fa"
    best4 =  input("Bestandsnaam sequenties stam 1 replicate 2: ") # "WCFS1_glc_2_tss.fa"
    best5 =  input("Bestandsnaam sequenties stam 2 replicate 1: ") # "NC8_glc_1_tss.fa"
    best6 =  input("Bestandsnaam sequenties stam 2 replicate 2: ") # "NC8_glc_2_tss.fa"
    nieuw1 = "genes1.fa" 
    nieuw2 = "genes2.fa"
    nieuw3 = "genes3.fa"
    nieuw4 = "genes4.fa"
    
    linesData = openBestdata(best1)
    linesGenes = openBestdata(best2)
    seqWCFS1_1 = openBestdata(best3)
    seqWCFS1_2 = openBestdata(best4)
    seqNC8_1 = openBestdata(best5)
    seqNC8_2 = openBestdata(best6)
    genesWCFS1_1 = openNieuwBest(nieuw1)
    genesWCFS1_2 = openNieuwBest(nieuw2)
    genesNC8_1 = openNieuwBest(nieuw3)
    genesNC8_2 = openNieuwBest(nieuw4)
    getGenes(linesData, linesGenes, genesWCFS1_1, genesWCFS1_2, genesNC8_1, genesNC8_2, seqWCFS1_1, seqWCFS1_2, seqNC8_1, seqNC8_2)

    
def openBestdata(best):
    best = open(best, 'r')
    lines = best.readlines()
    return lines

def openNieuwBest(nieuw):
    best = open(nieuw, 'w')
    return best

def getGenes(data, genes, genesWCFS1_1, genesWCFS1_2, genesNC8_1, genesNC8_2, seqWCFS1_1, seqWCFS1_2, seqNC8_1, seqNC8_2):
    lijstLP = []
    lijstNC = []
    lijstGenes = []
    lijstSeq = []
    p = 0;
    genesWCFS1 = []
    genesNC8 = []

    for i in data:
        lijstLP.append(i[1:8])
        
    lijstLP.remove('ID"\t"WC') 
   
    
    for lp in lijstLP:
        for gene in genes:
            if lp in gene:
                gene2 = gene.split('\t')
                genesWCFS1.append('>' + gene2[0] +'\n')
                genesNC8.append('>' + gene2[1])

    for item in genesNC8:
        item2 = item.split('|')
        lijstNC.append(item2[1])

  
    for lp in lijstLP:
        for seq in seqWCFS1_1:
            if lp in seq:
                item = seqWCFS1_1.index(seq)+1
                for m in genesWCFS1:
                    if lp in m:
                        genesWCFS1_1.write(m +'\n' + seqWCFS1_1[item])
        for seq in seqWCFS1_2:
            if lp in seq:
                item = seqWCFS1_2.index(seq)+1
                for m in genesWCFS1:
                    if lp in m:
                        genesWCFS1_2.write(m +'\n' + seqWCFS1_2[item])
    for nc in lijstNC:
        for seq in seqNC8_1:
            if nc in seq:
                item = seqNC8_1.index(seq)+1
                for m in genesNC8:

                    if nc in m:
                        genesNC8_1.write(m + seqNC8_1[item])
        for seq in seqNC8_2:
            if nc in seq:
                item = seqNC8_2.index(seq)+1
                for m in genesNC8:
                    if nc in m:
                        genesNC8_2.write(m + seqNC8_2[item])
    
 
    genesWCFS1_1.close()
    genesWCFS1_2.close()
    genesNC8_1.close()
    genesNC8_2.close()

     
    

main()
