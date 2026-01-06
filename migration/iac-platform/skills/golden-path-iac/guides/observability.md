# Observability

**Source files**: 4


## guides/observability-customize-otel-config.md

# Customize OTel configuration

Customize the OTel configuration to control which telemetry your application sends to Datadog.

## Things to consider

- !!! warning "Custom metric pricing" While custom metrics that you emit from your application can be valuable for business and system insights, they can be somewhat expensive as Datadog and most observability vendors treat each unique combination of metric attribute values as separate metrics. For this reason you should be concious of the number of custom metrics you emit, and especially avoid metric attributes that take on a high number of values (also called high-dimensionality) such as user IDs, IP addresses and timestamps. If it's difficult to remove certain metrics or metric attributes at the application layer, you can instead have the OTel collector filter them out by customizing the OTel configuration.

## Before you begin

Make sure you have:

- Completed the [getting started guide to set up basic Datadog integration](observability-getting-started.md).
- An application deployed using the `app` template with telemetry-collection enabled.

## Filter out specific metrics

```hcl title="stacks/dev/app-example/config_override.tf"
locals {
  otel_metric_config = {
    ignored_metrics = [
      # NOTE: We always want to remove the metrics below
      "^http\\.server\\.request\\.duration$",
      "^http\\.client\\.request\\.duration$",
      "^otlp\\.exporter\\.exported$",
      "^otlp\\.exporter\\.seen$",
      "^queueSize$",
      "^processedLogs$",
      "^processedSpans$",
      # TODO: Add the name of the metric you want to remove here
    ]
  }
}

```

## Remove metric attributes

```hcl title="stacks/dev/app-example/config_override.tf"
locals {
  # We add a new OTel processor to the OTel configuration
  otel_additional_processors = {
    "transform/remove_metric_attributes" = {
      metric_statements = [
        # Remove an attribute from all metrics
        "delete_key(datapoint.attributes, \"example.attribute\")",
        # Remove attribute only from specific metric
        "delete_key(datapoint.attributes, \"example.attribute\") where metric.name == \"system.memory.usage\""
      ]
    }
  }

  # We add our new processor to the OTel pipeline that contains metrics
  otel_pipeline_processors = {
    "metrics" = {
      processors = ["transform/remove_metric_attributes"]
    }
  }
}
```

## Only keep traces from a specific endpoint

```hcl title="stacks/dev/app-example/config_override.tf"
locals {
  # Configure tail sampling to only keep traces from a specific endpoint
  otel_tail_sampling_config = {
    additional_policies = [
      {
        name = "drop-everything-but-one-route"
        type = "drop"
        drop = {
          drop_sub_policy = [
            {
              name = "inverted-match"
              type = "string_attribute"
              string_attribute = {
                key                    = "http.route"
                values                 = ["^/my-route$"]
                enabled_regex_matching = true
                invert_match           = true
              }
            }
          ]
        }
      }
    ]
  }
}
```

## Bring your own OTel Collector configuration

- !!! warning When you bring your own OTel configuration, you'll lose useful behavior and telemetry tags that the Golden Path provides out-of-the-box. Consider using the `otel-config-generator` Terraform module to extend the default configuration rather than replacing it completely, or ask Kjøremiljø to support your use case.

```hcl title="stacks/dev/app-example/config_override.tf"
locals {
  otel_config = yamlencode(file("my-config.yml"))
}
```


---


## guides/observability-getting-started.md



# Get started with Datadog

- This guide helps you set up Datadog integration in your AWS accounts to enable observability for your applications and infrastructure. Once configured, you'll collect logs, metrics, and traces from applications and AWS services in your accounts.

## Before you begin

