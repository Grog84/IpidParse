from __future__ import print_function
import os.path
from google.auth.credentials import Scoped
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from google.oauth2 import service_account

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES) 

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'


service = build('sheets', 'v4', credentials=credentials)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))

