# 3ª Avaliação - Trabalho Prático: Caixeiro Viajante

**Data de Entrega:** 31 de julho de 2025 (quinta-feira)  
**Valor:** 37 pontos

## Objetivo
Implementar algoritmo de força bruta e uma heurística para o problema do Caixeiro Viajante (TSP).

O trabalho é composto de duas partes:
- Aplicação do algoritmo de força-bruta em instâncias do problema do caixeiro viajante.
- Aplicação de uma heurística em três instâncias do mesmo problema.

O problema do Caixeiro Viajante consiste em, dado um conjunto de cidades onde existe um caminho entre cada par de cidades com uma distância positiva, encontrar um caminho que, a partir de uma cidade, visita todas as cidades e retorna à cidade inicial percorrendo a menor distância possível.

## Parte 1: Força Bruta
1. Implementar o método de força bruta para solucionar o problema, determinando todas as possíveis rotas e escolhendo a menor.
2. Gerar instâncias de tamanho 2 até n e aplicar o método implementado.
3. Computar o tempo de execução durante a aplicação da força-bruta em cada instância gerada. A aplicação deve ser realizada em quantas instâncias forem possíveis (o tamanho máximo gira em torno de 10 a 14 cidades).
   - As instâncias devem ser geradas automaticamente, com pesos aleatórios.
   - Pode-se utilizar qualquer tipo de representação de grafo.

## Parte 2: Heurística
1. Implementar uma heurística para encontrar uma solução para o TSP (livre escolha da heurística).
2. Aplicar a heurística nas três instâncias disponíveis no moodle:
   - **si535.tsp**: 535 cidades, matriz de adjacência (apenas diagonal superior).
   - **pa561.tsp**: 561 cidades, matriz de adjacência (apenas diagonal inferior).
   - **si1032.tsp**: 1032 cidades, matriz de adjacência (apenas diagonal superior).
3. Verificar a distância calculada pela heurística.

## Entrega
- Postar no moodle o código fonte das implementações, comentados.
- Relatório via moodle contendo:
  - Gráfico mostrando o crescimento exponencial do tempo necessário para resolver o TSP pelo crescimento do tamanho do problema (força-bruta).
  - Distância encontrada pela heurística para cada uma das instâncias disponíveis no moodle.

**Bom trabalho!**
