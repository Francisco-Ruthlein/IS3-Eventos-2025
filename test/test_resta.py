from funciones import resta

def test_resta_positivos():
    assert resta(10, 4) == 6

def test_resta_negativos():
    assert resta(-5, -3) == -2