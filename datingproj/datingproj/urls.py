"""datingproj URL Configuration

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
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from dating import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dating/', include('dating.urls')),
    # url(r'^$', views.index, name='index'),
    url(r'^registerMember',views.register_member,  name='register_member'),
    url(r'^updateMember',views.update_member,  name='update_member'),
    url(r'^memberDeactivate',views.member_deactivate,  name='member_deactivate'),
    url(r'^uploadMemberPicture',views.upload__member_picture,  name='upload__member_picture'),
    url(r'^loadLocation',views.register_location,  name='register_location'),
    url(r'^loginMember',views.login_member,  name='login_member'),
    url(r'^login2Member',views.login_member2,  name='login_member2'),
    url(r'^uploadQuestionnaireInfo',views.upload_questionnaire,  name='upload_questionnaire'),
    url(r'^getAllUsers', views.get_all_users, name='get_all_users'),
    url(r'^load2QuestionnaireInfo',views.upload_questionnaire2,  name='upload_questionnaire2'),
    url(r'^post',views.post,  name='post'),
    url(r'^updatePost',views.updatePost,  name='updatePost'),
    url(r'^getposts',views.get_posts,  name='get_posts'),
    url(r'^delpost',views.delpost,  name='delpost'),
    url(r'^sendNotification',views.sendNotification,  name='sendNotification'),
    url(r'^getNotifications',views.getNotifications,  name='getNotifications'),    ##############################################
    url(r'^setActive',views.setActive,  name='setActive'),
    url(r'^getUser',views.getUser,  name='getUser'),
    url(r'^checkNotification',views.checkNotification,  name='checkNotification'),
    url(r'^removeNotification',views.removeNotification,  name='removeNotification'),
    url(r'^checkUnravel',views.checkUnravel,  name='checkUnravel'),
    url(r'^getActives', views.getActives, name='getActives'),
    url(r'^exitChat', views.exitChat, name='exitChat'),
    url(r'^leaveLastMessage', views.leaveLastMessage, name='leaveLastMessage'),
    url(r'^chatExit', views.chatExit, name='chatExit'),
    url(r'^setNotifications', views.setNoti, name='setNoti'),
    url(r'^getNoti', views.getNoti, name='getNoti'),
    url(r'^riseUnraveled', views.riseUnraveled, name='riseUnraveled'),
    url(r'^upgradeUser', views.upgradeUser, name='upgradeUser'),
    url(r'^resetPremium', views.resetPremium, name='resetPremium'),
    url(r'^getActiveDates',views.getActiveDates,  name='getActiveDates'),
    url(r'^releaseBlock',views.releaseBlock,  name='releaseBlock'),
    url(r'^releaseBlockOnChat',views.releaseBlockOnChat,  name='releaseBlockOnChat'),
    url(r'^$',views.adminloginpage,  name='adminloginpage'),
    url(r'^loginAdmin',views.loginAdmin,  name='loginAdmin'),
    url(r'^logout',views.logout,  name='logout'),
    url(r'^view_image',views.view_image,  name='view_image'),
    url(r'^photo_approved/(?P<member_id>[0-9]+)/$', views.photo_approved, name='photo_approved'),
    url(r'^home',views.home,  name='home'),
    url(r'^photorejected/(?P<member_id>[0-9]+)/$', views.photo_rejected, name='photo_rejected'),
    url(r'^questions',views.questions,  name='questions'),
    url(r'^add_dynamical',views.add_dynamical,  name='add_dynamical'),
    url(r'^delete_dynamical/(?P<q_id>[0-9]+)/$', views.delete_dynamical, name='delete_dynamical'),
    url(r'^questionupdate', views.questionupdate, name='questionupdate'),
    url(r'^getDynamicals',views.getDynamicals,  name='getDynamicals'),
    url(r'^editmembership',views.editmembership,  name='editmembership'),
    url(r'^updatemembership',views.updatemembership,  name='updatemembership'),
    url(r'^getmembership',views.getmembership,  name='getmembership'),
    url(r'^filter',views.filter,  name='filter'),
    url(r'^search',views.search,  name='search'),
    url(r'^ctrsearch',views.ctrsearch,  name='ctrsearch'),
    url(r'^new_photo_users',views.new_photo_users,  name='new_photo_users'),
    url(r'^photo_approved_users',views.photo_approved_users,  name='photo_approved_users'),
    url(r'^photo_rejected_users',views.photo_rejected_users,  name='photo_rejected_users'),
    url(r'^export_xlsx',views.export_xlsx,  name='export_xlsx'),
    url(r'^control',views.control,  name='control'),
    url(r'^deactivated/(?P<member_id>[0-9]+)/$', views.deactivated, name='deactivated'),
    url(r'^activated/(?P<member_id>[0-9]+)/$', views.activated, name='activated'),
    url(r'^activated_users',views.activated_users,  name='activated_users'),
    url(r'^deactivated_users',views.deactivated_users,  name='deactivated_users'),
    url(r'^userupdate',views.userupdate,  name='userupdate'),
    url(r'^okayUpdatedMembership',views.okayUpdatedMembership,  name='okayUpdatedMembership'),
    url(r'^uploadPicture',views.upload_picture,  name='upload_picture'),
    url(r'^updatePicture',views.updatePicture,  name='updatePicture'),
    url(r'^deletePicture',views.deletePicture,  name='deletePicture'),
    url(r'^getPictures',views.getPictures,  name='getPictures'),
    url(r'^saveSettings',views.saveSettings,  name='saveSettings'),
    url(r'^getSettings',views.getSettings,  name='getSettings'),

    url(r'^mybids/(?P<folder_id>[0-9]+)',views.mybids,  name='mybids'),
    url(r'^addbid/(?P<folder_id>[0-9]+)/$',views.addbid,  name='addbid'),
    url(r'^savebid/(?P<bid_id>[0-9]+)/(?P<folder_id>[0-9]+)/$', views.savebid, name='savebid'),
    url(r'^deletebid/(?P<bid_id>[0-9]+)/(?P<folder_id>[0-9]+)/$', views.deletebid, name='deletebid'),

    url(r'^loginpage', views.loginpage, name='loginpage'),
    url(r'^signuppage', views.signuppage, name='signuppage'),
    url(r'^userlogin', views.userlogin, name='userlogin'),
    url(r'^usersignup', views.usersignup, name='usersignup'),
    url(r'^folderhome', views.folderhome, name='folderhome'),
    url(r'^createnewfolder',views.createnewfolder,  name='createnewfolder'),
    url(r'^openfolder/(?P<folder_id>[0-9]+)/$', views.openfolder, name='openfolder'),
    url(r'^addfile', views.addfile, name='addfile'),
    url(r'^deletefile/(?P<folder_id>[0-9]+)/(?P<file_id>[0-9]+)/$', views.deletefile, name='deletefile'),
    url(r'^savefolder/(?P<folder_id>[0-9]+)/$', views.savefolder, name='savefolder'),
    url(r'^deletefolder/(?P<folder_id>[0-9]+)/$', views.deletefolder, name='deletefolder'),
    url(r'^filelogout', views.filelogout, name='filelogout'),

    url(r'^mynotes',views.mynotes,  name='mynotes'),
    url(r'^addnote',views.addnote,  name='addnote'),
    url(r'^savenote/(?P<note_id>[0-9]+)/$', views.savenote, name='savenote'),
    url(r'^deletenote/(?P<note_id>[0-9]+)/$', views.deletenote, name='deletenote'),

    url(r'^videochat',views.videochat,  name='videochat'),
    url(r'^sendMail',views.sendMail,  name='sendMail'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)