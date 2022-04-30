import dropbox

class UploadFiles :

    def __init__(self , accessToken):
        self.AccessToken = accessToken


    def uploadFile(self , source , destination):
        dbx = dropbox.Dropbox(self.AccessToken)

        with open(source, 'rb') as f:
            dbx.files_upload(f.read() , destination) 
        print("uploaded")



def main():
    accessToken = "sl.BGuj25IT4oF1MfYuFMBq4KmvY5WPt57iF_btv2YGwr_m7_jZLfVdnIggTEijYYnE7hvQcBeAlmhpUeFDgstahm6r7Fi_a60co75agvYfmeLioZNZAExRGgvE3KljeLWq7CB6QKV0aIxy"

    obj = UploadFiles(accessToken)

    source = "demo.txt"
    destination ="/new/intro.txt"
    obj.uploadFile(source , destination)
  


main()