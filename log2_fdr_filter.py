###############################################
# Filter log2/fdr module                      #
###############################################

def main(file):
    input_data = open(file, "r").readlines()
    sorted_list = []
    output_data = open("LP_DEG_glc_filtered.txt", "w")
    output_data.write(input_data[1])

    for line in input_data[2:]:
        line_split = line.strip().split()
        if float(line_split[1]) > -1 and float(line_split[1]) < 1:
            if float(line_split[2]) < 0.05:
                sorted_list.append(line)
    

    for line in sorted_list:
        output_data.write(line)
	
    return (True)


