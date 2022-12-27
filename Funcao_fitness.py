import numpy
import math
from scipy.interpolate import interp1d
from scipy.optimize import fsolve
from scipy.interpolate import make_interp_spline, BSpline
import matplotlib.pyplot as plt

plt.style.use('bmh')

V = 0
omega = 0
dens_ar = 0
Vr = 0
Cl = 0
Cd = 0
sinb = 0
cosb = 0
r_loc = 0
gama_loc = 0
sigma_loc = 0


def main():

    helice1 = [[0.23, 0.16], [0.22, 0.17], [0.14, 0.06], [0.12, 0.06], [0.15, 0.08], [0.12, 0.08], [0.25, 0.14], [0.28, 0.08], [0.24, 0.14], [0.21, 0.15], [0.23, 0.17], [0.28, 0.1], [0.17, 0.18], [0.09, 0.16], [0.2, 0.16], [0.15, 0.19], [0.27, 0.18], [0.28, 0.07], [0.3, 0.12], [0.17, 0.17], [0.19, 0.2], [0.22, 0.19], [0.2, 0.2], [0.21, 0.16], [0.11, 0.19], [0.16, 0.18], [0.23, 0.16], [0.05, 0.15], [0.07, 0.09], [0.1, 0.14], [0.03, 0.16], [0.06, 0.12], [0.1, 0.19], [0.12, 0.15], [0.05, 0.2], [0.1, 0.19], [0.07, 0.14], [0.07, 0.16], [-0.01, 0.19], [-0.02, 0.16], [0.09, 0.19], [0.07, 0.18], [0.05, 0.18], [0.01, 0.1], [0.04, 0.18], [-0.03, 0.19], [-0.01, 0.18], [0.08, 0.19], [0.06, 0.19], [0.05, 0.07]]
    # helice1 = [[0.35, 0.157], [0.324, 0.153], [0.3, 0.149], [0.277, 0.146], 
    #         [0.257, 0.142], [0.238, 0.137], [0.22, 0.133], [0.204, 0.13], 
    #         [0.189, 0.126], [0.175, 0.122], [0.161, 0.118], [0.149, 0.115], 
    #         [0.138, 0.112], [0.127, 0.108], [0.117, 0.105], [0.107, 0.102], 
    #         [0.098, 0.1], [0.09, 0.097], [0.082, 0.094], [0.075, 0.092], 
    #         [0.068, 0.09], [0.061, 0.087], [0.055, 0.085], [0.049, 0.083], 
    #         [0.043, 0.081], [0.037, 0.079], [0.032, 0.078], [0.027, 0.076], 
    #         [0.023, 0.074], [0.018, 0.073], [0.014, 0.071], [0.01, 0.07], 
    #         [0.006, 0.068], [0.002, 0.067], [-0.002, 0.066], [-0.005, 0.064], 
    #         [-0.009, 0.063], [-0.012, 0.062], [-0.015, 0.061], [-0.018, 0.06], 
    #         [-0.021, 0.059], [-0.024, 0.058], [-0.026, 0.057], [-0.029, 0.056], 
    #         [-0.032, 0.055], [-0.034, 0.054], [-0.036, 0.053], [-0.039, 0.052], 
    #         [-0.041, 0.051], [-0.043, 0.05]]
    # fitness_grafico_potencia(helice1)
    # helice1 = [[0.28, 0.13], [0.25, 0.08], [0.3, 0.11], [0.23, 0.13], [0.2, 0.07], [0.08, 0.11], [0.27, 0.17], [0.26, 0.15], [0.03, 0.06], [0.23, 0.13], [0.15, 0.13], [0.27, 0.19], [0.27, 0.18], [0.2, 0.17], [0.22, 0.18], [0.1, 0.16], [0.22, 0.16], [0.24, 0.1], [0.07, 0.2], [0.15, 0.18], [0.25, 0.08], [0.15, 0.18], [0.17, 0.19], [0.1, 0.16], [0.04, 0.18], [0.03, 0.19], [0.17, 0.19], [0.15, 0.16], [0.02, 0.17], [0.08, 0.19], [0.03, 0.11], [0.09, 0.18], [0.11, 0.17], [0.0, 0.16], [0.08, 0.2], [0.02, 0.19], [0.01, 0.17], [0.09, 0.18], [0.09, 0.16], [0.1, 0.13], [0.07, 0.18], [0.08, 0.14], [0.05, 0.16], [0.07, 0.1], [0.07, 0.16], [-0.0, 0.17], [0.07, 0.2], [0.04, 0.11], [0.01, 0.14], [-0.02, 0.19]]
    
    # gerar_grafico_potencia(helice1)
    # print(fitness(helice1))
    
    # rkga
    # helice = [[0.29, 0.18], [0.26, 0.06], [0.27, 0.06], [0.27, 0.16], [0.29, 0.18], [0.29, 0.18], [0.26, 0.19], [0.27, 0.19], [0.26, 0.19], [0.26, 0.13], [0.25, 0.18], [0.28, 0.19], [0.18, 0.2], [0.2, 0.19], [0.19, 0.18], [0.29, 0.2], [0.12, 0.2], [0.1, 0.19], [0.21, 0.18], [0.13, 0.19], [0.21, 0.18], [0.14, 0.19], [0.17, 0.19], [0.06, 0.19], [0.15, 0.19], [0.15, 0.2], [0.07, 0.2], [0.14, 0.18], [0.14, 0.18], [0.06, 0.2], [0.03, 0.2], [0.1, 0.18], [0.12, 0.17], [0.1, 0.2], [0.08, 0.18], [0.07, 0.2], [0.12, 0.19], [0.06, 0.2], [0.09, 0.19], [0.1, 0.19], [0.06, 0.19], [0.06, 0.19], [0.05, 0.2], [0.06, 0.16], [0.03, 0.17], [0.04, 0.19], [0.03, 0.19], [0.05, 0.19], [0.04, 0.19], [0.03, 0.2]]
    # brkga
    helice = [[0.24, 0.07], [0.3, 0.12], [0.27, 0.13], [0.29, 0.2], [0.26, 0.09], [0.26, 0.19], [0.26, 0.19], [0.25, 0.18], [0.29, 0.17], [0.27, 0.17], [0.24, 0.18], [0.17, 0.2], [0.26, 0.2], [0.22, 0.19], [0.23, 0.2], [0.16, 0.19], [0.16, 0.18], [0.24, 0.2], [0.22, 0.19], [0.21, 0.19], [0.14, 0.18], [0.05, 0.19], [0.18, 0.16], [0.2, 0.19], [0.1, 0.18], [0.15, 0.19], [0.17, 0.2], [0.03, 0.16], [0.08, 0.19], [0.05, 0.2], [0.1, 0.2], [0.13, 0.18], [0.01, 0.2], [0.12, 0.17], [0.09, 0.18], [0.05, 0.19], [0.1, 0.19], [0.07, 0.19], [0.07, 0.18], [0.02, 0.18], [0.08, 0.19], [0.05, 0.18], [0.07, 0.19], [0.01, 0.18], [0.04, 0.18], [-0.02, 0.19], [0.04, 0.18], [0.06, 0.19], [0.04, 0.19], [0.02, 0.19]]
    for i in range(7, 26):
        valores_potencia(helice, i)
    
