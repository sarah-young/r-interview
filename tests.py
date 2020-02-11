import unittest, requests
from nose.tools import assert_true

from interview import generate_permutations, parse_permutations

class InterviewTestCases(unittest.TestCase):

    def test_get_api_response(self):
        response = requests.get('https://csrng.net/csrng/csrng.php?min=0&max=10000')

        assert_true(response.ok)

    def test_generate_permutations(self):
        result = generate_permutations('123')
        print(result)
        self.assertCountEqual(result,['123', '132', '213', '231', '321', '312'])

    def test_parse_permutations(self):
        result = parse_permutations(['123', '132', '213', '231', '312', '321'])
        self.assertEqual(result, 1332)

if __name__ == '__main__':
    unittest.main()