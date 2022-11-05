"""
    Funciones para el notebook @simulacion_va.ipynb
    
    @Author: Jorge Iván Reyes Hernández
"""
import numpy as np


def pseudo_uniform(p: int = (2**43) - 1,
                   m: int = 321456,
                   seed: int = 1234567890,
                   size: int = 1):
  """
  :param p: módulo. Se elige un número primo muy grande.
  :param m: magnitud.
  :param seed: Semilla para generar el valor inicial.
  :param size: tamaño de la muestra.
  """
  # Arreglo de tamaño @param:size para guardar los números generados
  U = np.zeros(size)
  X = (seed * m + 1) % p
  U[0] = X / p

  for i in range(1, size):
    X = (X * m + 1) % p
    U[i] = X / p

  return U