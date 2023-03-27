import factory
from django.utils import timezone
from .models import Poll
from django.contrib.auth.models import User


class PollFactory(factory.django.DjangoModelFactory):
    question_text = "factory question"
    pub_date = timezone.now()

    class Meta:
        model = Poll


class UserFactory(factory.django.DjangoModelFactory):
    first_name = "XM"
    last_name = "G"
    email = factory.LazyAttribute(lambda a: "{0}.{1}@example.com".format(a.last_name, a.first_name).lower())
    username = factory.Sequence(lambda n: "person{0}".format(n))

    class Meta:
        model = User
