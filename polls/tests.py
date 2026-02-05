import datetime

from django.test import TestCase
from django.utils import timezone

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

    def test_was_published_recently_with_old_question(self):
        """
        pub_date が1日より前の場合、
        was_published_recently() は False を返す
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        pub_date が直近1日以内の場合、
        was_published_recently() は True を返す
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)