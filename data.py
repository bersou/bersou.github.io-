# Dados das paradas mensais
mdf1_paradas = [
    {"tempo": "15:48:00", "descricao": "MANUTENÇÃO NO VENTILADOR DA FIBRA REJEITADA", "impacto": 495},
    {"tempo": "08:30:00", "descricao": "QUEDA DE ENERGIA", "impacto": 265},
    {"tempo": "07:00:00", "descricao": "ROSCA DE EXTRAÇÃO TRANCADA NO DIGESTOR / VALVULA DE SAIDA SEM MOVIMENTO", "impacto": 224}
]

mdf2_paradas = [
    {"tempo": "31:14:00", "descricao": "MANUTENÇÃO DA CINTA DA PRENSA", "impacto": 880},
    {"tempo": "19:36:00", "descricao": "MANUTENÇÃO NO VENTILADOR DO ÓLEO TERMICO DA USINA", "impacto": 198},
    {"tempo": "06:59:00", "descricao": "FALHA DE TRANSDUTOR DE DISTANCIA E ALGORITMO NA PRENSA", "impacto": 190}
]

mdf1_repetidas = [
    {"descricao": "DIVERT VALVULE NÃO VIRA PARA SECADOR AO ARRANCAR LINHA", "duracao": "56 MINUTOS"},
    {"descricao": "DESALINHAMENTO TC 45 E SENSOR DE ROTAÇÃO", "duracao": "4:15 HORAS"},
    {"descricao": "PRESSÃO BAIXA NA USINA QUEDA DA BORRACHA DO CHUT DA MOEGA EMBUCHANDO TC 27", "duracao": "2:32 HORAS"}
]

mdf2_repetidas = [
    {"descricao": "PRESSÃO E TREMPERATURA BAIXA NA USINA DEVIDO AO CARACOL DAS ROSCAS DA MOEGA COM DESGASTE", "duracao": "10:00 HORAS"},
    {"descricao": "TRANSDUTOR DE DISTANCIA DA PRENSA", "duracao": "7:00 HORAS"},
    {"descricao": "PRESSÃO BAIXA NAS BOM BAS DO ÓLEO HIDRAULICO DA PRENSA", "duracao": "1:02 HORAS"}
]

# Dados para o gráfico de pizza de paradas repetidas
paradas_repetidas_dados = {
    'descricao': [
        'Divert Valvule',
        'Desalinhamento TC 45',
        'Pressão Baixa na Usina',
        'Pressão e Temperatura Baixa',
        'Transdutor de Distância',
        'Pressão Baixa nas Bombas'
    ],
    'horas': [0.93, 4.25, 2.53, 10, 7, 1.03]
}
