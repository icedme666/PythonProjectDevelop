from django.db import models

# Create your models here.
TEA_KINDS = (
    ("english", "英式红茶"),
    ("chinese", "中国茶"),
    ("japanese", "日本茶")
)


class TeaManager(models.Manager):
    def recommended(self):
        """ 仅显示推荐商品 """
        return self.filter(is_flavor=True)

    def count_each_kind(self):
        """ 以字典形式返回各类茶的件数 """
        result = self.values_list("kind").annotate(count=models.Count("kind"))
        return dict(result)


class Tea(models.Model):
    objects = TeaManager()

    name = models.CharField("名称", max_length=255)
    kind = models.CharField("种类", max_length=255, choices=TEA_KINDS)
    price = models.IntegerField("价格")
    is_recommended = models.BooleanField("推荐商品", default=False)