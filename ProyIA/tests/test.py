import unittest
import requests
import os

class TestGrobidService(unittest.TestCase):

    def test_grobid_up(self):
        url = "http://grobid:8070"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_grobid_pdf(self):
        url = "http://grobid:8070/api/processFulltextDocument"
        pdf_dir = '../Resources'
        for pdf_file in os.listdir(pdf_dir):
            if pdf_file.endswith('.pdf'):
                pdf_path = os.path.join(pdf_dir, pdf_file)
                files = {'input': open(pdf_path, 'rb')}
                response = requests.post(url, files = files)
                self.assertEqual(response.status_code, 200, f"Error en {pdf_file}, compruebe si el archivo está en formato pdf")

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestGrobidService)
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    if test_result.wasSuccessful():
        print("Servicio de Grobid levantado y PDFs recibidos correctamente")
    else:
        print("Servicio de grobid no disponible o PDFs no recibidos correctamente")
