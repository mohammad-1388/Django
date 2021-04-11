from django.contrib.auth.models import User
from django.db import models

from accounts.models import Profile, GroupUsers, MuteUsers, AdminUsers, BlockedUsers, CancelUsers, LikesUsers, \
    VisitsUsers

CTM = lambda C: tuple([(x, C[x]) for x in C])


class Message(models.Model):
    """
        Represent A Message
    """

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام'

    text = models.TextField('متن')
    date = models.DateTimeField('تاریخ', auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='نویسنده', null=True)
    to_user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='گیرنده')
    is_system = models.BooleanField('از طرف سیستم', default=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.writer.get_full_name() + " to " + self.to_user.user.get_full_name() + " => " + self.text[:10]


class Group(models.Model):
    """
     Represent A Group
    """

    class Meta:
        verbose_name = "گروه"
        verbose_name_plural = "گروه ها"

    name = models.CharField('عنوان', max_length=255)
    link = models.CharField('لینک', max_length=100, null=True, blank=True, unique=True)
    add_link = models.TextField('لینک عضویت', null=True, blank=True, unique=True)
    mute_users = models.ForeignKey(MuteUsers, on_delete=models.PROTECT, verbose_name='مشاهده کنندگان')
    users = models.ForeignKey(GroupUsers, on_delete=models.PROTECT, verbose_name='اعضا')
    admin_users = models.ForeignKey(AdminUsers, on_delete=models.PROTECT, verbose_name='مدیران')
    blocked_users = models.ForeignKey(BlockedUsers, on_delete=models.PROTECT, verbose_name='مسدود شده ها')
    cancel_users = models.ForeignKey(CancelUsers, on_delete=models.PROTECT, verbose_name='افراد ترک کرده')
    STATUS_ADD_U = 1
    STATUS_ADD_B = 2
    STATUS_ADD_M = 3
    STATUS_ADD_W = 4
    STATUS_ADD_A = 5
    status_choices_l = {
        STATUS_ADD_U: 'عضو شود',
        STATUS_ADD_B: 'مسدود شود',
        STATUS_ADD_M: 'فقط بتواند مشاهده کند',
        STATUS_ADD_W: 'نتواند عضو شود فقط ببیند',
        STATUS_ADD_A: 'مدیر شود',
    }
    status_choices_a = status_choices_l.copy()
    status_choices_a[STATUS_ADD_W] = 'لینک از کار بیفتد'

    on_link = models.IntegerField(' درزمان اضافه شدن با لینک', choices=CTM(status_choices_l))
    on_add_link = models.IntegerField('در زمان اضافه شدن با لینک عضویت', choices=CTM(status_choices_a))
    description = models.TextField('توضیحات')

    def __str__(self):
        return self.name + self.description[:10]

    def __repr__(self):
        return self.__str__()


class MessageGroup(models.Model):
    """
        The Model Represent a Message Group
    """

    class Meta:
        verbose_name = 'پیام گروهی'
        verbose_name_plural = 'پیام گروهی'

    text = models.TextField('متن')
    date = models.DateTimeField('تاریخ', auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='نویسنده', null=True)
    group = models.ManyToManyField(Group, verbose_name='گروه')
    visit = models.OneToOneField(VisitsUsers, on_delete=models.PROTECT)
    like = models.OneToOneField(LikesUsers, on_delete=models.PROTECT)

    @property
    def like_count(self):
        return self.like.users.count()

    @property
    def visit_count(self):
        return self.visit.users.count()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.writer.get_full_name() + " to " + self.group.__str__() + " => " + self.text[:10]
