# SequenceDataHelper-ForBiologists
This repository holds python scripts meant to help biologists analyze their sequence data on their Linux machines.

These sequence analysis tools are designed for DNA or RNA sequencing. 

Prior Requirements--------
Firstly, Python3 must be installed on the Linux machine. Instructions for checking for and downloading Python3 can be found here: https://docs.python-guide.org/starting/install3/linux/ 


Fastq Quality Filtering ----------
  First, the raw read data must be filtered by quality. Fastq sequence files contain a quality indicator for every nucleotide in the read. The Joint Genome Institute has a tool called BBDuk that will remove and trim reads that fall below a quality threshold. Low quality reads may indicate sample contamination, and it is highly recommended that they be filtered out before further analysis. 
Follow https://jgi.doe.gov/data-and-tools/bbtools/bb-tools-user-guide/installation-guide/ for tool installation instruction and guides. 
Run_Quality_Trim.py is the script for quality trimming. This script requires prompted user keyboard inputs:
1. Input the full path of the bbduk.sh script file. e.g. /data/BBDuk_Quality_Trim/bbmap/bbduk.sh
2. Are you, the user, using quality trim on both Paired and Unpaired reads at once? Response: Y/N. Paired reads generally have two files per sequencing run. This means that a pair of files will complimentarily represent the sequencing of the same sample. This tool requires the two reads be marked by R1 or R2 tags in the file names. Unpaired reads are single files of single stranded sequencing data. 
This tool requires the Paired reads and Unpaired reads to be in separate directories; there must be one directory of Paired reads and one directory of Unpaired reads.
3. If the answer to 2 was 'N' (If you, the user, are hoping to quality trim only one type of sequencing data), enter the type of sequencing data. 'P' for Paired or 'U' for Unpaired reads.
4. Enter the full path to the directory holding the the read files. e.g. /data/practice_raw_reads
i. If the answer to 2 was 'Y' (If you, the user, are hoping to quality trim both types of sequencing data), you will be asked to input the full paths to both directories. First, the path to the directory of Paired sequencing files. Second, the path to the directory of Unpaired sequencing files. 

The script will then create a directory called either Trim_Paired or Trim_Unpaired to hold the trimmed sequencing data within the given directories of raw sequencing data. 

SPAdes Assembly --------------
  Refer to https://cab.spbu.ru/files/release3.14.1/manual.html for the installation and usage guide. Before using Run_SPAdes.py, the script relies on the input data organizational system. If the reads are paired, it is assumed that the read files are separated into forward and reverse files in the same directory. Additionally, the file names should be labeled with 'R1' in the file name of the forward reads and 'R2' in the file name of the reverse reads. 
  Importantly, each genome is labeled with a "tag" that each read corresponding to that genome will have in the file name. For example, genomes for a project may be labeled 'UMB001' through 'UMB100'.  Run_SPAdes.py requires the user to input the letters that make up the 'tag' for the data. In the previous example, 'UMB' are the letters being used in the tag, and Run_SPAdes.py will automatically detect the numeric components. 
  Once SPAdes is installed, Run_SPAdes.py is an easy script to automate the assembly of multiple genomes. Use vim, nano, or your preferred text editors to edit Run_SPAdes.py. There are 5 necessary inputs on lines 8, 11, 14, 17, and 20. Each required change is highlighted by a 'CHANGE ME:' followed by a brief description on the line above. User changes must be within the apostrophes. 
  1. input the full path of the installed spades.py
  2. input the full path of the directory holding all filtered reads
  3. input the full path of the new directory that will hold all results
  4. input the type of sequence data. D for DNA/genomic, R for RNA, or M for metagenomic data
  5. input the alphabetic components of the genomic tags for the project. These 'tags' -described above- should be consistent throughout the dataset that you are working with. For example, a three-genome project may use labels G1, G2, and G3 within the read file names to signify the reads corresponding to a specific sample. The input in this example would be 'G'.
  6. input 'Y' if only the output contigs.fasta file is desired; 'N' if all output files are desired


Filter Contigs Script Description -------------
filter_contigs.py is for more advanced users that hope to use NCBI's PGAP for genome annotation. filter_contigs.py uses Biopython, which must be installed (instructions and manual: https://biopython.org/wiki/Download). PGAP has a minimum contig length of 200 basepairs, and filter_contigs.py removes all contigs that do not meet the 200 bp threshold. The input and output file paths must be manually changed before use. Additionally, the user must be weary of the linux machine's file creation permissions, so the script might be required to run in the same directory as the file the user wishes to filter. 
