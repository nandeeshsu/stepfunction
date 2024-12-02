import boto3
import csv
import os

s3_client = boto3.client('s3')
ecs_client = boto3.client('ecs')


def lambda_handler(event, context):
    print('Started')
    # Step 1: Get the S3 file location and task definitions from Step Function input
    bucket_name = event['bucket_name']
    file_key = event['file_key']
    cluster_name = event['cluster_name']
    task_definitions = event['task_definitions']  # Expecting a list of task definitions

    print('bucket_name:', bucket_name)

    # Step 2: Download the CSV file from S3
    local_file = '/tmp/store_ranges.csv'
    s3_client.download_file(bucket_name, file_key, local_file)

    # Step 3: Parse the CSV to get store ranges
    task_arns = []
    with open(local_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            start = row['Start']
            end = row['End']

            print('Processing range - Start:', start, 'End:', end)

            # Step 4: Trigger ECS Task for each range and task definition
            for task_definition in task_definitions:
                response = ecs_client.run_task(
                    cluster=cluster_name,
                    taskDefinition=task_definition,
                    launchType='FARGATE',
                    networkConfiguration={
                        'awsvpcConfiguration': {
                            'subnets': [
                                'subnet-08c5266ee7383588e',
                                'subnet-078594168b1a5bffe',
                                'subnet-0c75a69e8d0c50f5d',
                                'subnet-053cd4aa7cba652c0',
                                'subnet-05bf635de1b91bc28',
                                'subnet-01e1eae286254e561'
                            ],  # Replace with your subnet IDs
                            'securityGroups': ['sg-02e017bf9999d5106'],  # Replace with your security group IDs
                            'assignPublicIp': 'ENABLED'  # Or 'DISABLED' based on your use case
                        }
                    },
                    overrides={
                        'containerOverrides': [
                            {
                                'name': task_definition,
                                'environment': [
                                    {'name': 'START', 'value': start},
                                    {'name': 'END', 'value': end}
                                ]
                            }
                        ]
                    },
                    count=1
                )
                print("Task triggered for task definition", task_definition, "Response:", response)

                if response['tasks']:
                    task_arn = response['tasks'][0]['taskArn']
                    task_arns.append({
                        'task_arn': [task_arn],
                        'cluster_name': cluster_name,
                        'task_definition': task_definition
                    })

    # Step 5: Return the ECS Task ARNs
    return {
        'task_arns': task_arns
    }
