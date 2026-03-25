dias_uteis = int(input('digite os dias uteis'))
horas_trab = float(input('digite as horas trabalhadas: '))
valor_horas = float(input('digite o valor da hora trabalhada: '))

jornada_devida = dias_uteis * 8
if horas_trab <= jornada_devida:
    salario = horas_trab * valor_horas
else: 
    horas_extras = horas_extras -valor_horas
    valor_hora_extra = valor_horas *horas_extras * 1.50
    print(f'hora extra: {horas_extras}')
    salario = jornada_devida * valor_horas + valor_hora_extra
    print(f'o salario é: {salario}')