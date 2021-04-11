from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    The Model Represent A Profile Account
    """

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')

    mobile = models.CharField('شماره تلفن', max_length=50, null=True, blank=True)

    idUser = models.CharField('آی دی', unique=True, max_length=255)

    profile_picture = models.ImageField(upload_to='users_profile/', verbose_name='پروفایل', null=True, blank=True)

    def __str__(self):
        return self.user.get_username() + " - " + self.user.get_full_name()


class GroupUsers(models.Model):
    """
    The Model Represent a GroupUsers
    """

    class Meta:
        verbose_name = 'مجموعه'
        verbose_name_plural = 'مجموعه'

    users = models.ManyToManyField(User, verbose_name='کاربر ها')

    def __str__(self):
        return "مجموعه کاربر های " + str(self.pk)

    def __repr__(self):
        return self.__str__()


class MuteUsers(models.Model):
    users = models.ForeignKey(GroupUsers, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.users)

    def __repr__(self):
        return self.__str__()


class AdminUsers(models.Model):
    users = models.ForeignKey(GroupUsers, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.users)

    def __repr__(self):
        return self.__str__()


class BlockedUsers(models.Model):
    users = models.ForeignKey(GroupUsers, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.users) + ""

    def __repr__(self):
        return self.__str__()


class CancelUsers(models.Model):
    users = models.ForeignKey(GroupUsers, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.users)

    def __repr__(self):
        return self.__str__()


class LikesUsers(models.Model):
    users = models.ManyToManyField(User)

    def __str__(self):
        return str(self.users)

    def __repr__(self):
        return self.__str__()


class VisitsUsers(models.Model):
    users = models.ManyToManyField(User)

    def __str__(self):
        return str(self.users)

    def __repr__(self):
        return self.__str__()
