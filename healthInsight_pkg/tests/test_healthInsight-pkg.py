import unittest

from healthinsight import __version__

from healthinsight.Calculations import HealthCalc

def test_version():
	assert __version__ == "0.0.1"


class TestHealthCalc(unittest.TestCase):
    
    def test_bmi(self):
        bmi_value, category = HealthCalc.bmi(65, 1.70)
        self.assertAlmostEqual(bmi_value, 22.49, places=2)
        self.assertEqual(category, "Normal")

    def test_bai(self):
        result = HealthCalc.bai(90, 1.75)
        self.assertAlmostEqual(result, 24.91, places=2)

    def test_bsi(self):
        result = HealthCalc.bsi(80, 65, 1.75)
        self.assertAlmostEqual(result, 0.090, places=3)

    def test_tbw(self):
        result = HealthCalc.tbw(70, 30)
        self.assertAlmostEqual(result, 42.0, places=1)

    def test_corpulence_index(self):
        result = HealthCalc.corpulence_index(65, 1.75)
        self.assertAlmostEqual(result, 21.22, places=2)

    def test_waist_to_hip(self):
        result = HealthCalc.waist_to_hip(80, 90)
        self.assertAlmostEqual(result, 0.888, places=4)

    def test_pignetindex(self):
        result = HealthCalc.pignetindex(175, 70, 90)
        self.assertEqual(result, 15)

    def test_birthrate(self):
        result = HealthCalc.birthrate(2000, 1000000)
        self.assertAlmostEqual(result, 2.0, places=1)

if __name__ == "__main__":
    unittest.main()
