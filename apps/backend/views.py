import base64
import imp
import requests
import json
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class ResumeParserAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        APIURL="https://rest.rchilli.com/RChilliParser/Rchilli/parseResumeBinary"
        USERKEY = '8QPVX7RX'
        VERSION = '8.0.0'
        subUserId = 'Bobby Singh'

        # file absolutepath and file name
        # filePath='SampleResume.docx'
        # fileName='SampleResume.docx'
        filePath = request.FILES['file']
        print("@@@@@@@@@@@@@    ")
        fileName='SampleResume.docx'
        # do some stuff with uploaded file

        # with open(filePath, "rb") as filePath:
        encoded_string = base64.b64encode(filePath.read())
        data64 = encoded_string.decode('UTF-8')
        # data64 = str(base64.b64encode(filePath))

        headers = {'content-type': 'application/json'}

        body =  """{"filedata":\""""+data64+"""\","filename":\""""+ fileName+"""\","userkey":\""""+ USERKEY+"""\",\"version\":\""""+VERSION+"""\",\"subuserid\":\""""+subUserId+"""\"}"""

        response = requests.post(APIURL,data=body,headers=headers)
        resp =json.loads(response.text)

        #please handle error too
        Resume =resp["ResumeParserData"]

        #read values from response
        print (Resume["Name"]["FirstName"])
        print (Resume["Name"]["LastName"])
        print (Resume["Email"])
        print (Resume["SegregatedExperience"])


        return Response({"status": 200,"response": Resume })