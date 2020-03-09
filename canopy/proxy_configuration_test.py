import unittest
import canopy


class ProxyConfigurationTest(unittest.TestCase):

    def test_it_should_throw_if_scheme_not_found(self):
        with self.assertRaises(RuntimeError):
            canopy.ProxyConfiguration('test.com')

    def test_it_should_create_auth_url_and_headers_when_no_auth(self):
        proxy = canopy.ProxyConfiguration('https://test.com')
        self.assertEqual(proxy.url, 'https://test.com')
        self.assertEqual(proxy.auth_url, 'https://test.com')
        self.assertIsNone(proxy.username)
        self.assertIsNone(proxy.password)
        self.assertIsNone(proxy.headers)

    def test_it_should_create_auth_url_and_headers_when_auth(self):
        proxy = canopy.ProxyConfiguration('https://test.com', 'u1', 'p1')
        self.assertEqual(proxy.url, 'https://test.com')
        self.assertEqual(proxy.auth_url, 'https://u1:p1@test.com')
        self.assertEqual(proxy.username, 'u1')
        self.assertEqual(proxy.password, 'p1')
        self.assertIsNotNone(proxy.headers)

