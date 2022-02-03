#projeto calcula intensidade dos veteores e soma vetorial#
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
print(f'------------------------------CALCULADORA DE SOMA VETORIAL EM 3 DIMENSÕES------------------------------')
Iniciar = input('Deseja efetuar uma soma vetorial ? Sim/não ')
Iniciar = Iniciar.lower()
if Iniciar == 'sim':
    vetor1 = float(input('Insira a intensidade do Vetor 1 '))
    print("Insira os ângulos diretores(em relação ao sentido anti-horário)")
    α1 = float(input('α : '))
    β1 = float(input('β : '))
    γ1 = float(input('γ : '))
    x1 = math.cos(math.radians(α1)) * vetor1
    y1 = math.cos(math.radians(β1)) * vetor1
    z1 = math.cos(math.radians(γ1)) * vetor1

    vetor2 = float(input('Insira a intensidade do Vetor 2 '))
    print("Insira os ângulos diretores (em relação ao sentido anti-horário)")
    α2 = float(input('α : '))
    β2 = float(input('β : '))
    γ2 = float(input('γ : '))
    x2 = math.cos(math.radians(α2)) * vetor2
    y2 = math.cos(math.radians(β2)) * vetor2
    z2 = math.cos(math.radians(γ2)) * vetor2

    vetor3 = float(input('Insira a intensidade do Vetor 3 '))
    print("Insira os ângulos diretores(em relação ao sentido anti-horário)")
    α3 = float(input('α : '))
    β3 = float(input('β : '))
    γ3 = float(input('γ : '))
    x3 = math.cos(math.radians(α3)) * vetor3
    y3 = math.cos(math.radians(β3)) * vetor3
    z3 = math.cos(math.radians(γ3)) * vetor3

    print(f'\n------------Dados sobre os vetores fornecidos------------')
    print(f'\nVetor 1  '
          f'\nMódulo do vetor= {vetor1}'
          f'\nÂngulos diretores= α={α1} β={β1} γ={γ1} '
          f'\nDecomposição vetorial= {x1:.1f}i {y1:.1f}j {z1:.1f}k\n')

    print(f'\nVetor 2  '
          f'\nMódulo do vetor= {vetor2}'
          f'\nÂngulos diretores= α={α2} β={β2} γ={γ2} '
          f'\nDecomposição vetorial= {x2:.1f}i {y2:.1f}j {z2:.1f}k\n')

    print(f'\nVetor 3  '
          f'\nMódulo do vetor= {vetor3}'
          f'\nÂngulos diretores= α={α3} β={β3} γ={γ3} '
          f'\nDecomposição vetorial= {x3:.1f}i {y3:.1f}j {z3:.1f}k\n')

    vetor_resultante_x = x1 + x2 + x3
    vetor_resultante_y = y1 + y2 + y3
    vetor_resultante_z = z1 + z2 + z3
    vetor_resultante = (vetor_resultante_x)**2 + \
        (vetor_resultante_y)**2+(vetor_resultante_z)**2
    vetor_resultante = math.sqrt(vetor_resultante)
    α4 = math.acos(vetor_resultante_x/vetor_resultante)
    α4 = math.degrees(α4)
    β4 = math.acos(vetor_resultante_y/vetor_resultante)
    β4 = math.degrees(β4)
    γ4 = math.acos(vetor_resultante_z/vetor_resultante)
    γ4 = math.degrees(γ4)

    print(f'\n------------Vetor resultante------------')
    print(f'\nVetor Resultante  '
          f'\nMódulo do vetor= {vetor_resultante:.1f}'
          f'\nÂngulos diretores= α={α4:.1f} β={β4:.1f} γ={γ4:.1f} '
          f'\nDecomposição vetorial= {vetor_resultante_x:.0f}i {vetor_resultante_y:.0f}j {vetor_resultante_z:.0f}k\n')


elif Iniciar == 'não':
    print('Operação encerrada')
else:
    print('Operação inválida')


figura = plt.figure()
grafico = figura.gca(projection='3d')
z = np.linspace(0, vetor_resultante_z, 200)
y = np.linspace(0, vetor_resultante_y, 200)
x = np.linspace(0, vetor_resultante_x, 200)
#x = z * np.sin(y)


grafico.plot(x, y, z, color='purple')

plt.show()
