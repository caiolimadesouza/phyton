gols_time_a = int(input('digite os gols: '))
gols_time_b = int(input('digite os gols: '))

if gols_time_a > gols_time_b:
    print('time A venceu o jogo')
    print(f'{gols_time_a} X {gols_time_b}')
else:
    if gols_time_b > gols_time_a:
        print('time B venceu o jogo')
        print(f'{gols_time_b} X {gols_time_a}')
    else: 
        print('o jogo empatou')
        print(f'{gols_time_a} X {gols_time_b}')
        