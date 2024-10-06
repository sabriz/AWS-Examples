import json

# Define the IAM policy
iam_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket-name",  # Replace with your bucket name
                "arn:aws:s3:::your-bucket-name/*"  # Replace with your bucket name
            ]
        }
    ]
}

# Specify the file name
file_name = 's3_read_policy.json'

# Write the policy to a JSON file
with open(file_name, 'w') as json_file:
    json.dump(iam_policy, json_file, indent=4)

print(f"Policy JSON has been written to {file_name}")
