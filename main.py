import boto3
import os

S3_NAME = 'photokb867452'


def get_zip_files(directory='.'):
    """
    Get a list of all zip files in a directory

    :param directory: The directory to search for zip files in
    :return: A list of zip file names
    """
    zip_file_names = []
    for filename in os.listdir(directory):
        file_base_name, file_extension = os.path.splitext(filename)
        if file_extension.lower() == ".zip":
            zip_file_names.append(filename)
    return zip_file_names


class S3Client():
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(bucket_name)

    def __repr__(self):
        return f'S3Client({self.bucket_name})'

    def upload_file(self, file_name):
        self.bucket.upload_file(file_name, file_name)
        print(f'File {file_name} uploaded to {self.bucket_name}')
        return True

    def check_if_file_exists(self, file_name):
        for obj in self.bucket.objects.all():
            if obj.key == file_name:
                return True
        return False

    def download_file(self, file_name):
        ...

if __name__ == '__main__':
    s3client = S3Client(S3_NAME)
    zip_files = get_zip_files()

    for file in zip_files:
        if not s3client.check_if_file_exists(file):
            s3client.upload_file(file)
        else:
            print(f'File {file} already exists')
