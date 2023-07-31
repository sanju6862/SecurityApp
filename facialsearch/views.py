import boto3
import io
from PIL import Image
from django.shortcuts import render
from users.models import *
import imghdr
from django.contrib.auth.decorators import login_required

rekognition = boto3.client('rekognition', region_name='us-east-1')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')
bucket_name = 'students-iitbhu'
folder_prefix = 'index'

@login_required
def facialsearch(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated and user.profile.user_type != 'security':
            print(user.profile.user_type)
            return render(request, 'facialsearch/bhag.html', {})

        uploaded_files = request.FILES.getlist('images')
        
        found_users = set()  # Change to set
        
        for uploaded_file in uploaded_files:

            image = Image.open(uploaded_file)

            # Convert the image to RGB if it is not already in RGB format
            if image.mode != 'RGB':
                image = image.convert('RGB')

            stream = io.BytesIO()
            image.save(stream, format="JPEG")
            image_binary = stream.getvalue()

            response = rekognition.search_faces_by_image(
                CollectionId='students',
                Image={'Bytes': image_binary}
            )

            for match in response['FaceMatches']:
                face_id = match['Face']['FaceId']
                confidence = match['Face']['Confidence']

                response = dynamodb.get_item(
                    TableName='students',
                    Key={'RekognitionId': {'S': face_id}}
                )

                if 'Item' in response:
                    username = response['Item']['FullName']['S']
                    found_users.add(username)  # Add to set

        profiles = Profile.objects.filter(user__username__in=found_users)

        return render(request, 'facialsearch/facialsearchresults.html', {'profiles': profiles})

    return render(request, 'facialsearch/facialsearch.html')
