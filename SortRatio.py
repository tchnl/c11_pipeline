

def main():
    bestand = "LP_DEG_glc_filtered.txt"
    best = openBestdata(bestand)
    bestNieuw = open("LP_DEG_glc_filtered.txt", "w")
    
    
    lijstNieuw = []
    lijstSorted = []
    
    for line in best:
        if line.startswith("ID"):
            bestNieuw.write(line)
        if line.startswith("lp"):
            line2 = line.split("\t")
            #print(line2)
            t = (line2[0], line2[1], line2[2])
            lijstNieuw.append(t)
    lijst2 = sorted(lijstNieuw, key=lambda line2: line2[1])
    for item in lijst2:
        item = "\t".join(item)
        bestNieuw.write(item)
    
        
    
    bestNieuw.close()
    
def openBestdata(bestand):
    best = open(bestand, 'r')
    lines = best.readlines()
    best.close()
    return lines   
        
        
    
        
    



main()
