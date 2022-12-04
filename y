version = 0.1
[y]
[y.deploy]
[y.deploy.parameters]
stack_name = "sam-app"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-8864rfdzfnoa"
s3_prefix = "sam-app"
region = "us-west-2"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
disable_rollback = true
parameter_overrides = "ParameterInstancePrefix=\"loan\""
image_repositories = []
