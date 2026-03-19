"""
Queda Livre - Modelo Discreto com Euler
Salva dados de entrada, saída e gráficos em arquivos na pasta 'src/saida'.
"""
import numpy as np
import matplotlib.pyplot as plt
import os

def simular_queda_livre(H, V, g, dt, salvar_prefixo):
    # Listas para armazenar os resultados
    t_list, x_list, v_list, a_list = [0], [H], [V], [-g]
    t, x, v = 0, H, V
    while x > 0:
        t += dt
        x_novo = x + v * dt
        v_novo = v - g * dt
        # Corrige se passar do solo
        if x_novo < 0:
            x_novo = 0
        t_list.append(t)
        x_list.append(x_novo)
        v_list.append(v_novo)
        a_list.append(-g)
        x, v = x_novo, v_novo
    # Salva dados em txt
    np.savetxt(f"src/saida/{salvar_prefixo}_dados.txt", np.column_stack([t_list, x_list, v_list, a_list]),
               header="tempo(s)\tposicao(m)\tvelocidade(m/s)\taceleracao(m/s^2)", fmt="%.5f", delimiter="\t")
    return t_list, x_list, v_list, a_list

def plotar_graficos(t, x, v, a, salvar_prefixo):
    plt.figure()
    plt.plot(t, x, label="Posição (m)")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (m)")
    plt.title("Posição x Tempo")
    plt.grid()
    plt.savefig(f"src/saida/{salvar_prefixo}_posicao_tempo.png")
    plt.close()

    plt.figure()
    plt.plot(t, v, label="Velocidade (m/s)", color='orange')
    plt.xlabel("Tempo (s)")
    plt.ylabel("Velocidade (m/s)")
    plt.title("Velocidade x Tempo")
    plt.grid()
    plt.savefig(f"src/saida/{salvar_prefixo}_velocidade_tempo.png")
    plt.close()

    plt.figure()
    plt.plot(t, a, label="Aceleração (m/s²)", color='green')
    plt.xlabel("Tempo (s)")
    plt.ylabel("Aceleração (m/s²)")
    plt.title("Aceleração x Tempo")
    plt.grid()
    plt.savefig(f"src/saida/{salvar_prefixo}_aceleracao_tempo.png")
    plt.close()

def simular_com_resistencia_ar(H, V, g, dt, c, salvar_prefixo):
    t_list, x_list, v_list, a_list = [0], [H], [V], [-g + c*V]
    t, x, v = 0, H, V
    while x > 0:
        t += dt
        x_novo = x + v * dt
        a_novo = -g + c * v
        v_novo = v + a_novo * dt
        if x_novo < 0:
            x_novo = 0
        t_list.append(t)
        x_list.append(x_novo)
        v_list.append(v_novo)
        a_list.append(a_novo)
        x, v = x_novo, v_novo
    np.savetxt(f"src/saida/{salvar_prefixo}_dados.txt", np.column_stack([t_list, x_list, v_list, a_list]),
               header="tempo(s)\tposicao(m)\tvelocidade(m/s)\taceleracao(m/s^2)", fmt="%.5f", delimiter="\t")
    return t_list, x_list, v_list, a_list

def main():
    # Entradas padrão
    H = 100.0  # altura inicial (m)
    V = 0.0    # velocidade inicial (m/s)
    g = 9.81   # gravidade (m/s^2)
    dts = [1.0, 0.1, 0.01]  # diferentes passos de tempo

    # Simulação sem resistência do ar para diferentes dt
    for dt in dts:
        prefixo = f"queda_livre_dt{str(dt).replace('.', '_')}"
        t, x, v, a = simular_queda_livre(H, V, g, dt, prefixo)
        plotar_graficos(t, x, v, a, prefixo)

    # Simulação com resistência do ar (bônus)
    c = 0.1  # coeficiente de arrasto
    dt = 0.01
    prefixo = "queda_livre_ar"
    t, x, v, a = simular_com_resistencia_ar(H, V, g, dt, c, prefixo)
    plotar_graficos(t, x, v, a, prefixo)

    # Salva entradas usadas
    with open("src/saida/entradas.txt", "w") as f:
        f.write(f"H = {H} m\nV = {V} m/s\ng = {g} m/s^2\ndts = {dts}\nc (arrasto) = {c}\n")

if __name__ == "__main__":
    main()
