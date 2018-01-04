from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class PasswordUpdate(APIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request, *args, **kwargs):
        """
        Validates user's existing credentials
        Updates password
        Deletes user's existing token
        Generates a new token
        Return new token id
        """
        password = request.data['newPassword']
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user and user.is_active:
            user.set_password(password)
            user.save()
            token = Token.objects.get(user=user)
            token.delete()
            new_token = Token.objects.create(user=user)
            if user.is_staff:
                groups = [group.name for group in user.groups.all()]
            else:
                groups = ['property_contact']

            return Response({'token': new_token.key, 'id': user.id, 'email': user.email, 'username': user.username,
                             'firstName': user.first_name, 'lastName': user.last_name, 'groups': groups})

        else:
            raise APIException('AuthenticationFailed')
