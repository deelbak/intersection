from django.db import models
from django.contrib.auth import get_user_model

'''
Model/Table relations

1) OneToOne - each "User" can have only one "Profile"
2) OneToMany - each "District" can have many "Products"
3) ManyToMany - each "Post" can have many "Tags", in the same time, one "Tag" can in in multiple "Posts"
'''

User = get_user_model()


class District(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

    def __str__(self):
        return f'{self.id}: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    # name = models.CharField(max_length=255)
    price = models.FloatField(default=1000)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    rating = models.FloatField(max_length=5.0)
    district = models.ForeignKey(District,
                                 on_delete=models.CASCADE,
                                 related_name='products')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    # def __str__(self):
    #     return f'{self.id}: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'name': self.name,
            'description':self.description,
            'rating':self.rating,
            'district':self.district
        }