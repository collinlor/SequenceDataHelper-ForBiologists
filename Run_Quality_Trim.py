#!/usr/bin/python
import os

def main():
    #file paths for bbduk, raw reads, and trimmed output
    print('\n')
    bbdukFile = input('Enter the full path of the bbduk.sh file:').strip()
    
    print(bbdukFile)

    bothTypes = input('Do you wish to quality trim both Paired and Unpaired reads? (Y/N):').strip().upper()
    
    if bothTypes == 'Y':
        pairedDir = input('Provide the directory that holds the Paired reads:').strip()
        unpairDir = input('Provide the directory that holds the Unpaired reads:').strip()

        #form the new directories and call BBDuk. Pass the Y to BBDUk
        #program to use the correct BBDuk input

        #form directories of trimmed reads
        newPDir = makeDir(pairedDir,'P')
        newUDir = makeDir(unpairDir, 'U')

        #call BBDuk
        BBDukIt(bbdukFile, pairedDir, newPDir, 'P')
        BBDukIt(bbdukFile, unpairDir, newUDir, 'U')

    elif bothTypes == 'N':
        whichType = input('Enter \'P\' for Paired or \'U\' for Unpaired:').strip().upper()
        
        directory = input('Provide the directory that holds the reads:').strip()

        #form the new directory and call BBDuk. 
        destinationDir = makeDir(directory, whichType)

        #call BBDuk

        BBDukIt(bbdukFile, directory, destinationDir, whichType)


def makeDir(originalPath,readType):
    #Simply make Directory inside of given directory
    #Named "Trim_" readType
    if readType == 'P':
        newDir = 'Trim_Paired'
    elif readType == 'U':
        newDir = 'Trim_Unpaired'
    
    if originalPath[-1] != '/':
        originalPath+='/'

    finalDir=''
    try:
        os.mkdir(originalPath + newDir)
        finalDir = originalPath + newDir + '/'

    except(PermissionError):
        os.system('sudo mkdir ' + originalPath + newDir)
        finalDir = originalPath + newDir+'/'
    
    except(FileExistsError):
        
        potential = originalPath+newDir + '.2'
        
        print(originalPath+newDir+'/  \t already exists. If you choose to NOT use the existing directory, ' + potential + ' will be the new output location')
        carry = input('Do you wish to utilize the existing output directory? (Y/N)').strip().upper()

        if carry == 'Y':
            finalDir = originalPath+newDir+'/'
            pass
        elif carry == 'N':
            os.mkdir(potential)
            finalDir = potential+'/'

    return finalDir


def BBDukIt(bbduk, origin, new, readType):
    #cycle through all raw reads
    for read in os.listdir(origin):
        
        #need to skip all directories
        if os.path.isdir(read):
            pass
        else:
            r1name = str(read)
        
        #for paired reads
        if readType == 'P':
            #call the command using R1 files only
            r1nameLocation = r1name.upper().find('R1')
            if r1nameLocation != '-1':
                r2name = r1name[:r1nameLocation] +'R2'+ r1name[r1nameLocation+2:]

                r1out = new + r1name
                r2out = new + r2name

                #create the command
                command = 'bash ' + bbduk + ' in1=' + origin+'/'+r1name + ' in2=' + origin+'/'+r2name+ ' out1='+r1out + ' out2='+r2out + ' qtrim=rl trimq=35'
            
        elif readType == 'U':
            r1out = new+'/'+r1name

            command = 'bash ' + bbduk + ' in=' + origin+r1name + ' out=' + r1out + ' qtrim=rl trimq=35'

        #command check
        print('\n'+command+'\n')
        
        #call the command
        #try:
        #    os.system(command)
        #except(PermissionError):
        #    os.system('sudo ' + command)
        #except(FileNotFoundError):
        #    print('The BBDuk script file was not input correctly or the sequence file paths were not correct; be sure to include /"bbduk.sh/" at the end of your BBDuk path /n')
        
        #test
        break


main()
