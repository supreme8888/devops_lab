from unittest import TestCase
import handlers.pulls as pulls
#from handlers.pulls import get_pulls

class TestPulls(TestCase):

  def setUp(self):
    """Init"""

  def test_get_list_label(self):
    """Test for get_list_label"""
    result = pulls.get_list_label("accepted")
    self.assertIsInstance(result, list)

  def test_get_list_res(self):
    """Test for get_list_res"""
    result = pulls.get_list_res("open")
    self.assertIsInstance(result, list)

  def test_get_list_all(self):
    """"Test for get_list_all"""
    result = pulls.get_list_all(None)
    self.assertIsInstance(result, list)

  def test_get_pulls(self):
    """"Test for main function"""
    result = pulls.get_pulls("accepted")
    self.assertIsInstance(result, list)
    result = pulls.get_pulls("open")
    self.assertIsInstance(result, list)
    result = pulls.get_pulls("closedd")
    self.assertIsInstance(result, list)
    result = pulls.get_pulls("needs work")
    self.assertIsInstance(result, list)

  def tearDown(self):
    """Finish"""
