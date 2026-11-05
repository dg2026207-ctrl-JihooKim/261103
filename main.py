box(pos=vec(0,0,-0.1),color=color.yellow,size=vec(20,13,0.1))
while True:
    rate(100)
    k = keysdown()
    if ' ' in k :
        box(color=color.red,size=vec(20,13,0.1))
        box(color=color.white,pos=vec(-5,-5,0.2),size=vec(4,2,0.1))   
        box(color=color.white,pos=vec(5,-5,0.2),size=vec(4,2,0.1))
    if 'o' in k :
        box(color=color.blue,size=vec(20,13,0.6))
    if 'x' in k :
        box(color=color.green,size=vec(20,13,0.6))    
