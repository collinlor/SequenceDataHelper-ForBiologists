# SequenceDataHelper-ForBiologists
This repository holds python scripts meant to help biologists analyze their sequence data on their Linux machines.

These sequence analysis tools are designed for DNA or RNA sequencing. 

Fastq Quality Filtering ------
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
