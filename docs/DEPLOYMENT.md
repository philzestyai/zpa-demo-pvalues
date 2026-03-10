# DEPLOYMENT

This file is intended as a reference point for capturing manual steps required
for a successful deployment of the service.

## Process

The deployment process for this service uses xxx pipelines to deploy a xxx
application on [AWS/Azure] consisting of xxx.

The stack is created using xxx and configured via xxx.

## Environments

Deployment to an environment is trggered by merging into the relevant branch.
The following branches have been configured:

- `master` deploys to `prd`
- `dev` deploys to `dev`

## Secrets

The required environment variables for this service are:

```
EXAMPLE_VAR=...
```

These are configured to be pulled from [parameter store/key vault] as part of
the deployment - ensure all parameters have been created and seeded prior to
initial deployment.

## Data

### Schema

This service required the schema defined [here](../src/scripts/schema.sql) to
be configured in the database.
