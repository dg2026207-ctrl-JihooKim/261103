#box(texture='')
box(opacity=0)
while True:
    rate(100)
    k = keysdown()
    if ' ' in k :
        box(color=color.red)
