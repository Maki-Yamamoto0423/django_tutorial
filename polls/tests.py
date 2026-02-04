from django.test import TestCase
from django.utils import timezone
import datetime

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        pub_date が未来の日付の場合、
        was_published_recently() は False を返すべき。
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)