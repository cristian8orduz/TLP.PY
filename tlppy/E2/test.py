import unittest
from final import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character()

    def test_initial_health(self):
        self.assertEqual(self.character.get_health(), 100)

    def test_initial_coins(self):
        self.assertEqual(self.character.get_coins(), 0)

    def test_add_coins(self):
        self.character.add_coins(20)
        self.assertEqual(self.character.get_coins(), 20)
        self.assertEqual(self.character.get_health(), 102)  
        
    def test_lose_health(self):
        self.character.lose_health(30)
        self.assertEqual(self.character.get_health(), 70)

    def test_character_death(self):
        self.character.lose_health(100)
        self.assertFalse(self.character.is_alive())

    def test_has_diamond(self):
        self.character.add_coins(200)
        self.assertTrue(self.character.has_diamond())

    def test_character_status(self):
        self.character.add_coins(50)
        self.assertEqual(self.character.get_status(), "Health: 105, Coins: 50, Diamonds: 0")

if __name__ == '__main__':
    unittest.main()
