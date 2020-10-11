#tests/update-readme-image-tests.py
"""
Test file to support continuous integration.
"""

from main import get_image_tag, verify_image_ext
import unittest
from unittest.mock import patch, Mock, call


class TestUpdateReadmeImage(unittest.TestCase):

    def test_get_image_tag(self):
        repo = Mock()
        repo.get_contents.return_value = Mock()
        with patch('main.random.choice') as mockChoice:
            with patch('main.verify_image_ext') as mockVerifyImg:
                newMock = Mock()
                mockChoice.return_value = newMock
                mockVerifyImg.return_value = True
                newMock.download_url = 'some_raw_github_content.png'
                actual_img_tag = get_image_tag(repo)
                expected_img_tag = "<img src=some_raw_github_content.png height=None width=None align=None alt=None />"
                self.assertEqual(actual_img_tag, expected_img_tag)

    def test_get_image_tag_sys_exit(self):
        repo = Mock()
        repo.get_contents.return_value = Mock()
        with patch('main.random.choice') as mockChoice:
            with patch('main.verify_image_ext') as mockVerifyImg:
                newMock = Mock()
                mockChoice.return_value = newMock
                mockVerifyImg.return_value = False
                with self.assertRaises(SystemExit):
                    get_image_tag(repo)

    def test_verify_image_ext_true(self):
        image = Mock()
        image.path = 'images/image1.png'
        actual = verify_image_ext(image)
        self.assertTrue(actual)

    def test_verify_image_ext_false(self):
        image = Mock()
        image.path = 'images/image1.xyz'
        with patch('builtins.print') as mockPrint:
            actual = verify_image_ext(image)
            assert mockPrint.mock_calls == [call("Please make sure image is one of following type ['png', 'jpg', 'jpeg', 'gif', 'svg'], error caused by image - images/image1.xyz")]
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()