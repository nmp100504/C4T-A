a = [1,2,3,4,5]
b = []
c = []

def move(n,cot_xp,cot_tg,cot_dich):
    if n == 1 :
        cot_dich.insert(0,cot_xp.pop(0))     
    else:
        move(n-1,cot_xp,cot_dich,cot_tg)
        cot_dich.insert(0,cot_xp.pop(0))
        move(n-1,cot_tg,cot_xp,cot_dich)

move(5,a,b,c)
print(a,b,c)

