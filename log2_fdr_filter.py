###############################################
# Filter log2/fdr module                      #
###############################################

def main():
    input_data = open("/home/thierry/c11_pipeline/LP_DEG_glc.txt", "r").readlines()
    sorted_list = []

    for line in input_data[2:]:
        line_split = line.strip().split()
        if float(line_split[1]) > -1 and float(line_split[1]) < 1:
            if float(line_split[2]) < 0.05:
                sorted_list.append(line)
    
    nieuwBest = open("testLog2.txt", "w")
    nieuwBest.write(str(sorted_list))
    return sorted_list

main()
