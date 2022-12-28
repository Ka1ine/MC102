valor_hora = int(input())
dias_trabalhados = int(input())
extra = 0
horas_trabalhadas = 0
horas_semana = 0

for i in range(dias_trabalhados):
    registro_dia = int(input())
    horas_dia = 0
    for j in range(registro_dia):
        hora_inicio = int(input())
        hora_fim = int(input())

        horas_dia += hora_fim - hora_inicio

    if horas_dia > 8:
        horas_extra = horas_dia - 8
        extra += horas_extra

    horas_trabalhadas += horas_dia
    horas_semana = horas_trabalhadas - extra

if horas_semana > 44:
    horas_extra = horas_semana - 44
    extra += horas_extra

valor_semana = horas_trabalhadas * valor_hora
valor_extra = extra * (valor_hora*0.5)
valor_total = valor_semana + valor_extra

print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", extra)
print("Valor devido: R$ {:0.2f}".format(valor_total))




