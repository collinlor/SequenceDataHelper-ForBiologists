#!/usr/bin/python3
import os

def main():
    #file paths for SPAdes, quality trimmed reads, and output
    
    #CHANGE ME: change this file path to the full path of spades.py
    spades = '/data/SPAdes_Assembly/SPAdes-3.14.1-Linux/bin/spades.py'
    
    #CHANGE ME: change this file path to the path of the directory holding all filtered reads 
    original = '/data/trimmed_practice_reads/'
    
    #CHANGE ME: change this to a path of the new directory that will hold all results 
    new = '/data/practice_assemblies/'
    
    #CHANGE ME: change this to either 'D' for DNA, 'R' for RNA, or 'M' for metagenomic data
    which = 'D'
    
    #CHANGE ME: change this to represent the alphabetic components to the genomic 'tags'
    label = 'UMB'
    
    #CHANGE ME: change this to either 'Y' to only output the contigs.fasta file or 'N' to output all files
    toPrune = 'Y'
    
    #making the new directory
    try:
        os.mkdir(new)
    except PermissionError:
        os.system('sudo mkdir ' + new)
    except FileExistsError: #if the directory already exists
        pass

    runSPAdes(spades, original, new, label, which, toPrune)

def runSPAdes(spades, original, new, label, which, pruner):
    #cycle through all quality trimmed reads
    for read in os.listdir(original):
        r1name = str(read)
            
        #check which read out of R1 or R2
        r1test = r1name.find('R1')
        if r1test != -1:
            r2name = r1name[:r1test] + 'R2' + r1name[r1test+2:]
        else:
            pass

        #need to record the tag for current file
        #must pass the r1name and label to findTag() function
        tag = findTag(r1name,label)
        
        #end program if the tag cannot be found
        if not type(tag) is string:
            return
        
        #create new directory using file tags as name
        try:
            os.mkdir(new + tag)
        except PermissionError:
            os.system('sudo mkdir ' + new + tag)
        except FileExistsError: #the directory already exists
            print('Warning: ' + new + tag + ' is an existing directory. \n Output will be placed in directory, but output files may be under modified names.')
            pass
        
        outputDir = new+tag

        #form spades command
        #Must adhere to the specified data type
        if which == 'D': #DNA
            command = 'python3 ' + spades + ' -1 ' + original + r1name + ' -2 ' + original + r2name + ' -o ' + outputDir
        elif which == 'R': #RNA
            command = 'python3 ' + spades + ' --rna -1 ' + original + r1name + ' -2 ' + original + r2name + ' -o ' + outputDir
        elif which == 'M' #Metagenomic
            command = 'python3 ' + spades + ' --meta -1 ' + original + r1name + ' -2 ' + original + r2name + ' -o ' + outputDir
            
        #test
        #print(tag)
        #print(command)
        #break

        #call spades
        try:
            os.system(command)
        except PermissionError:
            os.system('sudo ' + command)

        #Check if user wants to prune output files
        if pruner == 'Y':
            #get rid of all SPAdes output files except contigs.fasta
            prune(new, outputDir, tag)
        #break

#For correct filing of paired reads by recognizing
#numbering after the user-given label
def findTag(fileName, label):
    tagLoc = fileName.find(label)

    #make sure user has input correct label
    if tagLoc == -1:
        print('ERROR: filing label cannot be detected. The given label:\n' + label + '\n cannot be found within filename: ' + fileName+ '\n Please check the user input.')
        return
    
    labelLen = len(label)
    
    #loop through file name until the first non-number after label
    for spot in range(tagLoc+labelLen, len(fileName)):
        status = fileName[spot].isdigit()
        if status == True: #the char is still a number
            continue
        else:
            return fileName[tagLoc:spot]

#Deletes all output files except for contigs.fasta
#also adds the sequence tag to contigs.fasta
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
            
    