def valores_potencia(helice, vento):
    print(f'{vento} - {fitness_adaptado(helice, vento)}')


# def fitness_grafico_potencia(helice):
#     global V
#     global omega
#     global dens_ar

#     apartir = 4

#     V = 8  # velocidade do vento
#     omega = 634.56
#     #omega = 434.56
#     omega = omega * math.pi / 30  # velocidade da rotação de rpm para radianos
#     dens_ar = 1.225  # densidade do ar
#     potencias_obtidas = []

#     for vento in range(apartir, V + 1):
#         potencia_maxima = torque(helice, vento)
#         if potencia_maxima > 0:
#             potencias_obtidas.append(torque(helice, vento))
#         else:
#             potencias_obtidas.append(0)
            
#     print(max(potencias_obtidas))

#     T = numpy.array([i for i in range(apartir, V + 1)])
#     xnew = numpy.linspace(T.min(), T.max(), 300)

#     spl = make_interp_spline([i for i in range(apartir, V + 1)], potencias_obtidas, k=3)
#     power_smooth = spl(xnew)
#     plt.plot(xnew, power_smooth)
#     plt.title(f"Curva de Potência - Otimização a {V-13}m/s")
#     plt.ylabel("Potência (W)")
#     plt.xlabel("Velocidade do vento (m/s)")
#     fig1 = plt.gcf()
#     plt.draw()
#     fig1.savefig("graficos/curva_de_potencia")
#     plt.show()

