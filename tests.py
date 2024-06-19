# Example of using Django's setUpTestData class method
class UserModelTestCase(TestCase):
    """Test User model."""

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(
            photo=SimpleUploadedFile("foo.gif", SAMPLE_GIF_DATA))
