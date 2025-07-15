from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def health(request):
    """Health check endpoint to verify server status."""
    return Response({"message": "Server is up!"})

# PUBLIC_INTERFACE
class NoteListCreateView(ListCreateAPIView):
    """
    get:
    List all notes.

    post:
    Create a new note.
    """
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer

# PUBLIC_INTERFACE
class NoteRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
    Retrieve a note by id.

    put:
    Update a note by id.

    patch:
    Partially update a note by id.

    delete:
    Delete a note by id.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
