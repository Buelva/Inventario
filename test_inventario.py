from inventario import registrar_producto
import pytest

def test_registrar_producto():
    inventario = {}
    registrar_producto(inventario, 1, "Teclado", 10)
    assert inventario[1]["nombre"] == "Teclado"

def test_registrar_producto_repetido():
    inventario = {}
    registrar_producto(inventario, 1, "Teclado", 10)

    with pytest.raises(ValueError): # se utiliza with pytest.raises para with espere un error de ValueError
        registrar_producto(inventario, 1, "Leche", 20)