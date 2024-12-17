# Trabalho Sinais e Sistemas - Diagrama de Bode Filtro Passa Faixa
# Luana Fujikawa Roysen - NUSP: 13677010
# Maria Clara Monteiro de Almeida Ferreira - NUSP: 13676951

import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

# Pede para o usuário o valor das resistências e capacitâncias do circuito e a frequência
# máxima que o diagrama deve ir. 
r_alta = float(input('Insira o resistor do filtro passa alta:')) 
c_alta = float(input('Insira o capacitor do filtro passa alta:'))
r_baixa = float(input('Insira o resistor do filtro passa baixa:'))
c_baixa = float(input('Insira o capacitor do filtro passa baixa:'))
f_max = float(input('Insira a frequência máxima a ser mostrada no formato log ex: 1e12:'))

# Divide os valores entre denominador e numerador para que se possa calcular a
# função de transferência
num = r_alta*c_alta
dem1 = r_alta*r_baixa*c_alta*c_baixa
dem2 = r_baixa*c_baixa + c_alta*r_alta

numerador = [num, 0]
denominador = [dem1, dem2 ,1]

sys = signal.TransferFunction(numerador, denominador)

# Faixa personalizada com mais pontos e frequência
frequencia_min = 0.1  # Frequência mínima [rad/s]
frequencia_max = f_max # Frequência máxima [rad/s]
num_pontos = 5000  # Mais pontos para maior resolução

# Faz o diagrama de bode da função de transferência com o número de pontos especificado
w = np.logspace(np.log10(frequencia_min), np.log10(frequencia_max), num_pontos)
w, mag, phase = signal.bode(sys, w=w)

# Plota o gráfico de magnitude
plt.figure()
plt.semilogx(w, mag)  # Magnitude
plt.title('Diagrama de Bode - Magnitude')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude [dB]')
plt.grid()

# Ajustando os limites dos eixos
plt.xlim(1e-1, f_max)  # Intervalo no eixo x (frequência)
plt.ylim(-60, 20)  # Intervalo no eixo y (magnitude em dB)

# Plota o gráfico de fase
plt.figure()
plt.semilogx(w, phase)  # Fase
plt.title('Diagrama de Bode - Fase')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Fase [graus]')
plt.grid()

plt.show()

