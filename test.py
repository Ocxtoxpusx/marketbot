from unittest import *
import bot


class Test(TestCase):
    def test_add(self):

        bot.process_name_step()

    def test_isupper(self):
        self.assertTrue("ABC".isupper())
        self.assertFalse("aBc".isupper())

    def test_split(self):
        self.assertEquals("a b c".split(), ['a', 'b', 'c'])

    def test_find(self):
        self.assertEquals("abc".find("a"), 0)
        self.assertEquals("abc".find("b"), 1)

    def test_len(self):
        self.assertEquals(len("abc"), 3)
        self.assertNotEquals(len("abc"), 4)
