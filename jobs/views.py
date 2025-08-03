from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer
from .models import Job


@api_view(['GET'])
def job_list(request):
    """
    List all jobs or create a new job.
    """
    jobs = Job.objects.all()

    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)
