import unittest
import json
from app import app

class CrawlerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_crawl_bloomberg(self):
        response = self.app.get('/crawl?url=https://www.bloomberg.com/markets')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('articles', data)
        if data['articles']:
            self.assertIn('title', data['articles'][0])
            self.assertIn('link', data['articles'][0])
            self.assertIn('summary', data['articles'][0])

    def test_crawl_reuters(self):
        response = self.app.get('/crawl?url=https://www.reuters.com/world/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('articles', data)
        if data['articles']:
            self.assertIn('title', data['articles'][0])
            self.assertIn('link', data['articles'][0])
            self.assertIn('summary', data['articles'][0])

    def test_missing_url(self):
        response = self.app.get('/crawl')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Missing url parameter')

    def test_unsupported_website(self):
        response = self.app.get('/crawl?url=https://www.google.com')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Unsupported website')

if __name__ == '__main__':
    unittest.main()
