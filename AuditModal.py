from django.db import models
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from django.contrib.auth import get_user_model
from  saleor.account.models import User


class AuditModel(models.Model):
    row_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_created')
    row_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_updated')
    row_created_at = models.DateTimeField(auto_now_add=True)
    row_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        print("current user-->", get_current_user(), get_current_authenticated_user())

        if not self.id:
            self.row_created_by = user  # self.updated_by_audit
            print("createdby")
        else:
            print("updatedby")
            self.row_updated_by = user  # self.updated_by_audit
        super().save(*args, **kwargs)

