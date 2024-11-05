import unittest
import math
from scientific_calculator import sine_method,cosine_method,tan_method,square_method,logarithm_method,exponent_method

class test_scientific_calculator(unittest.TestCase):
    def test_sine_positive(self):
        value = sine_method(90)
        self.assertAlmostEqual(value,1)
    def test_sine_negative(self):
        value = sine_method(-90)
        self.assertAlmostEqual(value,-1)
    def test_sine_zero(self):
        value = sine_method(0)
        self.assertAlmostEqual(value,0)
    def test_sine_nonnumerical(self):
        with self.assertRaises(TypeError):
            sine_method("hello")


    def test_cos_positive(self):
        value = cosine_method(90)
        self.assertAlmostEqual(value,0)
    def test_cos_negative(self):
        value = cosine_method(-90)
        self.assertAlmostEqual(value,0)
    def test_cos_zero(self):
        value = cosine_method(0)
        self.assertAlmostEqual(value,1)
    def test_cos_nonnumerical(self):
        with self.assertRaises(TypeError):
            cosine_method("hello")

    
    def test_tan_positive(self):
        value = tan_method(45)
        self.assertAlmostEqual(value,1)
    def test_tan_negative(self):
        value = tan_method(-45)
        self.assertAlmostEqual(value,-1)
    def test_tan_zero(self):
        value = tan_method(0)
        self.assertAlmostEqual(value,0)
    def test_tan_nonnumerical(self):
        with self.assertRaises(TypeError):
            tan_method("hello")
    

    def test_square_positive(self):
        value = square_method(16)
        self.assertEqual(value,4)
    def test_square_negative(self):
        with self.assertRaises(ValueError):
            square_method(-4)
    def test_square_zero(self):
        value = square_method(0)
        self.assertEqual(value,0)
    def test_square_nonnumerical(self):
        with self.assertRaises(TypeError):
            square_method("hello")



    def test_logarithm_positive(self):
        value = logarithm_method(15)
        self.assertAlmostEqual(value,2.70805020110221)
    def test_logarithm_negative(self):
        with self.assertRaises(ValueError):
            logarithm_method(-15)
    def test_logarithm_zero(self):
        with self.assertRaises(ValueError):
            logarithm_method(0)
    def test_logarithm_nonnumerical(self):
        with self.assertRaises(TypeError):
            logarithm_method("hello")

    
    def test_exponent_positive(self):
        value = exponent_method(5)
        self.assertAlmostEqual(value,148.4131591025766)
    def test_exponent_negative(self):
        value = exponent_method(-5)
        self.assertAlmostEqual(value,0.006737946999085467)
    def test_exponent_zero(self):
        value = exponent_method(0)
        self.assertAlmostEqual(value,1)
    def test_exponent_nonnumerical(self):
        with self.assertRaises(TypeError):
            exponent_method("hello")
    



if __name__=='__main__':
    unittest.main()