#     return potencias_obtidas[-1]


def gerar_grafico_potencia(helice):
    global V
    global omega
    global dens_ar
    
    V = 12
    omega = 634.56
    omega = omega * math.pi / 40  # velocidade da rotação
    dens_ar = 1.225  # densidade do ar
    
    potencias_obtidas = []
    espaco_grafico = (4, 20)
    
    for vento in range(espaco_grafico[1]):
        potencia = torque(helice, vento)
        print(f'{vento} - {potencia}')
        if potencia > 0 and V <= vento:
            potencias_obtidas.append(potencia)
        else:
            #print(f'teste {vento}')
            potencias_obtidas.append(0)
            
    print(potencias_obtidas)
        
    T = numpy.array([i for i in range(espaco_grafico[1])])
    xnew = numpy.linspace(T.min(), T.max(), 300)
    
    spl = make_interp_spline([i for i in range(espaco_grafico[1])], potencias_obtidas, k=3)
    power_smooth = spl(xnew)
    plt.plot(xnew, power_smooth)
    plt.title(f"Curva de Potência - Otimização a {V}m/s")
    plt.ylabel("Potência (W)")
    plt.xlabel("Velocidade do vento (m/s)")
    fig1 = plt.gcf()
    plt.draw()
    fig1.savefig("graficos/curva_de_potencia")
    plt.show()

    return potencias_obtidas[-1]
    

def fitness_adaptado(helice, vento):
    global V
    global omega
    global dens_ar

    V = vento # velocidade do vento
    Omega = 634.56
    #Omega = 400.00
    omega = Omega * math.pi / 30  # velocidade da rotação de rpm para radianos
    dens_ar = 1.225  # densidade do ar

    potenciaMaxima = torque(helice, V)
    return potenciaMaxima

def fitness(helice):
    global V
    global omega
    global dens_ar

    V = 12 # velocidade do vento
    Omega = 634.56
    # Omega = 400.00
    omega = Omega * math.pi / 30  # velocidade da rotação de rpm para radianos
    dens_ar = 1.225  # densidade do ar

    potenciaMaxima = torque(helice, V)
    return potenciaMaxima


