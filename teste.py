from datetime import datetime, timedelta

# definição do periodo noturno
HORARIO_NOTURNO_INICIO = 22 * 60  # 22:00 em minutos (1320)
HORARIO_NOTURNO_FIM = 5 * 60  # 05:00 em minutos (300)

# converter HH:MM para minutos do dia
def converter_horas(tempo):
    if not tempo or ":" not in tempo:
        return None
    try:
        h, m = map(int, tempo.split(":"))
        return h * 60 + m
    except ValueError:
        return None

# função para calcular o tempo total trabalhado e separar as horas noturnas corretamente
def calcular_horas(entrada, intervalo, retorno, saida):
    entrada_min = converter_horas(entrada)
    intervalo_min = converter_horas(intervalo)
    retorno_min = converter_horas(retorno)
    saida_min = converter_horas(saida)

    if None in [entrada_min, intervalo_min, retorno_min, saida_min]:
        return "Erro: Horários inválidos."

    # ajuste para a virada do dia
    if intervalo_min < entrada_min:
        intervalo_min += 1440
    if retorno_min < intervalo_min:
        retorno_min += 1440
    if saida_min < retorno_min:
        saida_min += 1440

    # calcula o total de horas trabalhadas 
    total_trabalhado = (intervalo_min - entrada_min) + (saida_min - retorno_min)

    # Calcula o tempo trabalhado dentro do período noturno (22h-05h)
    def calcular_horas_noturnas(inicio, fim):
        minutos_noturnos = 0

        # Se o período cruza a meia-noite, ajustamos os minutos corretamente
        if fim < inicio:
            fim += 1440  # Adicionamos 24h em minutos

        for minuto in range(inicio, fim):
            minuto_do_dia = minuto % 1440  # Garante que fique dentro do ciclo de 24h
            if HORARIO_NOTURNO_INICIO <= minuto_do_dia or minuto_do_dia < HORARIO_NOTURNO_FIM:
                minutos_noturnos += 1

        return minutos_noturnos

    horas_noturnas_reais = calcular_horas_noturnas(entrada_min, intervalo_min) + calcular_horas_noturnas(retorno_min, saida_min)

    # Aplica a prorrogação corretamente se necessário
    if entrada_min <= (23 * 60 + 59) and saida_min > HORARIO_NOTURNO_FIM:
        horas_noturnas_reais = saida_min - HORARIO_NOTURNO_INICIO

    # Converte as horas noturnas reais para computadas (52m30s por hora)
    horas_noturnas_computadas = (horas_noturnas_reais * 60) / 52.5

    # Horas Normais = Total trabalhado
    horas_normais = total_trabalhado

    # Convertendo para formato HH:MM
    def formatar_horas(minutos):
        horas = max(0, int(minutos // 60))  # Garante que nunca seja negativo
        minutos_restantes = max(0, int(minutos % 60))
        return f"{horas:02d}:{minutos_restantes:02d}"

    return {
        "Horas Normais": formatar_horas(horas_normais),
        "Horas Noturnas Computadas": formatar_horas(horas_noturnas_computadas)
    }

# Entrada de dados para 7 dias
total_horas_normais = 0
total_horas_noturnas_computadas = 0

print("Calculadora de Horas Trabalhadas (Semanal)")

for i in range(7):  # 7 dias da semana
    print(f"\nDia {i + 1}")

    data = input("Digite a data (DD/MM/AAAA): ")
    entrada = input("Digite o horário de entrada (HH:MM): ")
    intervalo_inicio = input("Digite o horário de início do intervalo (HH:MM): ")
    intervalo_fim = input("Digite o horário de término do intervalo (HH:MM): ")
    saida = input("Digite o horário de saída (HH:MM): ")

    resultado = calcular_horas(entrada, intervalo_inicio, intervalo_fim, saida)

    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"Data: {data}")
        print(f"Horas Normais: {resultado['Horas Normais']}")
        print(f"Horas Noturnas Computadas: {resultado['Horas Noturnas Computadas']}")

        # Somar os valores semanais
        total_horas_normais += converter_horas(resultado["Horas Normais"])
        total_horas_noturnas_computadas += converter_horas(resultado["Horas Noturnas Computadas"])

# Exibir resumo final da semana
print("\nResumo Semanal")
print(f"Total de Horas Normais: {total_horas_normais // 60:02d}:{total_horas_normais % 60:02d}")
print(f"Total de Horas Noturnas Computadas: {total_horas_noturnas_computadas // 60:02d}:{total_horas_noturnas_computadas % 60:02d}")
