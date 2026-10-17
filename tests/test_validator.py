import unittest
from validator import validate_with_regex, validate_with_dfa
class ValidatorTests(unittest.TestCase):
 def test_cases(self):
  cases=[("Itm@2026",True),("Admin@123",True),("Abcdefghijk@1234",True),("admin@123",False),("ADMIN@123",False),("Admin1234",False),("Adm@12",False),("Admin@12345678901",False),("Admin @123",False),("",False),("Abcdefg1é@",False)]
  for p,want in cases:
   with self.subTest(password=p):
    self.assertEqual(validate_with_regex(p)["valid"],want)
    self.assertEqual(validate_with_dfa(p)["valid"],want)
 def test_agreement(self):
  alphabet="Aa1@ "
  for a in alphabet:
   for b in alphabet:
    p=a+b
    self.assertEqual(validate_with_regex(p)["valid"],validate_with_dfa(p)["valid"])
if __name__=="__main__": unittest.main()