def torque(helice, V):
    global r_loc
    global sigma_loc
    global omega
    global gama_loc
    global Vr
    global sinb
    global cosb
    global Cl
    global Cd
    global dens_ar

    turbine_R = 0.752  # raio externo total da turbina
    turbine_r = 0.150  # raio menor do centro, do "hub"
    turbine_nsec = 50  # secções na qual dividiremos a pá
    turbine_nb = 3  # número de pás
    dr = (turbine_R - turbine_r) / (turbine_nsec - 1)  # calcular porção da turbina, tamanho
    alfa0 = 4.3 * math.pi / 180  # ângulo de ataque; quanto maior, maior a sustentação (até certo ponto); entre a\
    # linha de corda e o vento relativo médio

    r_loc = turbine_r
    vraio = r_loc
    T2 = 0

    for i in range(turbine_nsec):  # calculo dos esforços para cada secção

        betam = helice[i][0]
        sigma_loc = (turbine_nb * helice[i][1]) / (2 * math.pi * r_loc)
        gama_loc = betam + alfa0
        alnew = fsolve(movang, 0, V)
        dT = (helice[i][1]) * (Vr ** 2) * (Cl * sinb - Cd * cosb) * r_loc * dr  # calcula o torque da secção
        T2 = T2 + dT  # soma dos esforços para obter o torque total da pá, e consequentemente a potência

        vraio = vraio + dr
        r_loc = vraio

    T = ((turbine_nb * dens_ar) / 2) * T2
    VT = T * 0.65
    P = omega * VT  # ao multiplicar o torque total com omega, obtém-se a potência
    return P


def movang(al, V):
    global gama_loc
    global r_loc
    global sigma_loc
    global sinb
    global cosb
    global Cl
    global Cd
    global omega
    # global V
    global Vr

    Vt = omega * r_loc * (1 + al)
    Vr = numpy.sqrt(V * V + Vt * Vt)
    beta_n = numpy.arctan2(V, Vt)
    sinb = V / Vr
    cosb = Vt / Vr
    alfa = beta_n - gama_loc
    Cl, Cd = coeficiente3(alfa * 180 / math.pi)
    Cx = Cl * sinb - Cd * cosb

    return (sigma_loc * Cx / (4 * sinb * cosb)) - (al / (1 + al))


