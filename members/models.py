from django.db import models
from django.contrib.auth.models import User
from website.models import Package
from django.db.models.signals import pre_save
from django.utils.text import slugify


class MembershipNumber(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='identification',
                                blank=True,
                                null=True)
    id_number = models.CharField(max_length=13, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.id_number


def create_slug(instance, new_slug=None):
    slug = slugify(instance.id_number)
    if new_slug is not None:
        slug = new_slug
    qs = MembershipNumber.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%$-%$" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_MembershipNumber_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_MembershipNumber_receiver, sender=MembershipNumber)

STATUS_CHOICES = (
    ('pending', 'pending'),
    ('active', 'active'),
    ('deceased', 'deceased'),
    ('cancelled', 'cancelled'),
)


class Member(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    # membership_no = models.ForeignKey(MembershipNumber,
    #                                   on_delete=models.CASCADE,
    #                                   related_name='member',
    #                                   blank=True,
    #                                   null=True)
    package = models.ForeignKey(Package,
                                max_length=15,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    phone_2 = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=15,
                              choices=STATUS_CHOICES,
                              default="pending")
    recieved_by = models.CharField(max_length=250, default='online')
    burial_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.first_name


class Spouse(models.Model):
    status = models.CharField(max_length=15,
                              choices=STATUS_CHOICES,
                              default="active")
    membership_no = models.ForeignKey(MembershipNumber,
                                      on_delete=models.CASCADE,
                                      related_name='spouse')
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    id_no = models.CharField(max_length=13,
                             blank=True,
                             null=True,
                             db_index=True,
                             unique=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    phone_2 = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField(unique=True)
    burial_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.first_name


def spouse_slug(instance, new_slug=None):
    slug = slugify(instance.id_no)
    if new_slug is not None:
        slug = new_slug
    qs = Spouse.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%$-%$" % (slug, qs.first().id)
        return spouse_slug(instance, new_slug=new_slug)
    return slug


def pre_save_Spouse_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = spouse_slug(instance)


pre_save.connect(pre_save_Spouse_receiver, sender=Spouse)


class Family(models.Model):
    status = models.CharField(max_length=15,
                              choices=STATUS_CHOICES,
                              default="active")
    membership_no = models.ForeignKey(MembershipNumber,
                                      on_delete=models.CASCADE,
                                      related_name='family')

    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    id_no = models.CharField(max_length=13, blank=True, null=True, unique=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    phone_2 = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField(unique=True)
    burial_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # class Meta:
    #     ordering = ['-created']

    def __str__(self):
        return self.first_name


def fam_slug(instance, new_slug=None):
    slug = slugify(instance.id_no)
    if new_slug is not None:
        slug = new_slug
    qs = Family.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%$-%$" % (slug, qs.first().id)
        return fam_slug(instance, new_slug=new_slug)
    return slug


def pre_save_Family_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = fam_slug(instance)


pre_save.connect(pre_save_Family_receiver, sender=Family)


class Document(models.Model):
    membership_no = models.ForeignKey(MembershipNumber,
                                      on_delete=models.CASCADE,
                                      related_name='document',
                                      blank=True,
                                      null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d',
                               blank=True,
                               null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


"""

class Bar(models.Model):
    external_id = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.external_id


class Bazz(models.Model):
    bar = models.ForeignKey(Bar,
                            to_field='external_id',
                            on_delete=models.CASCADE)


"""
