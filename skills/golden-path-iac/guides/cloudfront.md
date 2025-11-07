# CloudFront Deployment

**Source files**: 3


## guides/cloudfront-deploy-github-actions.md

# Set up CloudFront deploy with GitHub Actions

- This guide shows how to set up automated deployment of static sites to S3 and CloudFront using GitHub Actions.

- <!-- prettier-ignore-start --> !!! example "Reference implementation" See how [CloudFront deploy workflow is configured in `golden-path-docs`](https://github.com/oslokommune/golden-path-docs/blob/main/.github/workflows/deploy.yml). <!-- prettier-ignore-end -->

## Things to consider

- This workflow uses a composite action that automatically discovers your CloudFront distribution and handles the entire deployment process including S3 sync and cache invalidation.

- The workflow requires your static site to be built before deployment. You can use any build process that outputs static files to a directory.

## Before you begin

- You have set up a CloudFront static website using the CloudFront static website template
- You have configured GitHub secrets for AWS authentication and S3 bucket access
- Your application has a build process that generates static files

## Step 1: Create workflow file

Navigate to your application repository

```bash title="repo-app/"
cd repo-app/
```

Create the GitHub Actions workflow directory

```bash title="repo-app/"
mkdir -p .github/workflows
```

Create the deployment workflow file

```yaml title="repo-app/.github/workflows/deploy.yml"
name: Deploy to CloudFront

on:
  workflow_dispatch:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    permissions:
      id-token: write
      contents: read

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "18"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Build static site
        run: npm run build

      - name: Deploy to CloudFront
        uses: oslokommune/composite-actions/cloudfront-deploy@main
        with:
          aws-role-arn: ${{ secrets.AWS_ROLE_ARN }}
          s3-bucket-name: ${{ secrets.S3_BUCKET_NAME }}
          site-path: "./dist"
```

## Step 2: Customize for your build process

The workflow above uses Node.js and npm, but you can adapt it for your technology stack:

=== "Node.js/npm"

    ```yaml
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '18'
        cache: 'npm'

    - name: Install dependencies
      run: npm ci

    - name: Build static site
      run: npm run build

    - name: Deploy to CloudFront
      uses: oslokommune/composite-actions/cloudfront-deploy@main
      with:
        aws-role-arn: ${{ secrets.AWS_ROLE_ARN }}
        s3-bucket-name: ${{ secrets.S3_BUCKET_NAME }}
        site-path: './dist'
    ```

=== "Hugo"

    ```yaml
    - name: Setup Hugo
      uses: peaceiris/actions-hugo@v2
      with:
        hugo-version: 'latest'

    - name: Build static site
      run: hugo --minify

    - name: Deploy to CloudFront
      uses: oslokommune/composite-actions/cloudfront-deploy@main
      with:
        aws-role-arn: ${{ secrets.AWS_ROLE_ARN }}
        s3-bucket-name: ${{ secrets.S3_BUCKET_NAME }}
        site-path: './public'
    ```

=== "Jekyll"

    ```yaml
    - name: Setup Ruby
      uses: ruby/setup-ruby@v1
      with:
        ruby-version: '3.1'
        bundler-cache: true

    - name: Build static site
      run: bundle exec jekyll build

    - name: Deploy to CloudFront
      uses: oslokommune/composite-actions/cloudfront-deploy@main
      with:
        aws-role-arn: ${{ secrets.AWS_ROLE_ARN }}
        s3-bucket-name: ${{ secrets.S3_BUCKET_NAME }}
        site-path: './_site'
    ```

=== "MkDocs"

    ```yaml
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Build static site
      run: mkdocs build

    - name: Deploy to CloudFront
      uses: oslokommune/composite-actions/cloudfront-deploy@main
      with:
        aws-role-arn: ${{ secrets.AWS_ROLE_ARN }}
        s3-bucket-name: ${{ secrets.S3_BUCKET_NAME }}
        site-path: './site'
    ```

Update the `site-path` parameter to match where your build process outputs the static files.

## Step 3: Verify

Check that the required secrets exist:

```sh
gh secret list --env production
```

You should see these secrets:

- `AWS_ROLE_ARN`
- `S3_BUCKET_NAME`

Push your changes to trigger the workflow

```bash title="repo-app/"
git add .github/
git commit -m "ci: add CloudFront deploy workflow"
git push
```

The workflow will:

- Build your static site using your specified build process
- Sync files to your S3 bucket
- Create CloudFront cache invalidations

## Next step

- Your static site will now be automatically deployed when you push changes to your main branch. Monitor the Actions tab in GitHub to see the deployment progress.


---


## guides/cloudfront-deploy.md

# Set up CloudFront deploy workflow

- This guide shows how to set up automated deployment of static sites to S3 and CloudFront using GitHub Actions.

- <!-- prettier-ignore-start --> !!! example "Reference implementation" See how [CloudFront deploy workflow is configured in `golden-path-docs`](https://github.com/oslokommune/golden-path-docs/tree/main/.github/workflows/_config). <!-- prettier-ignore-end -->

## Things to consider

- This workflow relies on the IAM role created by the CloudFront static website template with `IamForCicd.Enable` set to `true`.

- The workflow uses Docker to build your static site and requires a Dockerfile that produces built files in a specific location within the container.

## Before you begin

- You have set up a CloudFront static website using the CloudFront static website template
- You have enabled `IamForCicd` and run the `set_github_secrets.sh` script to configure GitHub secrets
- Your application repository has a Dockerfile that builds your static site

## Step 1: Create GitHub Actions configuration

Navigate to your application repository

```bash title="repo-app/"
cd repo-app/
```

Create the GitHub Actions configuration directories

```bash title="repo-app/"
mkdir -p .github/workflows/_config/dev
```

Create a common configuration file

```yaml title="repo-app/.github/workflows/_config/dev/common-config.yml"
AccountId: "1234567890"
Region: "eu-west-1"
Team: "pirates"
Environment: "pirates-dev"
```

Create a packages.yml file

```yaml title="repo-app/.github/workflows/_config/dev/packages.yml"
DefaultPackagePathPrefix: "boilerplate/github-actions"
```

## Step 2: Add the package

Add the CloudFront deploy package

```bash title="repo-app/.github/workflows/_config/dev/"
ok pkg add cloudfront-deploy
```

Create package configuration:

```yaml title="repo-app/.github/workflows/_config/dev/cloudfront-deploy.yml"
Name: "monkey"
Environment: "pirates-dev"
DockerContext: "."
DockerfilePath: "Dockerfile"
ContainerSitePath: "/static-website" # (1)!
```

1. Path inside the Docker container where the built static files are located.

??? "Example `Dockerfile` where `ContainerSitePath` is `/static-website`"
    ```dockerfile
    FROM busybox AS build

    RUN mkdir -p /static-website && echo "Hello world!" > /static-website/index.html
    ```

!!! Warning The stage must be named `build`.

Install the package to generate the workflow file:

```bash title="repo-app/.github/workflows/_config/dev/"
ok pkg install
```

## Step 3: Verify

Check that the workflow file was created

```bash title="repo-app/"
ls .github/workflows/
```

You should see a file named `_gp_monkey_pirates-dev_cloudfront_deploy.yml`.

Check that the secrets exist:

```sh
gh secret list --env pirates-dev-monkey
```

You should see these secrets:

- `AWS_ROLE_ARN`
- `S3_BUCKET_NAME`
- `CLOUDFRONT_DISTRIBUTION_ID`

Push your changes to trigger the workflow

```bash title="repo-app/"
git add .github/
git commit -m "ci: add CloudFront deploy workflow"
git push
```

The workflow will:

- Build your static site using Docker
- Extract the built files from the container
- Sync files to your S3 bucket
- Create CloudFront cache invalidations

## Next step

- Your static site will now be automatically deployed when you push changes to your repository. Monitor the Actions tab in GitHub to see the deployment progress.


---


## guides/cloudfront-static-website.md

# Set up CloudFront static website

- This guide shows you how to create a static website hosted on S3 with CloudFront distribution, SSL certificate, and custom domain.

- <!-- prettier-ignore-start --> !!! example "Reference implementation" See how [CloudFront static website is configured in `pirates-iac`](https://github.com/oslokommune/pirates-iac/tree/main/stacks/dev/web-monkey). <!-- prettier-ignore-end -->

## Before you begin

- Have an AWS account with networking and DNS infrastructure configured
- Have the `gh` CLI installed and authenticated

## Step 1: Add the package

Navigate to your infrastructure repository directory:

```bash title="repo-iac/environments/dev/"
cd repo-iac/environments/dev/
```

Add the CloudFront static website package:

```bash title="repo-iac/environments/dev/"
ok pkg add cloudfront-static-website web-monkey # (1)!
```

1. Replace `web-monkey` with a stack name that fits your project.

## Step 2: Configure the package

Create configuration file for your static website:

```yaml title="repo-iac/environments/dev/web-monkey/package-config.yml"
StackName: "web-monkey"
cloudfront-static-website-data.StackName: "web-monkey-data"
Name: "monkey"
RootObject: index.html
ErrorObject: 404.html
RedirectAllToIndex: false # (1)!
AppendIndexToDirectories: false # (2)!
IamForCicd:
  Enable: true
  GitHubRepo: golden-path-docs # (3)!
cloudfront-static-website-data.AutoForwardLogs:
  Enable: false # (4)!
versions.AwsProviderVersion: ">= 6.0.0"
```

1. By default, CloudFront returns a `403 Forbidden` error when someone requests a file that doesn't exist in your S3 bucket. Enable this setting to serve `index.html` instead of the error page. This allows your Single Page Application (SPA) to handle client-side routing - the SPA receives the request and can display the correct content based on the URL path
- 2. When someone visits a directory URL like `/getting-started/`, CloudFront needs to know which file to serve. Enable this to automatically append `index.html` to directory requests, so `/getting-started/` serves `/getting-started/index.html`. 3. Replace `golden-path-docs` with your GitHub repository. 4. Want logs in Datadog? Enable this later.

## Step 3: Install the package

Install the package to generate Terraform files:

```bash title="repo-iac/environments/dev/web-monkey/"
ok pkg install
```

## Step 4: Apply the configuration

Apply the data stack first. This creates the S3 buckets for content and logs:

```bash title="repo-iac/environments/dev/"
cd web-monkey-data/
terraform init
terraform apply
```

Apply the main CloudFront stack:

```bash title="repo-iac/environments/dev/"
cd ../web-monkey/
terraform init
terraform apply # (1)!
```

1. Takes about 5 minutes ⏳

!!! Wait "Time for a break?" It takes about 5 minutes to provision the CloudFront distribution.

The website will be available at `https://web-monkey.pirates-dev.oslo.systems`:

```xml title="Expected error message"
<Error>
  <Code>AccessDenied</Code>
  <Message>Access Denied</Message>
</Error>
```

## Step 5: Upload static files manually (optional)

Upload some files to the S3 bucket with at least one `index.html` file:

```bash
aws s3 sync ./your-static-files/ s3://your-bucket-name/
```

## Step 6: Set up secrets for CI/CD (optional)

Run the script to set up CI/CD secrets for GitHub Actions:

```bash title="repo-iac/environments/dev/web-monkey/"
cd bin/
./set_github_secrets.sh # (1)!
```

1. The script will prompt you to confirm ✅

The script will set these secrets in your GitHub repository:

- `AWS_ROLE_ARN`
- `S3_BUCKET_NAME`
- `CLOUDFRONT_DISTRIBUTION_ID`

## Next step

- Create the [CloudFront deploy workflow](cloudfront-deploy.md) that will allow automated deployment of your static site from GitHub Actions.


---
