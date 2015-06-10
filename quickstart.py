#!/usr/bin/python
import httplib2
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow

# Copy your credentials from the console
CLIENT_ID = '95549989400-2dh5v48239rridk4knmlkc02o3s700iv.apps.googleusercontent.com'
CLIENT_SECRET = 'sX0uboC1EEVut16-OP6q9lx1'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Run through the OAuth flow and retrieve credentials
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, redirect_uri=REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()

print 'Go to the following link in your browser: ' + authorize_url
code = raw_input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

drive_service.revisions().update(
    fileId = '1L-Ck0qUaF_ym9frGWNtPDAUUoVbeZlWIAKnnn4FfRDc',
    revisionId='head',
    body={
        'published':True,
        'publishAuto': True
    }
).execute()