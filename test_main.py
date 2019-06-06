import unittest
import main


class TestMain(unittest.TestCase):

    def test_calculate_right_solution(self):
        """
        Test that the returned solution is correct.
        """
        items_data = [
            ('dolan.jpg', 126, 6),
            ('smutna_zaba.png', 221, 10),
            ('t-series.avi', 522, 12),
            ('dank.png', 205, 8),
            ('scotish_pokemon.gif', 601, 16)
        ]
        capacity_data = 1

        expected = (32, {'scotish_pokemon.gif', 'smutna_zaba.png', 'dolan.jpg'})
        result = main.calculate(capacity_data, items_data)

        self.assertEqual(expected, result)

    def test_calculate_string_type_usb(self):
        """
        Test that the function reacts correctly to the String type data that should be int.
        """
        items_data = [
            ('dolan.jpg', 126, 6),
            ('smutna_zaba.png', 221, 10),
            ('t-series.avi', 522, 12),
            ('dank.png', 205, 8),
            ('scotish_pokemon.gif', 601, 16)
        ]
        capacity_data = '1'

        expected = (32, {'dolan.jpg', 'smutna_zaba.png', 'scotish_pokemon.gif'})
        result = main.calculate(capacity_data, items_data)

        self.assertEqual(expected, result)

    def test_calculate_wrong_type_usb(self):
        """
        Test that the function reacts correctly to the String type data that should be int.
        """
        items_data = [
            ('dolan.jpg', 126, 6),
            ('smutna_zaba.png', 221, 10),
            ('t-series.avi', 522, 12),
            ('dank.png', 205, 8),
            ('scotish_pokemon.gif', 601, 16)
        ]
        capacity_data = 'something incorrect'

        with self.assertRaises(ValueError):
            main.calculate(capacity_data, items_data)

    def test_calculate_list_type_memes(self):
        """
        Test that the function reacts correctly to a list(list) type data that should be a list(tuple).
        """
        items_data = [
            ['dolan.jpg', 126, 6],
            ['smutna_zaba.png', 221, 10],
            ['t-series.avi', 522, 12],
            ['dank.png', 205, 8],
            ['scotish_pokemon.gif', 601, 16]
        ]
        capacity_data = 1

        expected = (32, {'dolan.jpg', 'smutna_zaba.png', 'scotish_pokemon.gif'})
        result = main.calculate(capacity_data, items_data)

        self.assertEqual(expected, result)

    def test_calculate_wrong_type_memes(self):
        """
        Test that the function reacts correctly to a list of wrong types data that should be a list(tuple)
        or list(list).
        """
        items_data = [
            'dolan.jpg', 126, 6,
            ('smutna_zaba.png', 221, 10),
            ['t-series.avi', 522, 12],
            'dank.png', 205, 8,
            ['scotish_pokemon.gif', 601, 16]
        ]
        capacity_data = 1

        with self.assertRaises(TypeError):
            main.calculate(capacity_data, items_data)

    def test_calculate_float_type_inside_memes(self):
        """
        Test that the function reacts correctly to a list/tuple of wrong types data that should be str or int.
        """
        items_data = [
            ['dolan.jpg', 126, 6],
            ['smutna_zaba.png', 221, 10],
            ['t-series.avi', 52.2, 12],
            ['dank.png', 20.5, 8],
            ['scotish_pokemon.gif', 60.1, 1.6]
        ]
        capacity_data = 1

        with self.assertRaises(TypeError):
            main.calculate(capacity_data, items_data)

    def test_calculate_too_many_values_inside_memes(self):
        """
        Test that the function reacts correctly to too many values inside a tuple in a list.
        """
        items_data = [
            ['dolan.jpg', 126, 6],
            ['smutna_zaba.png', 221, 10, 1245],
            ['t-series.avi', 522, 1563, 12],
            ['dank.png', 205, 8],
            ['scotish_pokemon.gif', 601, 16]
        ]
        capacity_data = 1

        with self.assertRaises(ValueError):
            main.calculate(capacity_data, items_data)

    def test_calculate_too_few_values_inside_memes(self):
        """
        Test that the function reacts correctly to too few values inside a tuple in a list.
        """
        items_data = [
            ['dolan.jpg', 126, 6],
            ['smutna_zaba.png', 'fdsf'],
            ['t-series.avi', 1563],
            ['dank.png', 205, 8],
            ['scotish_pokemon.gif', 601, 16]
        ]
        capacity_data = 1

        with self.assertRaises(ValueError):
            main.calculate(capacity_data, items_data)

    def test_calculate_string_type_inside_memes(self):
        """
        Test that the function reacts correctly to a list/tuple of String types data.
        """
        items_data = [
            ['dolan.jpg', 126, 6],
            ['smutna_zaba.png', 221, 10],
            ['t-series.avi', 522, '1f2'],
            ['dank.png', '205', 8],
            ['scotish_pokemon.gif', '601', '16']
        ]
        capacity_data = 1

        with self.assertRaises(TypeError):
            main.calculate(capacity_data, items_data)


if __name__ == '__main__':
    unittest.main()
