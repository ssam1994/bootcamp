import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

def xa_to_diameter(xa):
    '''
    Convert an array of cross-sectional areas
    to diameters with commensurate units
    '''
    # Compute diameter from
    diameter = np.sqrt(xa * 4 /np.pi)
    return diameter

def easy_reshape(obj, ncols, order='C'):
    '''
    Guarantee reshaping works by defining only one shape parameter
    '''

    arr = np.reshape(obj, (ncols, len(obj)/ncols), order)
    return arr
