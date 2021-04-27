from datetime import datetime
import sqlalchemy, sqlalchemy.orm
from django.test import TestCase
from .models import Base, ShortestPathRequest
from mario import settings

class TestView(TestCase):        
    def get_shortest_path(self):
        response = self.client.get('http://127.0.0.1:8000/mario/api/get_shortest_path?grid=-----,p-x--,-----,x---m,----x&grid_size=5')
        self.assertEqual(response.status_code, 200)

class ShortestPathRequestTestCase(TestCase):
    def setUp(self):
        self.engine = sqlalchemy.create_engine("sqlite:///" + str(settings.DATABASES['default']['NAME']))
        self.Session = sqlalchemy.orm.sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)
        self.shortest_path = ShortestPathRequest(grid="['-----','p-x--','-----','x---m','----x']", grid_size=5, request_time=str(datetime.now())) 
        self.session.add(self.shortest_path)
        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_shortest_path_request(self):        
        grid = self.session.query(ShortestPathRequest).all()        
        self.assertEqual(grid[0], self.shortest_path)
