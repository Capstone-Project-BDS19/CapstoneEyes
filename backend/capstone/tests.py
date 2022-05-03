from unicodedata import category
from django.test import TestCase

from django.contrib.auth.models import User #bring in the User table
from capstone.models import Post, Category

class Test_create_post(TestCase):
    @classmethod
    def setUpTestData(cls): #insert some data for testing
        test_category = Category.objects.create(name = 'django') #new entry
        testuser1= User.objects.create_user(
            username = 'test_user1', password = '123456789')
        test_post = Post.objects.create(
            category_id = 1, 
            title = 'Post Title', 
            excerpt = 'Post Excerpt', 
            content = 'Post-content', 
            slug = 'post-title', 
            author_id= 1,
            status = 'published'
        )
    
    def test_blog_content(self):
        post = Post.posotobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f"{post.author}"
        excerpt = f"{post.excerpt}"
        title = f"{post.title}"
        content= f"{post.content}"
        status = f"{post.status}"

        self.assertEqual(author, 'test_user1')
        self.assertEqual(excerpt, 'Post Excerpt')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post-content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Post Title')
        self.assertEqual(str(cat), 'django')



