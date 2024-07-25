import requests
from pathlib import Path
import time

api_key = "0457f35f91c5260b0ddb1d79a3065c08efe85d858c35d9158a2cb981998ded50"

def scan_file(api_key, file_path):
    with open(file_path, "rb") as data:

        url = 'https://www.virustotal.com/vtapi/v2/file/scan'

        params = {'apikey': api_key}

        files = {"file": data}

        response = requests.post(url, files= files, params = params)

        return get_report(api_key, response.json()["resource"])


def get_report(api_key, resourceId):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {"apikey": api_key, "resource": resourceId}

    while True:
        r = requests.get(url, params=params)
        r.raise_for_status()  # Raise an error for bad responses (e.g., 404)
        

        report = r.json()
        if report['response_code'] == 1:
            return report
      


       
          # Adjust delay time as needed\



def scan_directory(path):
    # itme is file:

    if path.is_file():
        response = scan_file(api_key, path)
        time.sleep(61)

        
        positives = response["positives"]
        
        if positives == 0:
            print(f"File {path} is good (not detected as malicious).")

        else:
            print(f"File {path} is flagged by {positives} antivirus engines.")

    # item is a folder:
    else:
        for item in path.iterdir():
            scan_directory(item )





def main():

    directory_path = Path(input("enter folder/file to start with: "))

    scan_directory(directory_path)





if __name__ == "__main__":
    main()






