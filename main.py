box(pos=vec(0,0,-0.1),color=color.yellow,size=vec(20,13,0.1))
while True:
    rate(100)
    k = keysdown()
    if ' ' in k :
        box(texture='https://i.postimg.cc/T1fFDfNy/unnamed.png',size=vec(1,1,0.1))
        box(color=color.white,pos=vec(-5,-5,0.2),size=vec(4,2,0.1))   
        box(color=color.white,pos=vec(5,-5,0.2),size=vec(4,2,0.1))
    
    if 'a' in k :
        box(color=color.blue,size=vec(20,13,0.1),pos=vec(0,0,0.4))
        box(color=color.white,pos=vec(-5,-5,0.5),size=vec(4,2,0.1))   
        box(color=color.white,pos=vec(5,-5,0.5),size=vec(4,2,0.1)) 
        if 'q' in k: 
            box(color=color.red,size=vec(20,13,0.1),pos=vec(0,0,0.6))
            box(color=color.white,pos=vec(-5,-5,0.7),size=vec(4,2,0.1))   
            box(color=color.white,pos=vec(5,-5,0.7),size=vec(4,2,0.1)) 
        if 'w' in k: 
            box(color=color.cyan,size=vec(20,13,0.1),pos=vec(0,0,0.6))
            box(color=color.white,pos=vec(-5,-5,0.7),size=vec(4,2,0.1))   
            box(color=color.white,pos=vec(5,-5,0.7),size=vec(4,2,0.1)) 
    if 'd' in k :
        box(color=color.green,size=vec(20,13,0.1))    
        box(color=color.white,pos=vec(-5,-5,0.7),size=vec(4,2,0.1))   
        box(color=color.white,pos=vec(5,-5,0.7),size=vec(4,2,0.1))
        if 'q' in k: 
            box(color=color.yellow,size=vec(20,13,0.1),pos=vec(0,0,0.6))
            box(color=color.white,pos=vec(-5,-5,0.7),size=vec(4,2,0.1))   
            box(color=color.white,pos=vec(5,-5,0.7),size=vec(4,2,0.1)) 
        if 'w' in k: 
             box(color=color.skyblue,size=vec(20,13,0.1),pos=vec(0,0,0.6))
             box(color=color.white,pos=vec(-5,-5,0.7),size=vec(4,2,0.1))   
             box(color=color.white,pos=vec(5,-5,0.7),size=vec(4,2,0.1))     
