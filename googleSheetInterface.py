from __future__ import print_function
import os.path
from google.auth.transport import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

class MyGoogleSheet():
    def __init__(self, Spreadsheet_Id):
        self.ID = Spreadsheet_Id
        self.credentials = None

        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.SERVICE_ACCOUNT_FILE = 'keys.json' 

        self.Sheet = None

    def Init(self):

        self.credentials = service_account.Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES) 
        service = build('sheets', 'v4', credentials=self.credentials)
        self.Sheet = service.spreadsheets()

    def ReadData(self, range_name):
        result = self.Sheet.values().get(spreadsheetId=self.ID,
                            range=range_name).execute()
        values = result.get('values', [])
        return values
    
    # values as array[]
    def WriteData(self, range_name, values):
        request = self.Sheet.values().update(spreadsheetId=self.ID,range=range_name, valueInputOption="USER_ENTERED", body={"values": values}).execute()
        
