def main(lijstRatios):
    #best1 = "data.txt"
    best2 = "LP_genes_ED.txt"
    best3 = "WCFS1_glc_1_tss.fa"
    best4 = "WCFS1_glc_2_tss.fa"
    best5 = "NC8_glc_1_tss.fa"
    best6 = "NC8_glc_2_tss.fa"
    nieuw1 = "genes1.fa"
    nieuw2 = "genes2.fa"
    nieuw3 = "genes3.fa"
    nieuw4 = "genes4.fa"
    
    #linesData = openBestdata(best1)
    linesGenes = openBestdata(best2)
    seqWCFS1_1 = openBestdata(best3)
    seqWCFS1_2 = openBestdata(best4)
    seqNC8_1 = openBestdata(best5)
    seqNC8_2 = openBestdata(best6)
    genesWCFS1_1 = openNieuwBest(nieuw1)
    genesWCFS1_2 = openNieuwBest(nieuw2)
    genesNC8_1 = openNieuwBest(nieuw3)
    genesNC8_2 = openNieuwBest(nieuw4)
    getGenes(linesData, linesGenes, genesWCFS1_1, genesWCFS1_2, genesNC8_1, genesNC8_2, seqWCFS1_1, seqWCFS1_2, seqNC8_1, seqNC8_2, lijstRatios)

    
def openBestdata(best):
    best = open(best, 'r')
    lines = best.readlines()
    return lines

def openNieuwBest(nieuw):
    best = open(nieuw, 'w')
    return best

def getGenes(data, genes, genesWCFS1_1, genesWCFS1_2, genesNC8_1, genesNC8_2, seqWCFS1_1, seqWCFS1_2, seqNC8_1, seqNC8_2, lijstRatios):
    lijstLP = []
    lijstNC = []
    lijstGenes = []
    lijstSeq = []
    p = 0;
    genesWCFS1 = []
    genesNC8 = []
    
    for line in lijstRatios::
        line2 = line.split("\t")
        lijstLP.append(line2[0])
    
    for lp in lijstLP:
        for gene in genes:
            if lp in gene:
                gene2 = gene.split('\t')
                genesWCFS1.append('>' + gene2[0] +'\n')
                genesNC8.append('>' + gene2[1])

    for item in genesNC8:
        item2 = item.split('|')
        lijstNC.append(item2[1])


    fasta1 = fastaMaker(lijstLP, seqWCFS1_1, genesWCFS1, genesWCFS1_1)
    fasta2 = fastaMaker(lijstLP, seqWCFS1_2, genesWCFS1, genesWCFS1_2)
    fasta3 = fastaMaker(lijstNC, seqNC8_1, genesNC8, genesNC8_1)
    fasta4 = fastaMaker(lijstNC, seqNC8_2, genesNC8, genesNC8_2)
   

def fastaMaker(lijstCode, seqGenen, genen, nieuw):
    for nc in lijstCode:
        for seq in seqGenen:
            if nc in seq:
                item = seqGenen.index(seq)+1
                for m in genes:

                    if nc in m:
                        nieuw.write(m + seqNC8_1[item])
    
 
    genesWCFS1_1.close()
    genesWCFS1_2.close()
    genesNC8_1.close()
    genesNC8_2.close()

     
    

main()
