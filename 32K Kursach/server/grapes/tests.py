from django.test import TestCase

from grapes.models import Bunch
from grapes.utils import process_bunch

# Create your tests here.
class BunchTestCase(TestCase):
    def setUp(self):
        self.bunch=Bunch.objects.create(count=12,outside=True,shape=False,color=False,sugar=False)
    
    def test_bunch_processing(self):
        processed_bunch=process_bunch(self.bunch)
        self.assertEqual(processed_bunch.stage, Bunch.Stage.Raisins)