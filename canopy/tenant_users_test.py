import unittest
import canopy


class TenantUsersTest(unittest.TestCase):

    def setUp(self):
        self.users = [
            canopy.openapi.GetTenantUsersQueryResultUserItem('id0', 'u0', 'u0@d.com'),
            canopy.openapi.GetTenantUsersQueryResultUserItem('id1', 'u1', 'u1@d.com'),
            canopy.openapi.GetTenantUsersQueryResultUserItem('id2', 'u2', 'u2@d.com'),
        ]

        self.target = canopy.TenantUsers(
            canopy.openapi.GetTenantUsersQueryResult(self.users))

    def test_it_should_contain_list_of_users(self):
        self.assertSequenceEqual(self.users, self.target.list)

    def test_it_should_return_by_user_id(self):
        self.assertEqual(
            self.users[1],
            self.target.get_by_user_id('id1'))

    def test_it_should_return_by_username(self):
        self.assertEqual(
            self.users[1],
            self.target.get_by_username('u1'))

    def test_it_should_throw_if_user_id_not_found(self):
        with self.assertRaises(canopy.NotFoundError):
            self.target.get_by_user_id('blah')

    def test_it_should_throw_if_username_not_found(self):
        with self.assertRaises(canopy.NotFoundError):
            self.target.get_by_username('blah')
