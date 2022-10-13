from http import client
import boto3

client = boto3.client('rekognition')

bucketName = "22951266-cloudstorage"

urbunPic = "DF5DC8211A4643CB853D12ADBC36A458_recompress.jpg"

manBeachPic = "15135cb3d515dc58fef12804898d3452.jpeg"

okPic = "86abfd73c12b5b26d378e2c80ab9ccd7.jpeg"

wordyPic = "b5a35dfcd04dada1a77f3ffe5784fe06.jpeg"

pictures = []

pictures.append(urbunPic)

pictures.append(manBeachPic)

pictures.append(okPic)

pictures.append(wordyPic)

def labelsML(pic):
    print(f"Labels detection from {bucketName}/{pic}:")
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucketName,
                'Name': pic,
            }
        },
        MaxLabels=50,
    )
    for names in response['Labels']:
        print(f"label: {names['Name']}, confidence: {int(names['Confidence'])}%")
    #print(response)
    print("____________________________________________")



for pics in pictures:
    labelsML(pics)