import mock
import os
import sys
#
# m = mock.Mock()
# print(m.something("this-is-dummy-arg"))
#
# # return_value指定返回值
# m.something.return_value=10
# print(m.something("this-is-dummy-arg"))
#
# # 查看mock方法调用
# print(m.something.called)
# print(m.something.call_args)
#
# # 指定发生例外
# m.something.side_effect = Exception('oops')
# print(m.something("this-is-dummy-arg"))
#
# # 在测试内使用断言
# m.something("spam")  # 第一次调用
# print(m.something.assert_called_with("egg"))
#
# m.something("spam") # 第二次调用
# print(m.something.assert_called_with("spam"))
#


p = os.path.dirname(os.path.dirname((os.path.abspath('__file__'))))
if p not in sys.path:
    sys.path.append(p)

import project
# patch装饰器使用示例
@mock.patch('project.views.SomeService')
def test_it(MockSomeService):
    mock_obj = MockSomeService.return_value
    mock_obj.something.return_value = 10
    from project.views import MockView
    result = MockView().index()
    assert result == 10
