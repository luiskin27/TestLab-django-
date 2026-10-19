from django.test import TestCase
from django.urls import reverse
from .models import Blog

class BlogTests(TestCase):

    def setUp(self):
        # пихаем картинку шоб шаблоны не падали без фотки
        self.blog = Blog.objects.create(
            title='тестовый заголовок',
            description='тестовое описание статьи',
            image='blog/test.jpg'
        )

    # 1. проверка списка постов
    def test_blog_list_returns_200_and_content(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'тестовый заголовок')

    # 2. проверка деталки (id и контент)
    def test_blog_detail_returns_200_and_id(self):
        url = reverse('blog_detail', args=[self.blog.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, str(self.blog.id))
        self.assertContains(response, 'тестовое описание статьи')

    # 3. проверка ошипки 404
    def test_blog_detail_not_found(self):
        url = reverse('blog_detail', args=[99999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # 4. проверка html шаблона
    def test_blog_detail_template_used(self):
        url = reverse('blog_detail', args=[self.blog.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog_detail.html')

    # 5. проверка ссылки назад
    def test_blog_detail_has_link_to_list(self):
        url = reverse('blog_detail', args=[self.blog.id])
        response = self.client.get(url)
        self.assertContains(response, reverse('blog_list'))

    # ==========================================
    # ЗАДАНИЕ 2: Лайки
    # ==========================================

    # 6. дефолтные лайки равны 0
    def test_new_blog_has_zero_likes(self):
        new_blog = Blog.objects.create(
            title='второй', 
            description='текст',
            image='blog/test2.jpg'
        )
        self.assertEqual(new_blog.likes, 0)

    # 7. накрутка +1 лайк при посещении
    def test_get_detail_increments_likes(self):
        self.assertEqual(self.blog.likes, 0)
        url = reverse('blog_detail', args=[self.blog.id])
        self.client.get(url)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.likes, 1)