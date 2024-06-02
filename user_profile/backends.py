from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserProfile = get_user_model()


class UserProfileBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        if username is None:
            username = kwargs.get(UserProfile.USERNAME_FIELD)

        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            pass

        # Cek apakah user sudah ditemukan lewat username, jika belum maka cek lewat email
        # dan nomor HP

        if user is None:
            try:
                user = UserProfile.objects.get(email=username)
            except UserProfile.DoesNotExist:
                pass

        if user is None:
            try:
                user = UserProfile.objects.get(nomor_hp=username)
            except UserProfile.DoesNotExist:
                pass

        # Jika user ditemukan dan melewati pengecekan password dan
        if user is not None and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    def login(self, request, user):
        super.login(request, user)
