from django.urls import path
from . import views

urlpatterns = [
    #     path('admin-home/', views.HomepageView, name="admin-home"),
    # path('<int:member_id>/', views.MemberDetail, name="member"),
    #     path('view_member/<str:pk>/', views.MemberDetail, name="view_member"),

    # Pending Member View
    path('view_pending/<str:pk>/',
         views.PendingMemberDetail,
         name="view_pending"),

    # Update Member
    #     path('update_member/<str:pk>/', views.UpdateMember, name="update_member"),
    path('update-member-admin/<int:profile_id>',
         views.UpdateMemberAdmin,
         name="update-member-admin"),

    # Pending Update
    path('update_pending_member/<str:pk>/',
         views.UpdatePendingMember,
         name="update_pending_member"),
    # SHOW PROFILE FINAL
    path('showprofile/', views.showprofile, name="showprofile"),
    # PROFILE DETAILS <slug:slug_id>
    path('profile-details/<int:profile_id>',
         views.showprofiledetails,
         name="profile-details"),
    # SEARCH
    path('search-member/', views.search_member, name="search-member"),
    # Payments
    path('payments/<slug:slug_id>', views.payments, name="member-payments"),
    # Burials
    path('burials/<slug:slug_id>', views.burials, name="member-burials"),
    path('list-burials', views.allburials, name="all-member-burials")
]
