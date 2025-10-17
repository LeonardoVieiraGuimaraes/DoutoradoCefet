# Conversão automática do notebook trabalho_arvores.ipynb para script Python
# Todas as células de código foram agrupadas sequencialmente

import matplotlib.pyplot as plt
import numpy as np
import random
import datetime
import os
from typing import Optional, List, Tuple
import sys

# Configurações do matplotlib
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
sys.setrecursionlimit(15000)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Criação automática de pastas
pastas_necessarias = [
    'relatorio/dados',
    'relatorio/graficos',
]
for pasta in pastas_necessarias:
    if not os.path.exists(pasta):
        os.makedirs(pasta, exist_ok=True)

# Classe BST
class NoArvoreBinariaPesquisa:
    def __init__(self, valor: int):
        self.valor = valor
        self.esquerda: Optional['NoArvoreBinariaPesquisa'] = None
        self.direita: Optional['NoArvoreBinariaPesquisa'] = None

class ArvoreBinariaPesquisa:
    def __init__(self):
        self.raiz: Optional[NoArvoreBinariaPesquisa] = None
        self.comparacoes = 0
    def inserir(self, valor: int) -> None:
        if self.raiz is None:
            self.raiz = NoArvoreBinariaPesquisa(valor)
            return
        atual = self.raiz
        while True:
            if valor < atual.valor:
                if atual.esquerda is None:
                    atual.esquerda = NoArvoreBinariaPesquisa(valor)
                    break
                else:
                    atual = atual.esquerda
            elif valor > atual.valor:
                if atual.direita is None:
                    atual.direita = NoArvoreBinariaPesquisa(valor)
                    break
                else:
                    atual = atual.direita
            else:
                break
    def buscar(self, valor: int) -> bool:
        self.comparacoes = 0
        return self._buscar_recursivo(self.raiz, valor)
    def _buscar_recursivo(self, no: Optional[NoArvoreBinariaPesquisa], valor: int) -> bool:
        if no is None:
            return False
        self.comparacoes += 1
        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)
        else:
            return self._buscar_recursivo(no.direita, valor)
    def obter_comparacoes(self) -> int:
        return self.comparacoes

# Classe AVL
class NoArvoreAVL:
    def __init__(self, valor: int):
        self.valor = valor
        self.esquerda: Optional['NoArvoreAVL'] = None
        self.direita: Optional['NoArvoreAVL'] = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz: Optional[NoArvoreAVL] = None
        self.comparacoes = 0
    def _altura(self, no: Optional[NoArvoreAVL]) -> int:
        return no.altura if no else 0
    def _fator_balanceamento(self, no: NoArvoreAVL) -> int:
        return self._altura(no.esquerda) - self._altura(no.direita)
    def _atualizar_altura(self, no: NoArvoreAVL) -> None:
        no.altura = 1 + max(self._altura(no.esquerda), self._altura(no.direita))
    def _rotacao_direita(self, y: NoArvoreAVL) -> NoArvoreAVL:
        x = y.esquerda
        T2 = x.direita
        x.direita = y
        y.esquerda = T2
        self._atualizar_altura(y)
        self._atualizar_altura(x)
        return x
    def _rotacao_esquerda(self, x: NoArvoreAVL) -> NoArvoreAVL:
        y = x.direita
        T2 = y.esquerda
        y.esquerda = x
        x.direita = T2
        self._atualizar_altura(x)
        self._atualizar_altura(y)
        return y
    def inserir(self, valor: int) -> None:
        self.raiz = self._inserir_recursivo(self.raiz, valor)
    def _inserir_recursivo(self, no: Optional[NoArvoreAVL], valor: int) -> NoArvoreAVL:
        if no is None:
            return NoArvoreAVL(valor)
        if valor < no.valor:
            no.esquerda = self._inserir_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir_recursivo(no.direita, valor)
        else:
            return no
        self._atualizar_altura(no)
        balance = self._fator_balanceamento(no)
        if balance > 1 and valor < no.esquerda.valor:
            return self._rotacao_direita(no)
        if balance < -1 and valor > no.direita.valor:
            return self._rotacao_esquerda(no)
        if balance > 1 and valor > no.esquerda.valor:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)
        if balance < -1 and valor < no.direita.valor:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)
        return no
    def buscar(self, valor: int) -> bool:
        self.comparacoes = 0
        return self._buscar_recursivo(self.raiz, valor)
    def _buscar_recursivo(self, no: Optional[NoArvoreAVL], valor: int) -> bool:
        if no is None:
            return False
        self.comparacoes += 1
        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)
        else:
            return self._buscar_recursivo(no.direita, valor)
    def obter_comparacoes(self) -> int:
        return self.comparacoes

# Funções auxiliares
def gerar_dados_ordenados(n: int) -> List[int]:
    return list(range(1, n + 1))

def gerar_dados_aleatorios(n: int, seed: int = None) -> List[int]:
    if seed is not None:
        random.seed(seed)
    numeros = random.sample(range(1, n * 2), n)
    return numeros

def executar_experimento(arvore_class, dados: List[int], elemento_busca: int) -> int:
    arvore = arvore_class()
    for valor in dados:
        arvore.inserir(valor)
    arvore.buscar(elemento_busca)
    return arvore.obter_comparacoes()

# Experimentos e gráficos podem ser executados sequencialmente
# Basta copiar as células de experimento e análise do notebook para este script
# Exemplo de uso:
# dados_ord = gerar_dados_ordenados(1000)
# dados_alea = gerar_dados_aleatorios(1000, seed=42)
# bst = ArvoreBinariaPesquisa()
# for v in dados_ord: bst.inserir(v)
# print(bst.buscar(10001), bst.obter_comparacoes())
