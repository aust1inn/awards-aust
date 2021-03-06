from django.test import TestCase
from .models import *
# Create your tests here.
class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='roro')
        self.profile = Profile.objects.create(user = self.user,bio = 'Fantastic')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

class ProjectTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='roro')
        self.profile = Profile.objects.create(user = self.user,bio = 'Die Hard')

        self.project = Project.objects.create(posted_by = self.user,
                                          profile = self.profile,
                                          title = 'Blog',
                                          description='turn up',
                                          project_link= 'https://austinsta.herokuapp.com/')

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

    def test_get_projects(self):
        self.project.save()
        project = Project.get_projects()
        self.assertTrue(len(project) == 1)

    def test_find_project(self):
        self.project.save()
        project = Project.find_project('blog')
        self.assertTrue(len(project) > 0)

class ReviewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='roro')

        self.review= Reviews.objects.create(juror= self.user, design=5, usability=5,content=5,comment="good" )

    def test_instance(self):
        self.assertTrue(isinstance(self.review, Reviews))

    def test_save_review(self):
        self.assertTrue(isinstance(self.review,Reviews))

    def test_get_reviews(self):
        self.review.save()
        review = Reviews.get_reviews()
        self.assertTrue(len(review) == 1)