"""usaspending_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from usaspending_api import views as views
from django.views.generic import TemplateView
from usaspending_api.common.views import MarkdownView
from django.conf.urls.static import static


urlpatterns = [
    url(r'^status/', views.StatusView.as_view()),
    url(r'^api/v1/awards/', include('usaspending_api.awards.urls_awards')),
    url(r'^api/v1/transactions/', include('usaspending_api.awards.urls_transactions')),
    url(r'^api/v1/submissions/', include('usaspending_api.submissions.urls')),
    url(r'^api/v1/accounts/', include('usaspending_api.accounts.urls')),
    url(r'^api/v1/financial_activities/', include('usaspending_api.financial_activities.urls')),
    url(r'^api/v1/references/', include('usaspending_api.references.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('usaspending_api.api_docs.urls')),
    url(r'^$', MarkdownView.as_view(markdown='landing_page.md')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
