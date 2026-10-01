from .serializer import StudentSerializer
from .models import StudentDetails

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# GET - Get all students
@api_view(['GET'])
def getStudents(request):

    students = StudentDetails.objects.all()

    serializer = StudentSerializer(students, many=True)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

# POST - Create a new student
@api_view(['POST'])
def createStudent(request):

    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['PUT'])
def updateStudent(request, stid):

    try:
        student = StudentDetails.objects.get(pk=stid)

    except StudentDetails.DoesNotExist:

        return Response(
            {
                'error': 'Student not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = StudentSerializer(
        student,
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


# DELETE - Delete a student
@api_view(['DELETE'])
def deleteStudent(request,stid):

    try:
        student = StudentDetails.objects.get(pk=stid)

    except StudentDetails.DoesNotExist:

        return Response(
            {
                'error': 'Student not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )

    student.delete()

    return Response(
        {
            'message': 'Student deleted successfully'
        },
        status=status.HTTP_204_NO_CONTENT
    )
