from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.journal import Journal
from ..serializers import JournalSerializer, UserSerializer

# Create your views here.
class Journals(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = JournalSerializer
    def get(self, request):
        """Index request"""
        # Get all the journals:
        # journals = Journal.objects.all()
        # Filter the journals by owner, so you can only see your owned journals
        journals = Journal.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = JournalSerializer(journals, many=True).data
        return Response({ 'journals': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['journal']['owner'] = request.user.id
        # Serialize/create journal
        journal = JournalSerializer(data=request.data['journal'])
        # If the journal data is valid according to our serializer...
        if journal.is_valid():
            # Save the created journal & send a response
            journal.save()
            return Response({ 'journal': journal.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(journal.errors, status=status.HTTP_400_BAD_REQUEST)

class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the journal to show
        journal = get_object_or_404(Journal, pk=pk)
        # Only want to show owned journals?
        if not request.user.id == journal.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this journal')

        # Run the data through the serializer so it's formatted
        data = JournalSerializer(journal).data
        return Response({ 'journal': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate journal to delete
        journal = get_object_or_404(Journal, pk=pk)
        # Check the journal's owner agains the user making this request
        if not request.user.id == journal.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this journal')
        # Only delete if the user owns the  journal
        journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # 1. Check if there's an `owner` key on the incoming data
        # We don't want people to physically update the `owner` of a journal
        # later, after we already set the owner on create
        # If the request.data['journal'] dictionary has a key of 'owner'
        # if request.data['journal'].get('owner'):
            # If the key exists, delete it from the dictionary
            # del request.data['journal']['owner']
        journal = get_object_or_404(Journal, pk=pk)
        # If you get an error about "Something object is not subscriptable"
        # it means you cannot use the square bracket syntax
        # (and it's probably not an object in this case)
        # if not request.user == journal['owner']:
        # 2. Check if user making the request is the same as journal's owner ID
        if not request.user.id == journal.owner.id:
            raise PermissionDenied('You do not own this journal')
        # 3. Attach the incoming request's user's id to the journal as the `owner`
        # This ends up overwriting any incoming `owner` data
        # and makes step #1 redundant
        request.data['journal']['owner'] = request.user.id
        # Validate updates with serializer
        ms = JournalSerializer(journal, data=request.data['journal'])
        # Allow a partial update w/ our serializer by passing `partial` as True
        ms = JournalSerializer(journal, data=request.data['journal'], partial=True)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
