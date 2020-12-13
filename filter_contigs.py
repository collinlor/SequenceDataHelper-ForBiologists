from Bio import SeqIO

def main():
    inputFile = './UMB2128_contigs.fasta'
    outputFile = './UMB2128_trimmed.fasta'

    filter(inputFile, outputFile)

def filter(inFile, outFile):
    count=0
    qualityReads=[] #will hold all reads that meet threshold length
    
    for read in SeqIO.parse(inFile, 'fasta'):
        count+=1
        #check if readlen is > 200
        if len(read.seq) > 200 :
            qualityReads.append(read)
            print(read.id)

    #output the reads to the new file name UMB248_trim
    SeqIO.write(qualityReads, outFile, 'fasta')
    print('Code finished')
    print(str(len(qualityReads)) + ' reads in trimmed fasta down from ' + str(count) + ' reads')
main()
