import boto3

client = boto3.client('sqs')
QueueUrl = 'https://sqs.us-east-1.amazonaws.com/123456789012/TestQueue'

option =  input('Enter 1 to send message to the queue.\nEnter 2 to receive messages from the queue.\nEnter 3 to delete a message.\n')

if int(option) == 1:
    message = input('Enter message: ')
    if message:
        try:
            response = client.send_message(
                QueueUrl=QueueUrl,
                MessageBody=message
            )
            print(response)
        except:
            print('Unable to send message')
elif int(option) == 2:
    try:
        response = client.receive_message(
            QueueUrl=QueueUrl,
            MaxNumberOfMessages=10
        )
        print(response)
    except:
        print('Unable to receive messages')
elif int(option) == 3:
    receipt_handle = input('Enter receipt handle: ')
    if receipt_handle:
        try:
            response = client.delete_message(
                QueueUrl=QueueUrl,
                ReceiptHandle=receipt_handle
            )
            print(response)
        except:
            print('Unable to delete message')