- Make sure that TEK or Team Kjøremiljø has created a team for you in the [origo-datadog-iac](https://github.com/oslokommune/origo-datadog-iac/tree/main/teams) repository.

- Need help? Contact Team Kjøremiljø in [the `#origo-kjøremiljø-support` Slack channel](https://oslokommune.slack.com/archives/CV9EGL9UG).

- You may need to update your privacy assessment for medium and low risk, PLM (personvernvurdering på lav og middels risiko). So check with your lawyer and infosec people wether the new data flows created for Datadog require changes in your team's PLM.

## Step 1: Install the `datadog-common` template

- The `datadog-common` template sets up the necessary shared resources for Datadog integration in each AWS account.

1. Navigate to the root of an environment in your infrastructure repository (e.g., `stacks/dev`).
1. Add the `datadog-common` package to your environment:

    ```sh
    ok pkg add datadog-common
    ```

1. Navigate to the `datadog-common` directory:

    ```sh
    cd datadog-common
    ```

1. Open `package-config.yml` and set a name for the stack:

    ```diff title="stacks/dev/datadog-common/package-config.yml"
    +StackName: datadog-common
    ```

1. Install the template:

    ```sh
    ok pkg install
    ```

1. Review the generated Terraform configuration and apply the changes:

    ```sh
    terraform plan
    terraform apply
    ```

## Step 2: Verify the setup

Verify that the Datadog integration is working:

1. Log in to Datadog using your Microsoft email: [https://app.datadoghq.eu/account/login/by_email](https://app.datadoghq.eu/account/login/by_email).
1. Select the `Origo` organization if prompted.
1. Navigate to [Integrations > Amazon Web Services](https://app.datadoghq.eu/integrations?integrationId=amazon-web-services).
1. Verify that your AWS account is listed without errors.

## Next steps

With the basic Datadog integration in place, you can now:

- [Instrument Java applications](observability-java-instrumentation.md) to collect application metrics, logs, and traces.
- [Forward CloudWatch and ALB logs](observability-log-forwarding.md) to Datadog for centralized log management.

- If you have questions about or issues with any of this, please reach out in the [#origo-kjøremiljø-support](https://oslokommune.slack.com/archives/CV9EGL9UG) Slack channel and we'll help you out!


---


## guides/observability-java-instrumentation.md

# Instrument a Java container for Datadog

- This guide shows you how to instrument Java applications running in Amazon ECS containers. OpenTelemetry Collector will be configured to collect the resulting logs, metrics, and traces.

## Things to consider

- !!! tip "Recommended practice" Enable auto-instrumentation to automatically capture useful telemetry from HTTP requests, database queries, external service calls, and application logs. You don't need to change any code in your app.

## Before you begin

Make sure you have:

- Completed the [getting started guide to set up basic Datadog integration](observability-getting-started.md).
- A Java application deployed using the `app` template.

## Step 1: Enable telemetry collection and auto-instrumentation

- Auto-instrumentation automatically captures logs, metrics, and traces from your Java app. You don't need to change any code in your app.

1. Update to the newest version of the `app` template for the application you want to instrument.

2. Edit your `package-config.yml` file to enable telemetry collection:

    ```yml
    TelemetryCollection:
      Enable: true
      AutoInstrumentation:
        Enable: true # Disable this if you're already bundling the Java Agent with your application
        Runtime: java # This is the only supported runtime for auto-instrumentation
    ```

3. Apply the configuration:

    ```sh
    ok pkg install
    ```

4. Apply the Terraform configuration:

    ```sh
    terraform plan
    terraform apply
    ```

## Step 2: Add manual instrumentation (optional)

- Auto-instrumentation provides basic telemetry, but custom business metrics need manual instrumentation with the OpenTelemetry SDK. Add the API dependency and use `@WithSpan` annotations or the API directly.

- For detailed instructions on manual instrumentation, see the [OpenTelemetry Java documentation](https://opentelemetry.io/docs/instrumentation/java/manual/).

## Step 3: Verify instrumentation

- Check Datadog for incoming traces, metrics, and logs.  Use the `env` and `service` tags to filter the results. For example:

```text
env:pirates-dev service:too-tikki`.
```

## Next steps

With an instrumented application you can now:

- [Customize OTel configuration](observability-customize-otel-config.md) to more granularly control which telemetry gets sent to Datadog from your application.


---


## guides/observability-log-forwarding.md

# Forward logs from CloudWatch and S3 to Datadog

This guide shows you how to forward logs from AWS CloudWatch and S3 (like ALB logs) to Datadog.

## Before you begin

Make sure that you have:

- Completed the [getting started guide](observability-getting-started.md) to set up basic Datadog integration.
- A CloudWatch log group or S3 bucket with logs that you want to forward to Datadog.

## Things to consider

- !!! tip "Recommended practice" Set up log forwarding in each stack where a log source exists rather than creating a centralized forwarding setup. This approach reduces coupling between stacks and makes it easier to manage permissions and dependencies.

- !!! tip "All bucket or log group tags are forwarded to Datadog" As an example, if a log group or S3 bucket logically belongs to a specific application, you might want to add a `service` tag to it in AWS. The same tag will then make its way to Datadog and make it easier to query across all relevant logs for a given application.

- !!! note "ALB logs and `load-balancing-alb` template" If you're using the `load-balancing-alb` template, ALB log forwarding is automatically configured in newer versions. Check if you need to update your template version and apply the update (both in the ALB stack and associated `-data` stack).

## Step 1: Forward CloudWatch logs

- Use the `datadog-log-subscription` module to forward CloudWatch logs. Add it to your Terraform configuration:

```hcl title="dev/stacks/example-cloudwatch-data/datadog.tf"
module "forward_to_datadog" {
  source              = "git@github.com:oslokommune/golden-path-iac//terraform/modules/datadog-log-subscription?ref=datadog-log-subscription-v0.1.2"
  environment         = local.environment
  cloudwatch_sources  = {
    example = {
      log_group_name  = aws_cloudwatch_log_group.application.name
    }
  }
}
```

## Step 2: Forward S3 logs

For S3, add S3 sources to the same module:

```hcl title="dev/stacks/example-s3-data/datadog.tf"
module "forward_to_datadog" {
  source              = "git@github.com:oslokommune/golden-path-iac//terraform/modules/datadog-log-subscription?ref=datadog-log-subscription-v0.1.2"
  environment         = local.environment
  s3_sources = {
    example = {
      bucket_name = aws_s3_bucket.logs.name
    }
  }
}
```

## Step 3: Apply the configuration

Run Terraform to create the log forwarding resources:

```sh
terraform plan
terraform apply
```

## Step 4: Verify log forwarding

- Check the [Log Explorer in Datadog](https://app.datadoghq.eu/logs) for incoming logs. Use the `env` and `source` tags to filter results:

```text
env:pirates-dev source:(elb OR cloudwatch)
```

- !!! note "Existing log entries aren't forwarded" Only log entries created in CloudWatch or S3 _after_ enabling forwarding will be sent to Datadog.

- !!! warning "Timestamp format requirements" If your logs contain a `timestamp` attribute, it must use ISO8601, UNIX (milliseconds EPOCH), or RFC3164 format. Unsupported formats cause logs to be filtered by Datadog. See [Datadog preprocessing documentation](https://docs.datadoghq.com/logs/log_configuration/pipelines/?tab=date#preprocessing) for details.


---
