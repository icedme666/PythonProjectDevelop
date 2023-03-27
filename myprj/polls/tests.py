from django.test import TestCase
from polls.poll_factory import PollFactory, UserFactory
from django.utils import timezone


# Create your tests here.
class PollsTestCase(TestCase):
    fixtures = ['polls.json']

    def setUp(self):
        # 一般的测试定义
        pass

    def testPoll(self):
        # 使用配置器的测试

        # 返回没有save的Poll实例
        poll1 = PollFactory.build()
        print(poll1.question_text, poll1.pub_date)

        # 返回已save的Poll实例，设置灵活的日期
        poll2 = PollFactory.create(pub_date=timezone.now())
        print(poll2.question_text, poll2.pub_date)

        # 直接实例化效果与create相同
        poll3 = PollFactory()
        print(poll3.question_text, poll3.pub_date)

        # 以字典形式返回生成Poll实例时所需的属性

        # 返回所有属性桩代码化后的对象
        stub = PollFactory.stub()
        print(stub)

        # 覆盖属性
        poll4 = PollFactory.create(question_text="changed question")
        print(poll4.question_text, poll4.pub_date)

    def test_lazy_attribute(self):
        email = UserFactory().email
        print("\nemail is: %s" % email)
        self.assertEqual("g.xm@example.com", email)

    def test_sequence(self):
        username = UserFactory().username
        print("\nname is: %s" % username)
        self.assertEqual("person1", username)
