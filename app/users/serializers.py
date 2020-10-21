from rest_framework import serializers, status
from users.models import Profile, User
from django.contrib.auth.validators import UnicodeUsernameValidator


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "user", "bio", "pp")

        # extra_kwargs = {
        #     'user': {
        #         'validators': [],
        #     }
        # }


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name",
                  "email", "password", "last_login")


class UserNestedSerializers(serializers.ModelSerializer):
    profile_user = ProfileSerializers()

    class Meta:
        model = User
        fields = ("id", "username", "first_name",
                  "email", "password", "last_login", "profile_user")
        # extra_kwargs = {
        #     'username': {
        #         'validators': [],
        #     }
        # }

    # def create(self, validated_data):
    #     profile_data = validated_data.pop("profile_user")
    #     user_create = User.objects.create(**validated_data)
    #     for profil_data in profile_data:
    #         Profile.objects.create(user=user_create, **profil_data)
    #     return user_create

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop("profile_user")
    #     profile_update = (instance.profile_user)
    #     profile = profile_update.pop(0)
    #     instance.username = validated_data.get("username", instance.username)
    #     instance.first_name = validated_data.get(
    #         "first_name", instance.first_name)
    #     instance.email = validated_data.get("email", instance.email)
    #     instance.password = validated_data.get("password", instance.password)
    #     instance.last_login = validated_data.get(
    #         "last_login", instance.last_login)
    #     instance.save()
    #     profile.bio = profile_data.get("bio", instance.bio)
    #     profile.pp = profile_data.get("pp", instance.pp)
    #     profile.save()
    #     return instance

# TODO: overiding validating username


# class ProfileSerializers(serializers.ModelSerializer):
#     user = UserSerializers(required=True, many=True)

#     class Meta:
#         model = Profile
#         fields = ("id", "user", "bio", "pp")

#     def create(self, validated_data):
#         """
#         Overriding the default create method of the Model serializer.
#         :param validated_data: data containing all the details of student
#         :return: returns a successfully created student record
#         """
#         user_data = validated_data.pop("user")
#         user = UserSerializers.create(
#             UserSerializers(), validated_data=user_data)
#         user_profile = Profile.objects.update_or_create(user=user,
#                                                         bio=validated_data.pop("bio"), pp=validated_data.pop("pp"))
#         return user_profile

#     def update(self, instance, validated_data):
#         user_data = validated_data.pop("user")
#         user = UserSerializers.create(
#             UserSerializers(), validated_data=user_data)
#         instance.user = user
#         instance.bio = validated_data.get("bio", instance.bio)
#         instance.pp = validated_data.get("pp", instance.pp)
#         instance.save
#         return instance

    # def update(self, instance, validated_data):
    #     user_data = validated_data.pop("user")
    #     username = user_data.pop("username")
    #     user = get_user_model().object.getcreate

        #("profile_id", "nama", "bio", "pp", "fav_food",)


# class usersViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = UsersSerializers
#     renderer_classes = (JSONRenderer, )
#     parser_classes = (JSONParser,)

# TODO: masukin initial Data objek
# TODO: test viewset
# TODO: Tambahin app POST dan TM
# TODO: create collection API to postman
# TODO: apply change to production
