from funciones import cuadrado_binomio

def test_cuadrado_binomio():
    """
    Prueba que la función cuadrado_binomio retorne correctamente los tres componentes:
    - a²
    - 2*a*b
    - b²
    """
    # Caso de prueba: (2 + 3)^2 = 4 + 12 + 9
    a = 2
    b = 3
    a_cuadrado, dos_ab, b_cuadrado = cuadrado_binomio(a, b)
    
    assert a_cuadrado == 4     # 2² = 4
    assert dos_ab == 12        # 2*2*3 = 12
    assert b_cuadrado == 9     # 3² = 9