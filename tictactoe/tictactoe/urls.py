from django.conf.urls import patterns, url

from game.views import GameView

urlpatterns = patterns('',
    url(r'^$', GameView.as_view())
)
