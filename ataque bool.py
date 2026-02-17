hp = 3
heisSword = False
HeisShield = False
attackedbyanEnemy = True
attackedbyaFlow = True
damagefromEnemy = attackedbyanEnemy and (not heisSword)
damagefromArrow = attackedbyaFlow and (not HeisShield) 

if(attackedbyanEnemy and (not heisSword)):
    
    hp = hp -1
    print(f'tus vidas ahoras son {hp}')
else: 
    print("Ganastes unas monedas")
if(attackedbyaFlow and (not HeisShield)):

    hp = hp -1
    print(f'tus vidas ahoras son {hp}')
else: 
    print("Ganastes unas monedas")


if(damagefromEnemy or damagefromArrow):
    hp = hp -1
    print(f'tus vidas ahoras son {hp}')


if(hp == 0):
    print("MORISTES")


