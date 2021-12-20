def similar_license_plates(plate1:str, plate2:str) -> bool:
  plate1= plate1.replace(" ","")
  plate2= plate2.replace(" ","")
  if plate1==plate2:
    return True
  
  if plate1 != plate2:
    for c in ["0", "Q"]:
      if c in plate2 or c in plate1:
        plate2 = plate2.replace(c, "O")
        plate1 = plate1.replace(c, "O")
    for d in ["1", "T"]:
      if d in plate2 or d in plate1:
        plate2 = plate2.replace(d, "I")
        plate1 = plate1.replace(d, "I")
    for e in ["2"]:
      if e in plate2 or e in plate1:
        plate2 = plate2.replace(e, "Z")
        plate1 = plate1.replace(e, "Z")
    for f in ["5"]:
      if f in plate2 or f in plate1:
        plate2 = plate2.replace(f, "S")
        plate1 = plate1.replace(f, "S")
    for g in ["8"]:
      if g in plate2 or g in plate1:
        plate2 = plate2.replace(g, "B")
        plate1 = plate1.replace(g, "B")
    
    if plate1 != plate2:
      return False
    else:
      return True

print(similar_license_plates("01258","OIZSB"))

import unittest
class TestCalc(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(similar_license_plates("01258","OISZB"),False)
        self.assertEqual(similar_license_plates("01258","OIZSB"),True)
        self.assertEqual(similar_license_plates("01 258","OIZS B"),True)
    

if __name__ == '__main__':
    unittest.main()