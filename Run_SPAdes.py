#!/usr/bin/python3
import os

def main():
    #file paths for SPAdes, quality trimmed reads, and output
    spades = '/data/SPAdes_Assembly/SPAdes-3.14.1-Linux/bin/spades.py'
    original = '/data/trimmed_practice_reads/'
    new = '/data/practice_assemblies/'
    
    try:
        os.mkdir(new)
    except PermissionError:
        os.system('sudo mkdir ' + new)
    except FileExistsError:
        pass

    runSPAdes(spades, original, new)

def runSPAdes(spades, original, new):
    #cycle through all quality trimmed reads
    for read in os.listdir(original):
        r1name = str(read)

        #check which read out of R1 or R2
        r1test = r1name.find('R1')
        if r1test != -1:
            r2name = r1name[:r1test] + 'R2' + r1name[r1test+2:]
        else:
            pass

        #need to record the UMB#### tag
        tagLoc = r1name.find('UMB')
        if r1name[tagLoc+6].isdigit(): 
            #UMB four digits
            tag = r1name[tagLoc:tagLoc+7]
        else:
            #UMB three digits
            tag = r1name[tagLoc:tagLoc+6]

        #create new directory using UMB#### as name
        try:
            os.mkdir(new + tag)
        except PermissionError:
            os.system('sudo mkdir ' + new + tag)
        outputDir = new+tag

        #form spades command
        command = 'python3 ' + spades + ' -1 ' + original + r1name + ' -2 ' + original + r2name + ' -o ' + outputDir
            
        #test
        #print(tag)
        #print(command)
        #break

        #call spades
        try:
            os.system(command)
        except PermissionError:
            os.system('sudo ' + command)

        #get rid of all SPAdes output files except contigs.fasta
        prune(new, outputDir, tag)
        #break
    
def prune(new,sir, tag):
    #function to delete every SPAdes output except contigs.fasta
    for files in os.listdir(sir):
        if str(files) != 'contigs.fasta':
            #check if current file is directory
            if os.path.isfile(sir + str(files)):
                #print('\n FILE')
                os.system('sudo rm ' + sir + str(files))
            else:
                #print('\n DIR')
                os.system('sudo rm -r ' + sir + str(files))
        #relabel contigs.fasta with UMB####
        else:
            os.system('sudo mv ' + sir + 'contigs.fasta ' + sir + tag + '_contigs.fasta')


main()
            
    
