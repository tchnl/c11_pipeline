

def main(lijst):

    lijstNieuw = []
    lijstNieuw2 = []
    for line in lijst:
        if line.startswith("lp"):
            line2 = line.split("\t")
            #print(line2)
            t = (line2[0], line2[1], line2[2])
            lijstNieuw.append(t)
    lijst2 = sorted(lijstNieuw, key=lambda line2: line2[1])
    for item in lijst2:
        item = "\t".join(item)
        print (item)
        lijstSorted.append(item)
    
        
    
    return lijstSorted 

    
    
        
        
    
        
    



main()
