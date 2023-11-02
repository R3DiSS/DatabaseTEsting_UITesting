# from django.test import TestCase
# from .models import Articles  

# class ArticlesViewTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         Articles.objects.create(title='Test Title', anons='Test Anons', full_text='Test Body', date='2023-09-16T00:00')

#     def test_news_home_view(self):
#         response = self.client.get('/news/')
#         self.assertEqual(response.status_code, 200)

#     def test_news_detail_view(self):
#         article = Articles.objects.get(id=1)
#         response = self.client.get(article.get_absolute_url())
#         self.assertEqual(response.status_code, 200)

#     def test_news_create_view(self):
#         response = self.client.get('/news/create')
#         self.assertEqual(response.status_code, 200)
        

# from django.test import TestCase
# from django.urls import reverse
# from .models import Articles

# class NewsTestCase(TestCase):
#     def setUp(self):
#         Articles.objects.create(title="Test Title", anons="Test Anons", full_text="Test full text")
        
#     def test_news_list(self):
#         response = self.client.get(reverse('news_home'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Test Title")

#     def test_article_creation(self):
#         article = Articles.objects.get(title="Test Title")
#         self.assertIsNotNone(article)

    
from django.test import TestCase
from django.urls import reverse
from .models import Articles

class NewsSmokeTest(TestCase):

    def setUp(self):
        self.article = Articles.objects.create(
            title='Test Title',
            anons='Test Anons',
            full_text='Test Full Text',
            date='2022-01-01T10:20:30Z'
        )

    def test_news_home_view(self):
        response = self.client.get(reverse('news_home'))
        self.assertEqual(response.status_code, 200)

    def test_news_detail_view(self):
        response = self.client.get(reverse('news-detail', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)

    def test_news_create_view(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)

    def test_news_update_view(self):
        response = self.client.get(reverse('news-update', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)

    def test_news_delete_view(self):
        response = self.client.get(reverse('news-delete', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)



##DATABASE TESTING:

from django.test import TestCase, Client
from django.urls import reverse
from .models import Articles
from .forms import ArticlesForm

class NewsViewsTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.article = Articles.objects.create(title="Test Title", content="Test Content") 
        self.create_url = reverse('create')  
        self.detail_url = reverse('detail', args=[self.article.id])  
        self.update_url = reverse('update', args=[self.article.id])  
        self.delete_url = reverse('delete', args=[self.article.id])  

    def test_news_home_view(self):
        response = self.client.get(reverse('news_home'))  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Title")  

    def test_news_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Title")

    def test_news_create_view(self):
        data = {
            'title': 'New Test Article',
            'content': 'This is the content for the new test article.'
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Articles.objects.filter(title='New Test Article').exists())

    def test_news_update_view(self):
        data = {
            'title': 'Updated Test Title',
            'content': 'Updated test content.'
        }
        response = self.client.post(self.update_url, data)
        self.assertEqual(response.status_code, 302)
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, 'Updated Test Title')

    def test_news_delete_view(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Articles.objects.filter(id=self.article.id).exists())


#UI Testing:
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import Articles

class UITestCase(unittest.TestCase):

    def setUp(self):
        # Start the webdriver (assuming Chrome here)
        self.driver = webdriver.Chrome(executable_path='/path_to_chromedriver')
        self.article = Articles.objects.create(title="Test Title", content="Test Content") # Adapt based on your model

    def tearDown(self):
        self.driver.quit()  # Close the browser

    def test_news_home(self):
        driver = self.driver
        driver.get("http://localhost:8000/news/")  # Adjust URL if different
        self.assertIn("Test Title", driver.page_source)

    def test_article_detail(self):
        driver = self.driver
        driver.get(f"http://localhost:8000/news/{self.article.id}/")  # Adjust URL pattern if different
        self.assertIn("Test Title", driver.page_source)

    # ... Repeat similar steps for other views like Create, Update, and Delete.

if __name__ == "__main__":
    unittest.main()

