#place this python file in the directory with all the species projections
#output will be a origin folder with different species folder in it, and all the
#.grd .gri files will be moved accordingly into the species foler.
import os, re
filelist = os.listdir('./') #all the files in the folder
pattern = '[A-Z]+ [A-Z]+' #pattern for id'ing species
filestring = ','.join(filelist) #join the list of folder names into one string.
Species = re.findall(pattern,filestring) #in the filestring find all the species names
Species = list(set(Species)) #remove redundant names
folderNames = [x.lower().replace(' ','_') for x in Species] #make list of folderNames made of species in lower case
os.system('mkdir origin') #make origin dir
for folder in folderNames: #make species dir in the origin
    os.system('mkdir '+'origin/'+folder)
for file in filelist: #put every .gri .grd into the species folder accordingly
    if file.endswith('.gri') or file.endswith('.grd'): #if the file is .gri or .grd
        id = re.findall(pattern,file) #get the species id for the file
        folder2go = id[0].lower().replace(' ','_') #identify the species dir name for the file to go
        command = 'mv ' + file.replace(' ','\ ') + ' ./origin/' + folder2go #command to move it into the species dir
        os.system(command)
