from django.db import models
from cities_light.models import City
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Ad(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def views_up(self):
        self.views += 1
        self.save()

    def viewed_handler(self, session):
        viewed_ads = session.get('ads', {})
        if viewed_ads.get(self.id) is None:
            viewed_ads[self.id] = self.id
            session['ads'] = viewed_ads
            self.views_up()

    class Meta:
        ordering = ('created',)
