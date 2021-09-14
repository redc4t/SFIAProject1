from flask import url_for
from flask_testing import TestCase
from SFIAProject1 import app, db
from SFIAProject1.models import User , Post
from datetime import datetime
 

#base class
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///site.db",
                
                Debug=True,
                WTF_CSRF_ENABLED=False
     
                )
        return app
    def setUp(self): 
        """                                      
        Will be called before every test
        """
      
        db.create_all()#create db

        test_user = User(
            username = "steve",
            email =  "steve@steve.com",
            password = "fueling"
        )
        db.session.add(test_user) 
        db.session.commit()
                                                                            
        test_post = Post(
            title = "test time",                 
            date_posted =  datetime(2021,1,11),
            content = "this is a test",
            
        )
        db.session.add(test_post)
        db.session.commit()

        

    def tearDown(self):                                
        db.session.remove()
        db.drop_all()




class TestViews(TestBase):    
    def testing_home(self):
        response = self.client.get(url_for ('home'))
        self.assertEqual(response.status_code, 200)



                
