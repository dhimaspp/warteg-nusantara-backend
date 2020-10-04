from rest_framework import serializers, status
from users.models import Profile, User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password", "last_login")


class ProfileSerializers(serializers.ModelSerializer):
    user = UserSerializers(required=True)

    class Meta:
        model = Profile
        fields = ("user", "bio", "pp")

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop("user")
        user = UserSerializers.create(
            UserSerializers(), validated_data=user_data)
        user_profile, created = Profile.objects.update_or_create(user=user,
                                                                 bio=validated_data.pop("bio"), pp=validated_data.pop("pp"))
        return user_profile

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
