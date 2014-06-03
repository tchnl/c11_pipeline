data = open("/home/users/dhfot/Desktop/week 4/Zip bestand/LP_genes.txt", "r").readlines()
data_new = open("/home/users/dhfot/Desktop/week 4/Zip bestand/LP_genes_NEW.txt", "w")

new_set = []
for line in data[2:]:
    line_split = line.split()
    if len(line_split) > 2:
        for NC in line_split:
            if "NC" in NC:
                for NZ in line_split:
                    if "NZ" in NZ:
                        new_set.append(NC+"\t"+NZ+"\n")
                        
    else:
        new_set.append(line)

for line in new_set:
    data_new.write(line)


