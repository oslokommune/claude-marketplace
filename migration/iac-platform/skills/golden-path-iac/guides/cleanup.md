# Environment Cleanup

**Source files**: 2


## guides/delete/delete-environment.md

# Delete the environment

If you wish to delete the environment you created, follow the instructions below.

## Delete the application stack

```bash title="repo-iac/dev/myapp"
terraform destroy
```

## Delete the infrastructure stack

- We will use `terraform destroy` to delete all the stacks, but we also need to manually delete the AWS S3 bucket that was created by the `remote_state` stack.

```bash title="repo-iac/dev/infra"
terraform destroy
```

## Delete the remote state stack

```bash title="repo-iac/dev/remote_state"
terraform destroy
```

## Manually delete the S3 bucket

Go to the [guides document](delete-remote-state-bucket.md) to learn how to delete the S3 bucket.


---


## guides/delete/delete-remote-state-bucket.md

# Delete the remote state bucket

- After destroying each stack using `terraform destroy`, you will need to manually delete the S3 bucket used for remote state storage. This is because Terraform does not support deleting S3 buckets that are not empty.

## Using the AWS CLI

List the buckets in the AWS account:

```bash
aws s3 ls
```

```bash
2020-01-01 00:00:00 ok-iac-config-12345678910-eu-west-1-my-team-dev
```

Delete the bucket:

```bash
aws s3 rb s3://ok-iac-config-12345678910-eu-west-1-my-team-dev --force
```

## Using the AWS Management Console

- !!! info "Bucket name" The name of the bucket is inherited from the `metadata.environment` value in the `env.yml` file.

    ```text title="Example bucket name"
    ok-iac-config-12345678910-eu-west-1-my-team-dev
    ```

1. Go to the AWS console and navigate to the [S3 list](https://s3.console.aws.amazon.com/s3/home?region=eu-west-1){:target=\"_blank\"}.
- 2. Click on the bucket that was created by the `remote_state` stack. 3. Click on the **Empty** button. 4. Click on the **Delete** button.


---
