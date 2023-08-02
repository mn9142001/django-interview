from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Upload
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
import os
# Create your tests here.
class TestUpload(TestCase):
    
    
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="admin", password="admin")
        self.client.login(username=self.user.username, password="admin")

    def test_upload(self):
        image_path = os.path.join(settings.BASE_DIR, "media", "about-us.png")
        file = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        post_request = self.client.post(reverse("home"), data={"image" : file}, follow=True)
        assert Upload.objects.count() == 1, post_request.content