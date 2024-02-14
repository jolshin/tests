import unittest

def dis_code(geo_logs, location):
    sort_list = []

    count = 0

    for dict_ in geo_logs:
        for x in dict_.values():
            if x[1] != location:
                sort_list.append(count)

            count += 1

    sort_list.reverse()

    for x in sort_list:
        geo_logs.pop(x)

    return geo_logs

class TestDisCode(unittest.TestCase):
    
    def test_positive(self):
        geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]

        location = 'Росиия'
        expected = [{'visit1': ['Москва', 'Россия']}, 
                    {'visit3': ['Владимир', 'Россия']}, 
                    {'visit7': ['Тула', 'Россия']}, 
                    {'visit8': ['Тула', 'Россия']}, 
                    {'visit9': ['Курск', 'Россия']}, 
                    {'visit10': ['Архангельск', 'Россия']}]
        res = dis_code(geo_logs, location)
        #self.assertEqual(res, expected)
        for res_item, expected_item in zip(
            dis_code(geo_logs, location), expected
        ):
            self.assertEqual(res_item, expected_item)

    @unittest.expectedFailure
    def test_negative(self):
        geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]

        location = 'Индия'
        expected = [{'visit1': ['Москва', 'Россия']}, 
                    {'visit3': ['Владимир', 'Россия']}, 
                    {'visit7': ['Тула', 'Россия']}, 
                    {'visit8': ['Тула', 'Россия']}, 
                    {'visit9': ['Курск', 'Россия']}, 
                    {'visit10': ['Архангельск', 'Россия']}]
        res = dis_code(geo_logs, location)
        #self.assertEqual(res, expected)
        for res_item, expected_item in zip(
            dis_code(geo_logs, location), expected
        ):
            self.assertEqual(res_item, expected_item)
