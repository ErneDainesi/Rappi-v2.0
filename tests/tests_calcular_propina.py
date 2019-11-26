import unittest
from pedido_manual import calcular_propina_rappitendero


class TestsCalcularPropina(unittest.TestCase):
    def test_calcular_propina_quinientos(self):
        resultado_esperado = 25
        resultado = calcular_propina_rappitendero(500)
        self.assertEqual(resultado, resultado_esperado)

    def test_calcular_propina_un_millon(self):
        resultado_esperado = 50000
        resultado = calcular_propina_rappitendero(1000000)
        self.assertEqual(resultado, resultado_esperado)

if __name__ == '__main__':
    unittest.main()