def coeficiente3(alfa):
    alfcl = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87,
             -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73,
             -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59,
             -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45,
             -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31,
             -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17,
             -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
             0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
             20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
             37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
             54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
             71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
             88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    vCd = [2.67325, 2.60541, 2.54955, 2.50378, 2.46621, 2.4368, 2.4163, 2.54573,
           2.5351, 2.53058, 3.3303, 3.32385, 3.32444, 3.33207, 3.19486, 3.21092,
           3.23346, 3.2632, 3.30115, 3.34874, 3.40787, 3.48132, 3.20274, 3.27807,
           3.37214, 3.13439, 3.23543, 3.03813, 3.16064, 2.99931, 3.11323, 2.93935,
           3.06754, 2.90794, 4.45573, 4.30893, 2.86227, 2.72519, 2.61061, 3.89052,
           3.79775, 3.72731, 3.71281, 3.62288, 3.54048, 3.17587, 3.10801, 3.1504,
           3.09545, 2.76322, 2.69254, 2.66428, 2.77313, 265.88517, 2.30827, 2.05748,
           2.00195, 1.74921, 1.69759, 1.59062, 1.51129, 1.35872, 1.30222, 1.23776,
           1.12469, 1.0591, 0.92169, 0.87545, 0.818, 0.77865, 0.69822, 0.62974,
           0.57499, 0.53524, 0.48189, 0.43464, 0.40046, 0.35818, 0.33021, 0.28745,
           0.26785, 0.23381, 0.20731, 0.18057, 0.16184, 0.14359, 0.12798, 0.11206,
           0.09789, 0.08584, 0.07528, 0.06591, 0.02518, 0.02243, 0.02087, 0.0195,
           0.01924, 0.01869, 0.01825, 0.01834, 0.01812, 0.01834, 0.01825, 0.01869,
           0.01924, 0.0195, 0.02087, 0.02243, 0.02518, 0.06591, 0.07528, 0.08584,
           0.09789, 0.11206, 0.12798, 0.14359, 0.16184, 0.18057, 0.20731, 0.23381,
           0.26785, 0.28745, 0.33021, 0.35818, 0.40046, 0.43464, 0.48189, 0.53524,
           0.57499, 0.62974, 0.69822, 0.77865, 0.818, 0.87545, 0.92169, 1.0591,
           1.12469, 1.23776, 1.30222, 1.35872, 1.51129, 1.59062, 1.69759, 1.74921,
           2.00195, 2.05748, 2.30827, 265.88517, 2.77313, 2.66428, 2.69254, 2.76322,
           3.09545, 3.1504, 3.10801, 3.17587, 3.54048, 3.62288, 3.71281, 3.72731,
           3.79775, 3.89052, 2.61061, 2.72519, 2.86227, 4.30893, 4.45573, 2.90794,
           3.06754, 2.93935, 3.11323, 2.99931, 3.16064, 3.03813, 3.23543, 3.13439,
           3.37214, 3.27807, 3.20274, 3.48132, 3.40787, 3.34874, 3.30115, 3.2632,
           3.23346, 3.21092, 3.19486, 3.33207, 3.32444, 3.32385, 2.53362, 2.53058,
           2.5351, 2.54573, 2.4163, 2.4368, 2.46621, 2.50378, 2.54955, 2.60541,
           2.67325]

    vCl = [-0.078, -0.077, -0.077, -0.076, -0.076, -0.076, -0.075, -0.075, -0.075,
           -0.075, -0.066, -0.066, -0.066, -0.066, -0.066, -0.067, -0.067, -0.067,
           -0.068, -0.068, -0.069, -0.07, -0.07, -0.071, -0.072, -0.073, -0.074,
           -0.075, -0.077, -0.078, -0.079, -0.081, -0.083, -0.084, -0.086, -0.088,
           -0.091, -0.093, -0.095, -0.098, -0.101, -0.104, -0.107, -0.111, -0.115,
           -0.119, -0.123, -0.128, -0.133, -0.139, -0.145, -0.151, -0.158, -0.165,
           -0.174, -0.182, -0.192, -0.202, -0.213, -0.225, -0.238, -0.253, -0.269,
           -0.286, -0.304, -0.325, -0.347, -0.372, -0.399, -0.428, -0.46, -0.494,
           -0.532, -0.573, -0.617, -0.664, -0.713, -0.765, -0.818, -0.87, -0.911,
           -0.945, -0.975, -0.998, -1.013, -1.018, -1.013, -0.996, -0.967, -0.926,
           -0.875, -0.813, -0.886, -0.807, -0.705, -0.593, -0.478, -0.36, -0.24,
           -0.12, 0, 0.12, 0.24, 0.36, 0.478, 0.593, 0.705, 0.807, 0.886, 0.813,
           0.875, 0.926, 0.967, 0.996, 1.013, 1.018, 1.013, 0.998, 0.975, 0.945,
           0.911, 0.87, 0.818, 0.765, 0.713, 0.664, 0.617, 0.573, 0.532, 0.494,
           0.46, 0.428, 0.399, 0.372, 0.347, 0.325, 0.304, 0.286, 0.269, 0.253,
           0.238, 0.225, 0.213, 0.202, 0.192, 0.182, 0.174, 0.165, 0.158, 0.151,
           0.145, 0.139, 0.133, 0.128, 0.123, 0.119, 0.115, 0.111, 0.107, 0.104,
           0.101, 0.098, 0.095, 0.093, 0.091, 0.088, 0.086, 0.084, 0.083, 0.081,
           0.079, 0.078, 0.077, 0.075, 0.074, 0.073, 0.072, 0.071, 0.07, 0.07,
           0.069, 0.068, 0.068, 0.067, 0.067, 0.067, 0.066, 0.066, 0.066, 0.066,
           0.075, 0.075, 0.075, 0.075, 0.075, 0.076, 0.076, 0.076, 0.077, 0.077,
           0.078]

    Cd = interp1d(alfcl, vCd, fill_value="extrapolate")(alfa)
    Cl = interp1d(alfcl, vCl, fill_value="extrapolate")(alfa)

    return Cl * .8, Cd * .8


if __name__ == "__main__":
    main()

