# ## Universidad de Costa Rica
# ### Escuela de Ingeniería Eléctrica
# #### IE0405 - Modelos Probabilísticos de Señales y Sistemas
#
# Primer semestre del 2021
#
# ---
#
# * Estudiante: **Luis Daniel Ferreto Chavarria**
# * Carné: **B82958**
# * Grupo: **1**
#
from PIL import Image
import numpy as np


def fuente_info(imagen):
    '''Una función que simula una fuente de
    información al importar una imagen y
    retornar un vector de NumPy con las
    dimensiones de la imagen, incluidos los
    canales RGB: alto x largo x 3 canales

    :param imagen: Una imagen en formato JPG
    :return: un vector de pixeles
    '''
    img = Image.open(imagen)

    return np.array(img)