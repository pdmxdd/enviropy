import unittest, os
from util import add_enviropy, get_enviropy, delete_enviropy, enviropy_in_gitignore

class CreateEnviropyTest(unittest.TestCase):
    def setUp(self):
        if os.path.isfile("{}/.enviropy".format(os.getcwd())):
            os.remove("{}/.enviropy".format(os.getcwd()))
        add_enviropy({"test": "test data"})

    def test_file_exists(self):
        self.assertTrue(os.path.isfile("{}/.enviropy".format(os.getcwd())))

    def test_file_not_blank(self):
        with open("{}/.enviropy".format(os.getcwd()), 'r') as readfile:
            self.assertTrue("\n" in readfile.read())

    def tearDown(self):
        delete_enviropy()

    '''
    def test_create_enviropy(self):
        enviropy = get_enviropy()
        self.assertTrue("test" in enviropy.keys())
        self.assertTrue("test data" in enviropy.values())
    '''
class GetEnviropyTest(unittest.TestCase):
    def setUp(self):
        if os.path.isfile("{}/.enviropy".format(os.getcwd())):
            os.remove("{}/.enviropy".format(os.getcwd()))
        add_enviropy({"test": "test data"})
        self.enviropy = get_enviropy()

    def test_enviropy_type(self):
        temp_dict = {}
        self.assertEqual(type(temp_dict), type(self.enviropy))

    def test_enviropy_key(self):
        self.assertIn("test", self.enviropy.keys())

    def test_enviropy_value(self):
        self.assertIn("test data", self.enviropy.values())

    def test_get_enviropy_items(self):
        self.assertIn("test", self.enviropy.keys())
        self.assertIn("test data", self.enviropy.values())

class AddEnviropyTest(unittest.TestCase):
    def setUp(self):
        if os.path.isfile("{}/.enviropy".format(os.getcwd())):
            os.remove("{}/.enviropy".format(os.getcwd()))
        add_enviropy({"test": "test data"})
        self.enviropy1 = get_enviropy()
        add_enviropy({"foo": "bar"})
        self.enviropy2 = get_enviropy()

    def test_not_in_enviropy1(self):
        self.assertNotIn("foo", self.enviropy1.keys())
        self.assertNotIn("bar", self.enviropy1.values())

    def test_in_enviropy2(self):
        self.assertIn("foo", self.enviropy2.keys())
        self.assertIn("bar", self.enviropy2.values())

class DeleteEnviropyTest(unittest.TestCase):
    def setUp(self):
        if os.path.isfile("{}/.enviropy".format(os.getcwd())):
            os.remove("{}/.enviropy".format(os.getcwd()))
        add_enviropy({"test": "test data"})
        delete_enviropy()

    def test_no_file(self):
        self.assertFalse(os.path.isfile("{}/.enviropy".format(os.getcwd())))

class EnviropyAddedToGitignore(unittest.TestCase):
    def setUp(self):
        if os.path.isfile("{}/.enviropy".format(os.getcwd())):
            os.remove("{}/.enviropy".format(os.getcwd()))
        add_enviropy({"test": "test data"})

    def test_gitignore_exists(self):
        self.assertTrue(os.path.isfile("{}/.gitignore".format(os.getcwd())))

    def test_enviropy_added_to_gitignore(self):
        self.assertTrue(enviropy_in_gitignore())

class EnviropyRemovedFromGitignore(unittest.TestCase):
    def setUp(self):
        if os.path.isfile("{}/.enviropy".format(os.getcwd())):
            os.remove("{}/.enviropy".format(os.getcwd()))
        add_enviropy({"test": "test data"})
        delete_enviropy()

    def test_no_enviropy_in_gitignore(self):
        # print("-" * 40)
        self.assertFalse(enviropy_in_gitignore())
        # print("-" * 40)


