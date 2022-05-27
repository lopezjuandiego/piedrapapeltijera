import random

def play ():
    user = input("Elegí 'Piedra', 'Papel', o 'Tijera':\n" ).lower()
    pc = random.choice(['piedra', 'papel', 'tijera'])
    
    if user == pc:
        return 'Empate'
    
    if gano (user, pc):
        return f'Ganaste, la compu eligió {pc}' 
    
    return f'Perdiste la compu eligió {pc}' 

def gano (player, op):
    if (player == 'Piedra' and op == 'tijera')  or (player == 'tijera' and op == 'papel') or (player == 'papel' and op == 'piedra'):
        return True
    
print(play())