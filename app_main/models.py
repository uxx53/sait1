import datetime
from django.db import models
from decimal import Decimal
from sorl.thumbnail import ImageField
from django.forms import ModelForm


class CurrencyField(models.DecimalField, metaclass=models.SubfieldBase):
    def to_python(self, value):
        try:
            return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
        except AttributeError:
            return None

    def __str__(self):
        return self.value


class FIO(models.Model):
    name = models.CharField(u'Имя',max_length=200)
    age = models.IntegerField(u'Вoзраст')
    date_brd = models.DateTimeField(u'Дата рождения')
    phone = models.CharField(u'Телефон',max_length=30, null=True, blank=True)
    mail = models.EmailField(u'Почта',max_length=40)
    desc = models.TextField(u'Описание')
    per1 = models.FloatField(u'Процент')

    def __str__(self):
        return self.name + '  ' + self.desc

class FIOForm(ModelForm):
    class Meta:
        model = FIO
        fields = ['name', 'phone']


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = CurrencyField(max_digits=10, decimal_places=2)
    receive_news = models.BooleanField(default=True, db_index=True)
    slug = models.SlugField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    votes = models.IntegerField()

    def __str__(self):
        return self.title

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()


class Image(models.Model):
    item = models.ForeignKey(Item)
    file = ImageField(upload_to='images')
