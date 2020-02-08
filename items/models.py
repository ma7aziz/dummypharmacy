from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('general', 'GENERAL'),
    ('supplments', 'SUPPLMENTS'),
    ('pain killers', 'PAIN KILLERS'),
    ('cold-cough', 'COLD-COUGH'),
    ('stomach', 'STOMACH'),
    ('skin-care', 'SKIN-CARE'),
    ('hair-care', 'HAIR-CARE')
)
class Item(models.Model):
    name = models.CharField(max_length=200, blank=False)
    category = models.CharField(choices=CATEGORY_CHOICES,default='general', max_length=25 )
    price = models.FloatField(blank=False)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    times_sold = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/images/items', blank=True)
    published = models.BooleanField(default=True)



    def __str__(self):
        return self.name



# add category
# COLOR_CHOICES = (
#     ('green','GREEN'),
#     ('blue', 'BLUE'),
#     ('red','RED'),
#     ('orange','ORANGE'),
#     ('black','BLACK'),
# )

# class MyModel(models.Model):
#   color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')

