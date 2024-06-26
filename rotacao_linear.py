import numpy as np

def rotate_point(x, y, theta):
    # Converte o ângulo para radianos
    theta_rad = np.radians(theta)

    # Matriz de rotação
    rotation_matrix = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                                [np.sin(theta_rad), np.cos(theta_rad)]])

    # Ponto original como vetor coluna
    point = np.array([[x], [y]])

    # Aplica a rotação
    rotated_point = np.dot(rotation_matrix, point)

    # Retorna as coordenadas do ponto rotacionado
    return rotated_point[0, 0], rotated_point[1, 0]


# Solicita ao usuário que insira os valores
x_original = float(input('Digite a coordenada x do ponto original: '))
y_original = float(input('Digite a coordenada y do ponto original: '))
angulo_rotacao = float(input('Digite o ângulo de rotação em graus: '))

# Calcula as coordenadas do ponto rotacionado
x_rotacionado, y_rotacionado = rotate_point(x_original, y_original, angulo_rotacao)

# Exibe os resultados
print(f'Ponto original: ({x_original}, {y_original})')
print(f'Ponto rotacionado: ({x_rotacionado:.2f}, {y_rotacionado:.2f})')
