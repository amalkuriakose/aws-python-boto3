import boto3

client = boto3.client('dynamodb')

# First create a table called TestTable using AWS Console/CLI/SDK with partition key as id and sort key as name

option = input('Enter 1 to put item.\nEnter 2 to get item.\n')

if option:
    if int(option) == 1:
        id = input('Enter id: ')
        name = input('Enter name: ')
        if id and name:
            try:
                response = client.put_item(
                    TableName='TestTable',
                    Item={'id': { 'N': id}, 'name': { 'S': name}, 'title': {'S': 'test title'}}
                )
                print(response)
            except Exception as e:
                print(e)
                print('Unable to put item')
        else:
            print('Invalid values')
    elif int(option) == 2:
        id = input('Enter id: ')
        name = input('Enter name: ')
        if id and name:
            try:
                response = client.get_item(
                    TableName='TestTable',
                    Key={'id': {'N': id}, 'name': {'S': name}}
                )
                print(response)
            except Exception as e:
                print('Unable to get item')
                print(e)
        else:
            print('Invalid values')