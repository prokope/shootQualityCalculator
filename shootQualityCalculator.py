import math

    # Declaração de variáveis
def shoot_quality():
    coord_x_list = []
    coord_y_list = []
    euclidean_distance_list = []
    euclidean_calc = 0
    dmmax2 = 45.18
    dmmax3 = 38.73
    dmmax4 = 35.10
    dmmax5 = 32.55
    iqt = 0
    shoot_quantity = int(input('Informe a quantidade de tiros que impactaram o alvo: '))
    montante = 0
    resultado = "Não selecionado"

    # Recebendo a quantidade de tiros na silhueta

    while shoot_quantity < 1 or shoot_quantity > 5:
        shoot_quantity = int(input('Erro. Digite a quantidade de tiros que impactaram o alvo entre 2 e 5: '))

    # Recebendo as coordenadas de cada tiro acertado na silhueta

    if shoot_quantity != 1:
        for counter in range(0, shoot_quantity):
            print(f'Tiro {counter + 1}: ')
            coord_x_list.append(float(input('Informe coordenada de linha (X): ')))
            coord_y_list.append(float(input('Informe coordenada de linha (Y): ')))
            print('-----------------------------')

        # Calculando a distância euclidiana

        for shootFirst in range(0, shoot_quantity):
            for shootSecond in range(shootFirst + 1, shoot_quantity):
                euclidean_calc = math.sqrt(math.pow(coord_x_list[shootFirst] - coord_x_list[shootSecond], 2) + math.pow(coord_y_list[shootFirst] - coord_y_list[shootSecond], 2))
                euclidean_distance_list.append(euclidean_calc)

        for counter in range(0, len(euclidean_distance_list)):
            montante += euclidean_distance_list[counter]  # Somando resultados da lista
        dm_shoot = montante / len(euclidean_distance_list)  # Média dos resultados

        # Cálculo de Índice de Qualidade de Tiro
        if shoot_quantity == 2:
            iqt = (1000 * (shoot_quantity / 5) * (1 - (dm_shoot / dmmax2)))
        elif shoot_quantity == 3:
            iqt = (1000 * (shoot_quantity / 5) * (1 - (dm_shoot / dmmax3)))
        elif shoot_quantity == 4:
            iqt = (1000 * (shoot_quantity / 5) * (1 - (dm_shoot / dmmax4)))
        elif shoot_quantity == 5:
            iqt = (1000 * (shoot_quantity / 5) * (1 - (dm_shoot / dmmax5)))


        #  Resultados
        if iqt >= 850:
            resultado = "Selecionado"
        elif iqt < 850 and iqt >= 700:
            resultado = "Nova oportunidade"
        else:
            resultado = "Não Selecionado"
    print(f'TIROS: 5\nIMPACTOS: {shoot_quantity}\nÍNDICE DE QUALIDADE DO TIRO: {iqt:.2f}\nRESULTADO: {resultado}')


shoot_quality()
