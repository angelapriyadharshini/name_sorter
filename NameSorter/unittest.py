import unittest
from app import NameSorter


class Test_unittest(unittest.TestCase):
    def test_name_sorter(self):
        cases=[
            ([],[]),
            (['Adunis Julius Archer', 'Adonis Julius Archer','Marin Alvarez'],['Marin Alvarez', 'Adonis Julius Archer','Adunis Julius Archer'])
            ]
        for x, expected in cases:
            self.assertEqual(name_sorter(x,expected))

if __name__ == '__main__':
    unittest.main()
