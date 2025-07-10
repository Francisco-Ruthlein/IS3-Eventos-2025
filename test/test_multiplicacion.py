from funciones import multiplicacion

def test_multiplicacion_positivos():
    assert multiplicacion(4, 5) == 20

def test_multiplicacion_por_cero():
    assert multiplicacion(7, 0) == 0