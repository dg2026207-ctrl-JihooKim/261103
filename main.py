#box(texture='')
While True:
    rate(100)
    k = keysdown()
    if ' ' in k :
        box(color=color.red)
