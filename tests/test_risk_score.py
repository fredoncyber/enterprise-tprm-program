import unittest
from tools.risk_score import calculate
class TestRiskScore(unittest.TestCase):
    def test_no_controls(self):
        r=calculate(5,5,0,1)
        self.assertEqual(r.residual,25)
        self.assertEqual(r.rating,'Critical')
    def test_effective_controls(self):
        r=calculate(4,5,.75,1)
        self.assertEqual(r.residual,5)
        self.assertEqual(r.rating,'Moderate')
    def test_confidence_reduces_credit(self):
        high=calculate(4,5,.8,1).residual
        low=calculate(4,5,.8,.25).residual
        self.assertGreater(low,high)
    def test_invalid(self):
        with self.assertRaises(ValueError): calculate(0,5,.5,.5)
if __name__ == '__main__': unittest.main()
