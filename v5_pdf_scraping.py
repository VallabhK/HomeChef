import PyPDF2

def get_recipe(search_string):
    
    try:
        pdfFileObj = open('CookBook1.pdf', 'rb')
    except IOError:
        print('Please place CookBook1.pdf in the directory')
        return
        
    
    
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    recipe_name = []
    recipe = []
    # creating tags to identify start and stop of recipe
    ptime = 'Prep Time:' # start of recipe tag
    pappt = ['PER APPETIZER:','PER SERVING:'] # end of recipe tags
    
    for page_num in range(10, pdfReader.numPages):
        
        # a page object
        pageObj = pdfReader.getPage(page_num)
        
        # extracting text from page.
        # this will print the text you can also save that into String
        s = pageObj.extractText()
        
        d = s.split("\n")
        e = []
        
        for j in d:
            if(j.strip() !='') and (j.strip() !='TODAY™S') and (j.strip() !='RECIPE'):
                e.append(j.strip())
        
        recipe2 = e
        counter2 = -1
        
        # removing special characters between sentences causing a line break. 
        # appending line back to original line #
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
        
        # handling 1/2, 1/4 etc. numbers in ingredient list fro a recipe. 
        # also correcting the line break
        counter3 = -1
        for line in recipe2:
            counter3 +=1
            if(recipe2[counter3-1].isdigit() and recipe2[counter3-2].strip() != 'Servings:'):
                recipe2[counter3] = recipe2[counter3-1] + " " + recipe2[counter3]
                recipe2[counter3-1] = ''
            if(recipe2[counter3-1] == '½' or recipe2[counter3-1] == '¾' or recipe2[counter3-1] == '1 ¼' 
               or recipe2[counter3-1] == '¼'
               or recipe2[counter3-1] == '1 ½'  or recipe2[counter3-1] == '2 ½'  
               or recipe2[counter3-1] == '1½'):
                recipe2[counter3] = recipe2[counter3-1] + " " + recipe2[counter3]
                recipe2[counter3-1] = ''
            
        recipe3 = [line for line in recipe2 if line != '' ]
      
        loc_ptime = [] # start of receipe index search
        loc_pappt = [] # end of receipe index search
        counter = -1
        for line in recipe3:
            counter +=1
            if(line.strip() == ptime):
                loc_ptime.append(counter)
            for perapp_serv in pappt:
                if(perapp_serv in line.strip()):
                    loc_pappt.append(counter)
                    
        # handling for pages which have only one recipe pr 2 recipes
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
                recipe[counter4] = "-End of recipe-" # adding tag to denote end of a single recipe 
    
    start = []
    end = []
    
    # dividing 'recipe' to individaual recipes to be stored in 'recipe_store'
    for lno, line in enumerate(recipe):
        if(line.strip() == ptime):
            start.append(lno-1)
        if(line.strip() == "-End of recipe-"):
            end.append(lno)
    
    # initializing blank 2-d list
    recipe_store =[[] for i in range(len(start)-1)]
    
    # reading individual recipes into 'recipe_store'
    for i in range(0,(len(start)-1)):
        recipe_store[i]    
        for j in range(start[i], end[i]):
            recipe_store[i].append(recipe[j])
    
    # searching for a single recipe in 'recipe_store' as per ingredient provided by user
    recipe_number = []
    for i in range(0,(len(start)-1)):
        for j in range(0,(len(recipe_store[i])-1)):
            if (search_string.upper() in recipe_store[i][j].upper()):
                recipe_number.append(i)
                break
        if(len(recipe_number)>=3): #display maximum 3 recipes
            break
        
    get_recipe = []
    recipe_name=[]
    if(recipe_number != []):
        for i in recipe_number:
            get_recipe.append(recipe_store[i])
            recipe_name.append(recipe_store[i][0])
    
    recipe_info = ''
 
    # converting recipe to string for output
    if(recipe_number== []):
        recipe_info = 'Sorry! Receipe for ingredient not avaialble'
    else:
        for k in get_recipe:
            for i in k:
                recipe_info += i + "\n"
            recipe_info+= '\n******************************************\n'
    return((recipe_info), recipe_name)
