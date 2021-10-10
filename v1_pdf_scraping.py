import PyPDF2
import re

pdfFileObj = open('CookBook1.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

recipe_name = []
recipe = []
ptime = 'Prep Time:'
pappt = ['PER APPETIZER:','PER SERVING:']

for page_num in range(10, pdfReader.numPages):
    
    pageObj = pdfReader.getPage(page_num)
    s = pageObj.extractText()
    d = s.split("\n")
    e = []
    
    for j in d:
        if(j.strip() !=''):
            e.append(j.strip())
    
    recipe2 = e
    counter2 = -1
    
    for line in e:
        counter2 +=1    
        if('®' in line):
            recipe2[counter2 - 1] = str (e[counter2 - 1] + "/" + e[counter2 + 1])
            recipe2[counter2] =''
            recipe2[counter2+1] =''
        if('˚' in line):
            recipe2[counter2 - 1] = str (e[counter2 - 1] + "/" + e[counter2 + 1]+ " " + e[counter2 + 2])
            recipe2[counter2] =''
            recipe2[counter2+1] =''
            recipe2[counter2+2] =''
        if('˜' in line):
            recipe2[counter2 - 1] = str (e[counter2 - 1] + "/" + e[counter2 + 1]+ " " + e[counter2 + 2])
            recipe2[counter2] =''
            recipe2[counter2+1] =''
            recipe2[counter2+2] =''
    
    counter3 = -1
    for line in recipe2:
        counter3 +=1
        if(recipe2[counter3-1].isdigit() and recipe2[counter3-2].strip() != 'Servings:'):
            recipe2[counter3] = recipe2[counter3-1] + " " + recipe2[counter3]
            recipe2[counter3-1] = ''
        if(recipe2[counter3-1] == '½' or recipe2[counter3-1] == '¾' or recipe2[counter3-1] == '1 ¼' 
           or recipe2[counter3-1] == '1 ½'  or recipe2[counter3-1] == '2 ½'  
           or recipe2[counter3-1] == '1½'):
            recipe2[counter3] = recipe2[counter3-1] + " " + recipe2[counter3]
            recipe2[counter3-1] = ''
        
    recipe3 = [line for line in recipe2 if line != '' ]
  
    loc_ptime = []
    loc_pappt = []
    counter = -1
    for line in recipe3:
        counter +=1
        if(line.strip() == ptime):
            loc_ptime.append(counter)
        for perapp_serv in pappt:
            if(perapp_serv in line.strip()):
                loc_pappt.append(counter)
    
    if(len(loc_ptime)==1 and len(loc_pappt)==1):
        for i in loc_ptime:
            recipe_name.append(recipe3[i-1])
        for j in range(loc_ptime[0]-1,loc_pappt[0]+1):
            recipe.append(recipe3[j])
            

                
    
    if(len(loc_ptime)==2 and len(loc_pappt)==2):
        for i in loc_ptime:
            recipe_name.append(recipe3[i-1])
            
        for j in range(loc_ptime[0]-1,loc_pappt[0]+1):
            recipe.append(recipe3[j])
            
                
        for k in range(loc_ptime[1]-1,loc_pappt[1]+1):
            recipe.append(recipe3[k])       
            


for perapp_serv in pappt:
    counter4 = -1
    for line in recipe:
        counter4 += 1
        if(line == perapp_serv):
            recipe[counter4] = "-End of recipe-"
    
    
#receipe name for Mohini
for line in recipe_name: 
    print( (line))
    
print("\n ------------------------------------ \n")   

#receipe for Vallabh  
for line in recipe: 
    print( (line))
    
