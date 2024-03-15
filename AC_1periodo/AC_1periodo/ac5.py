""" 
AC5: Aventureiro vs Monstro

"""
import random

def main():
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)

    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)

    print(f'Aventureiro - Vida: {vida_aventureiro}, Ataque: {ataque_aventureiro}, Defesa: {defesa_aventureiro}')
    print(f'Monstro - Vida: {vida_monstro}, Ataque: {ataque_monstro}')
    
    rodada = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        print(f'\nRodada {rodada}:')
        
        dano_ataque_aventureiro = random.randint(1, ataque_aventureiro)
        vida_monstro -= dano_ataque_aventureiro
        print(f'O aventureiro atacou o monstro causando {dano_ataque_aventureiro} de dano.')

        if vida_monstro <= 0:
            print('O monstro morreu!')
            break

        dano_ataque_monstro = random.randint(1, ataque_monstro) - defesa_aventureiro
        if dano_ataque_monstro < 0:
            dano_ataque_monstro = 0
        vida_aventureiro -= dano_ataque_monstro
        print(f'O monstro atacou o aventureiro causando {dano_ataque_monstro} de dano.')

        if vida_aventureiro <= 0:
            print('O aventureiro morreu!')

        rodada += 1

    print('\nAtributos finais:')
    print(f'Aventureiro - Vida: {vida_aventureiro}, Ataque: {ataque_aventureiro}, Defesa: {defesa_aventureiro}')
    print(f'Monstro - Vida: {vida_monstro}, Ataque: {ataque_monstro}')

main()