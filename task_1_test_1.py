import unittest

boys = sorted(['Peter', 'Alex', 'John', 'Arthur', 'Richard'])
girls = sorted(['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'])

#boys = sorted([x for x in input('Введите имена мальчиков через пробел: ').split()])
#girls = sorted([x for x in input('Введите имена девочек через пробел: ').split()])

def dis_code(boys, girls):
    if len(boys) == len(girls):
        return('Идеальные пары:')
    for i, j in zip(boys, girls):
        return(f'{i} и {j}')

    else:
        return('Число девочек и мальчиков не совпадают.')


class TestDisCode(unittest.TestCase):
    def test_positive(self):
        boys = ['Peter']
        girls = ['Kate']
        expected = 'Идеальные пары:'
        res = dis_code(boys, girls)
        self.assertEqual(res, expected)

    def test_negative(self):
        boys = ['Peter']
        girls = ['Kate', 'Emma']
        expected = 'Число девочек и мальчиков не совпадают.'
        res = dis_code(boys, girls)
        self.assertEqual(res, expected)

    @unittest.expectedFailure
    def test_failed(self):
        boys = ['Peter']
        girls = ['Kate', 'Emma']
        expected = 'Peter и Kate'
        res = dis_code(boys, girls)
        self.assertEqual(res, expected)

