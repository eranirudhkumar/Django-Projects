from django.conf.urls import url

from . import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.home),
    url(r'^login/$', blog_views.user_login),
    url(r'^signup/$', blog_views.user_signup),

    # url(r'^signup-form/$', blog_views.LoginFormView.as_view(
    #     template_name="users/user_view_signup.html"
    # )),
    url(r'^signup-form/$', blog_views.signupFormView),
    url(r'^new-employee/$', blog_views.create_employee),


]
