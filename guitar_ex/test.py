import unittest


from inventory import Inventory
from builder import Builder
from type_ import Type
from wood import Wood
from guitarspec import GuitarSpec
from guitar import Guitar



class TestGuitarExample(unittest.TestCase):

    def test_inventory(self):
        guitarSpec1 = GuitarSpec(Builder.FENDER, 'idk', 6, Type.ELECTRIC, Wood.MAHOGANY)
        guitarSpec2 = GuitarSpec(Builder.GIBSON, 'ireallydk', 13, Type.ACOUSTIC, Wood.CEDAR)



        guitar1 = Guitar('22892', 0.0, guitarSpec1)
        guitar2 = Guitar('34211', 453.3, guitarSpec2)
        guitar3 = Guitar('11232', 453.3, guitarSpec2)
        guitar4 = Guitar('09995', 453.3, guitarSpec1)
        guitar5 = Guitar('05001', 453.3, guitarSpec1)
        guitar6 = Guitar('32002', 453.3, guitarSpec1)

        inventory = Inventory()


        inventory.add_guitar(guitar1)
        inventory.add_guitar(guitar2)
        inventory.add_guitar(guitar3)
        inventory.add_guitar(guitar4)
        inventory.add_guitar(guitar5)
        inventory.add_guitar(guitar6) #6 guitar instances added


        self.assertEqual(len(inventory.guitars), 6)

        return inventory

    def test_search(self):

        inventory = self.test_inventory()

        #customer's search (guitarspec1 appears 4 times)
        search_spec = GuitarSpec(Builder.FENDER, 'idk', 6, Type.ELECTRIC, Wood.MAHOGANY)

        results = inventory.search(search_spec)

        #[Guitar(22892, 0.0, GuitarSpec(Fender, idk, 6, Electric, Mahogany)), \
        # Guitar(09995, 453.3, GuitarSpec(Fender, idk, 6, Electric, Mahogany)),\
        #  Guitar(05001, 453.3, GuitarSpec(Fender, idk, 6, Electric, Mahogany)), \
        # Guitar(32002, 453.3, GuitarSpec(Fender, idk, 6, Electric, Mahogany))]
        
        self.assertEqual(len(results), 4)


if __name__ == '__main__':
    unittest.main()