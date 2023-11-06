def filesize(file):
    # x = file.size
    x = file
    
    if x!=0:
       
        if x<=1024*2:
            value = x/1024
            ext = ' KB'
            
        elif x<=1024*3:
            value = x/(1024*2)
            ext = ' MB'
            
        elif x<=1024*4:
            value = x/(1024*3)
            ext = ' GB'
        else:
            value = x/(1024*4)
            ext = ' TB'
            
        return [str(value)+ext,True]
    else:
        return ['',False]

print(filesize(int(input('enter any number: ')))[0])