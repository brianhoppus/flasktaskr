import os
import unittest

from project import app, db
from project._config import basedir
from project.models import User

TEST_DB = "test.db"


class MainTests(unittest.TestCase):

    # setup and teardown #

    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTf_CSRF_ENABLED"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
                os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        #db.drop_all()


    # helper methods #

    def login(self, name, password):
        return self.app.post("/", data=dict(
            name=name, password=password), follow_redirects=True)


    # tests #

    def test_404_error(self):
        response = self.app.get("this-route-does-not-exist/")
        self.assertEquals(response.status_code, 404)

#    def test_500_error(self):
#        bad_user = User(
#            name="Jeremy",
#            email="jeremy@realpython.com",
#            password="django"
#        )
#        db.session.add(bad_user)
#        db.session.commit()
#        response = self.login("Jeremey", "django")
#        self.assertEquals(response.status_code, 500)

    def test_inde(self):
        """ Ensure flask was setup correctly. """
        response = self.app.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

