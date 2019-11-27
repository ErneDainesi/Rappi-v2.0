import unittest
from pedido_manual import calcular_rappicreditos_ganados


class TestCalcularRappicreditos(unittest.TestCase):
    def test_calcular_rappicreditos_ganados_importe_menor_a_doscientos(self):
        resultado = calcular_rappicreditos_ganados(100)
        resultado_esperado = 5
        self.assertEqual(resultado_esperado, resultado)

    def test_calcular_rappicreditos_ganados_importe_doscientos(self):
        resultado = calcular_rappicreditos_ganados(200)
        resultado_esperado = 20
        self.assertEqual(resultado_esperado, resultado)

    def test_calcular_rappicreditos_ganados_importe_entre_doscientos_y_mil(self):
        resultado = calcular_rappicreditos_ganados(300)
        resultado_esperado = 30
        self.assertEqual(resultado_esperado, resultado)

    def test_calcular_rappicreditos_ganados_importe_mil(self):
        resultado = calcular_rappicreditos_ganados(1000)
        resultado_esperado = 150
        self.assertEqual(resultado_esperado, resultado)

    def test_calcular_rappicreditos_ganados_importe_mayor_a_mil(self):
        resultado = calcular_rappicreditos_ganados(1200)
        resultado_esperado = 180
        self.assertEqual(resultado_esperado, resultado)


if __name__ == '__main__':
    unittest.main()
