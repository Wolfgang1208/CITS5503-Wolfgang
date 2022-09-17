aws dynamodb create-table \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --table-class STANDARD

    # aws dynamodb put-item \
    # --table-name CloudFile \
    # --item '{"userId": {
    #     "S": "22951266-cloudstorage"
    # },
    # "filename": {
    #     "S": "rootfile.txt"
    # },
    # "path": {
    #     "S": "./rootdir"
    # },
    # "lastUpdated": {
    #     "S": "2022-08-18 04:57:28+00:00"
    # },
    # "owner": {
    #     "S": "mdanwarulkaium.patwary"
    # },
    # "permission": {
    #     "S": "FULL_CONTROL"
    # }
    # }' \
    # --endpoint-url=http://localhost:8000 \
    # --return-consumed-capacity TOTAL