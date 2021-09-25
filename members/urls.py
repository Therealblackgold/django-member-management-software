from django.urls import path
from . import views
from .views import AddMemberIdNumber

urlpatterns = [
    # Add Member ID Number
    path('add-id-number', AddMemberIdNumber.as_view(), name='add-id-number'),
    # ID Suceess page
    path('id-success/', views.idsuccess, name="id-success"),
    # Member Homepage
    path('homepage/', views.memberhomepage, name="member-homepage"),

    # Member Package
    path('member-package/', views.memberpackage, name="member-package"),

    # Member Profile Details
    path('member/<slug:slug_id>', views.memberprofile, name="member-profile"),
    # Payments
    path('payments/<slug:slug_id>', views.payments, name="member-payments"),
    # Member Documents
    path('documents/<slug:slug_id>', views.memberdocuments, name="documents"),
    # Update Member
    path('update-member/<int:profile_id>',
         views.updatememberprofile,
         name="update-member"),
]