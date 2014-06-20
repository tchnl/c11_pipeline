Motif finder
=========

The Motif finder is a python-based tool, made by Marieke Beltman, Tom Linssen and Thierry Haddad. It's goal is to find various MEME motifs based on input given.

Main Window
----
In the Main Window, one of the next items can be chosen:
- All modules without Sort
- All modules include Sort
- Select individual modules

When you choose All modules without Sort or All modules include Sort, you can enter the file names (e.g. "Ratios.txt") in the indicated boxes in the next GUI.

When you choose Select individual modules, you can choose one of the following modules: 
- Filter ratio's
- Sort ratio's
- NC/NZ convert
- FASTA files maker
- MEME 

Next, you can enter the required filenames (e.g. "Ratios.txt") in the indicated boxes in the next GUI.


Version
----

1.0


Installation
--------------
Motif finder can be installed in 2 ways:
####Clone from GitHub
The Workflow folder needs to be placed on the Desktop.
```sh
git clone git@github.com:tchnl/c11_pipeline.git
```
####Manual repository download
The Workflow folder can also be manually downloaded from the c11_pipeline at https://github.com/tchnl/c11_pipeline.

Python Scripts
-----------

The Motif finder currently consists of the following scripts:

  - BeginGUI.py
  - superscript.py
  - log2_fdr_filter.py
  - SortRatio.py
  - Convert.py
  - FastaDevelop.py
  - MEME.py
  
####log2_fdr_filter.py
This script filters out the genes that have both a proper log2 value (lesser than 1 and more than -1) and fdr value (less than 0,05). 
- The input file is a tab delimited file containing 2 columns. 
- The 2 upper lines are reserved for headers. 
- If you want to replace this file with your own, make sure it looks like the example beneath (but with 2 header lines):


    ID	WCFS1.glc.over.NC8.glc	fdr.WCFS1.glc.over.NC8.glc
    lp_0001	0.1447888778	0.588882175
    lp_0002	0.1290206907	0.6667254051
    lp_0004	0.3068669561	0.2503970634
    lp_0005	0.1489820994	0.5769007869

####Sort.py
The function of this module is sorting the ratios in the file with (filtered) ratios.
The inputfile should contain the following items:
- It should be a tab delimited text file
- The first line of the file is a header and the first column name should be 'ID'
- The first column should contain lp_0000 numbers
- The ratios should be standing in the second column


    ID	    WCFS1.glc.over.NC8.glc	fdr.WCFS1.glc.over.NC8.glc
    lp_0817	-0.3528561156	        0.0345769311
    lp_1562	-0.3946108719	        0.0277561895
    lp_1561	-0.4062462596	        0.025912464
    lp_2325	-0.4088324993	        0.0171639533

####Convert.py
This script's function is to separate orthologues in LP_genes_NEW.txt if there are more than 2 orthologues in a single row. It reads a tab-delimited file.

Example of the input:

    NC_004567|lp_1688|1536646_1537197|184AA	NZ_AGRI01000006|nc8_1446|106184_106735|184AA
    NC_004567|lp_2800|2494449_2495225|259AA	NZ_AGRI01000010|nc8_2380|173512_174288|259AA
    NC_004567|lp_0438|391575_391997|141AA	NZ_AGRI01000003|nc8_0402|60872_61294|141AA


If you want to replace LP_genes_NEW.txt with a similar file:
- The first 2 lines of LP_genes_NEW.txt are headers and are ignored by the script
- Replace "NC" and "NZ" in the script for the two orthologue-prefixes in your own file
- Either rename your file to LP_genes_NEW.txt or replace the file name in the Python script
- Both the script and the orthologues file need to be placed in the /Workflow folder	
	
####FastaDevelop.py
The function of this module is to make FASTA files by merging different files.
The files which will be used by this module are:
- The file with the (filtered and/or sorted) ratio's:
 - The file has to be a tab delimited text file
 - This file should contain a header
 - The lines have to begin with a lp_0000 number
 - The file should look like this:


    ID	    WCFS1.glc.over.NC8.glc	fdr.WCFS1.glc.over.NC8.glc
    lp_0817	-0.3528561156	        0.0345769311
    lp_1562	-0.3946108719	        0.0277561895
    lp_1561	-0.4062462596	        0.025912464
    lp_2325	-0.4088324993	        0.0171639533


- The file with orthologues (output from convert.py):
 - The file has to be a tab delimited text file
 - There should be only two orthologues per single line, first the ortologue with the LP_number and second the orthologue with the nc8_number.
 - The names of the ortologues have to look like this (NC or NZ number|lp_number or nc8_number|positions|length of sequence):


    NC_004567|lp_1688|1536646_1537197|184AA NZ_AGRI01000006|nc8_1446|106184_106735|184AA
    NC_004567|lp_2800|2494449_2495225|259AA NZ_AGRI01000010|nc8_2380|173512_174288|259AA
    NC_004567|lp_0438|391575_391997|141AA   NZ_AGRI01000003|nc8_0402|60872_61294|141AA
    NC_004567|lp_0436|390029_391390|454AA   NZ_AGRI01000003|nc8_0400|59326_60687|454AA
    NC_004567|lp_0435|389246_389956|237AA   NZ_AGRI01000003|nc8_0399|58543_59253|237AA


- Four files with sequences:
 - 2 replicates for each bacterial strain.
 - The files should be fasta files and look like this:

    
    >tss_lp_0004
    AAAATGGCTCTGAGTGCGGTTATAAATTGAATTTTCATCAAAAAACAAGTATAATATAACCTGTTAGGAGTGTGTGTAG    CACGCCAGACAGTCGTTTAAT
    >tss_lp_0009
    TTTTTGTAACAGTCGGCCGCTTCAACCCTTGCAACAAACTGATTTAGATGCTATACTTTAAATTCGTGAGTATCTAGCA    TTAGCTAGATTACTTTCCTTG

####MEME.py
Our MEME has only been tested on Linux based computers and should be installed on /sharing/students/meme/. Make sure the MEME executable file is placed in /sharing/students/meme/bin/.

The MEME script is build to accept a FASTA file for input. These are named "genes0.fa", "genes1.fa" etc. They superscript automatically names these FASTA files. The superscript runs the MEME script once for every FASTA file transmitted by the superscript.

The script changes location to the MEME bin directory (/sharing/students/meme/bin/) to call MEME. The parameters can be changed in the script. For parameter options, type 

    meme --help
    
in the Terminal. The default parameters are as follows:

    "/meme "+str(MEME_input)+" -dna -oc /home/thierry/c11_pipeline/output"+str(i)+"/ -nostatus -time 18000 -maxsize 60000 -mod zoops -nmotifs 3 -minw 35 -maxw 45 -revcomp"
    
str(MEME_input) are the 4 FASTA input files. The amount of input files can be changed. To modify the amount of FASTA files for MEME, change the "range" option in the script to the desired amount -1 (so if you have 6 scripts, give it a range of 5, as it automatically starts from "0").


License
----

Free software.