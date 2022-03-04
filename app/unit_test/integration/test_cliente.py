import unittest
from model.domain.cliente_model import ClienteModel

class TestCliente(unittest.TestCase):

    def test_edad(self):
        test_cliente = ClienteModel()
        test_cliente.IdCliente = '7'
        test_cliente.NumeroCliente = 'EPUPSZM'
        test_cliente.Email = 'viviana@vexi.mx'
        test_cliente.PrimerNombre = 'Marverde'
        test_cliente.SegundoNombre = 'Viviana'
        test_cliente.ApellidoPaterno = 'Arboleda'
        test_cliente.ApellidoMaterno = 'Pinos'
        test_cliente.CURP = 'AOPM750718MCMRNR00'
        test_cliente.FechaNacimiento = '1975-07-18'
        test_cliente.Celular = '5512933133'
        test_cliente.RFC = 'AOPM7507186P0'
        edad_valida = test_cliente.validar_edad()
        valor_esperado = True
        self.assertEqual(edad_valida, valor_esperado)

        test_cliente.FechaNacimiento = '2021-05-01'
        edad_valida = test_cliente.validar_edad()
        valor_esperado = False
        self.assertEqual(edad_valida, valor_esperado)

if __name__ == '__main__':
    unittest.main()