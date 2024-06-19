# An example of using the setUp method in Flask testing
class UserModelTestCase(TestCase):
    def setUp(self):
        dbx(db.delete(User))
        db.session.commit()

        hashed_password = (bcrypt
                           .generate_password_hash("password")
                           .decode('UTF-8')
                           )

        u1 = User(
            username="u1",
            email="u1@email.com",
            password=hashed_password,
            image_url=None,
        )

        u2 = User(
            username="u2",
            email="u2@email.com",
            password=hashed_password,
            image_url=None,
        )

        db.session.add_all([u1, u2])
        db.session.commit()

        self.u1_id = u1.id
        self.u2_id = u2.id
