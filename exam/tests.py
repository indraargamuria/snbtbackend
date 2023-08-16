from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import MasterYear, MasterTimeline, MasterPackage

class Test_Create_MasterPackage(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser1', password='123456789')
        test_year = MasterYear.objects.create(year=2023)
        test_timeline = MasterTimeline.objects.create(name='Try OUT SG #12 SNBT',year_id=1,month=9)
        test_package = MasterPackage.objects.create(name='Paket SNBT Test', timeline_id=1, status=1, user_id=1)

    def testData(self):
        package = MasterPackage.masterpackageobjects.get(id=1)
        timeline = MasterTimeline.objects.get(id=1)
        year = MasterYear.objects.get(id=1)
        user = f'{package.user}'
        name = f'{package.name}'
        self.assertEqual(user, 'testuser1')
        self.assertEqual(name, 'Paket SNBT Test')
        self.assertEqual(str(package), 'Paket SNBT Test')
        self.assertEqual(str(timeline), 'Try OUT SG #12 SNBT')
        self.assertEqual(str(year), '2023')