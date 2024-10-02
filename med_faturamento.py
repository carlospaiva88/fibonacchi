import json

faturamento_json = '''
{
    "faturamento": [1000, 2000, 0, 3000, 0, 500, 0, 4000, 0, 1000, 2500]
}
'''

# Carrega os dados
dados = json.loads(faturamento_json)
faturamento = [valor for valor in dados['faturamento'] if valor > 0]  # Ignorar dias com faturamento 0

# Cálculos
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_media = len([dia for dia in faturamento if dia > media_mensal])

print(f"Menor faturamento: R${menor_faturamento}")
print(f"Maior faturamento: R${maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
