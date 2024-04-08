# Platform manifests

You have seen with the [platform installation](PLATFORM_INSTALLATION.md) that Argo CD is taking care of deploying all the resources and is constantly watching them to prevent any drift.

Let's take a tour around those resources so that you understand how it works.

The single entrypoint for Argo CD is a [kustomization file](https://github.com/AmadeusITGroup/argo-projects-demo/blob/main/argo-projects/kustomization.yaml):

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - argo-cd/argo-cd-app.yaml
  - argo-workflows/argo-workflows-app.yaml
  - argo-rollouts/argo-rollouts-app.yaml
  - argo-events/argo-events-app.yaml
  - infra/infra-app.yaml
  - app/app-appset.yaml
```

It's referencing all Argo CD [Applications](https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#applications) or [ApplicationSets](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/).

Each of those `Applications` are referencing the git repository, in their own folder. Argo CD reads then the local `kustomization.yaml` file in each of those folders to include or patch more resources.

## Argo CD

In the Argo CD `Application`, and [folder](https://github.com/AmadeusITGroup/argo-projects-demo/blob/main/argo-projects/argo-cd/kustomization.yaml), we are deploying:

* The latest Argo CD manifests from github
* The `argocd` namespace
* An ingress to access the UI
* Some patches to change the controller options, and configure the notifications (see [Promotion Workflow](./PROMOTION_WORKFLOW.md))

## Argo Workflows

In the Argo Workflows `Application`, and [folder](https://github.com/AmadeusITGroup/argo-projects-demo/blob/main/argo-projects/argo-workflows/kustomization.yaml), we are deploying:

* The latest Argo Workflwos manifests from github
* The `argo` namespace
* An ingress to access the UI
* Some patches to change the argo server configuration
* Some manifests used for the [promotion Workflow](./PROMOTION_WORKFLOW.md).

## Argo Events

In the Argo Events `Application`, and [folder](https://github.com/AmadeusITGroup/argo-projects-demo/blob/main/argo-projects/argo-events/kustomization.yaml), we are deploying:

* The lastest Argo Events manifests from github
* Patches to deploy those resources in the 'argo' namespace, alongside Argo Workflows
* Some manifests used for the [promotion Workflow](./PROMOTION_WORKFLOW.md).

## Argo Rollouts

In the Argo Rollouts `Application`, and [folder](https://github.com/AmadeusITGroup/argo-projects-demo/blob/main/argo-projects/argo-rollouts/kustomization.yaml), we are deploying:

* The lastest Argo Rollouts manifests from github
* The `argo-rollouts` namespace
* Some manifests used for the [progressive rollout](./PROGRESSIVE_ROLLOUT.md).

## Infra

In the Infra `Application`, and [folder](https://github.com/AmadeusITGroup/argo-projects-demo/blob/main/argo-projects/infra/kustomization.yaml), we are deploying:

* The `infra` namespace
* The prometheus stack, nginx ingress controller and docker registry using a [multi-source Application](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/): ref [here](https://github.com/AmadeusITGroup/argo-projects-demo/blob/main/argo-projects/infra/infra-app.yaml#L7-L29).
* A `ServiceMonitor` to scrape the prometheus metrics from the demo app on both test and prod namespaces: ref [here](https://github.com/AmadeusITGroup/argo-projects-demo/blob/main/argo-projects/infra/resources/app-service-monitor.yaml)

## The demo application

In the app `ApplicationSet` and [folder](https://github.com/AmadeusITGroup/argo-projects-demo/tree/main/argo-projects/app), we are deploying the helm chart of the demo application that contains:

* A `Namespace` (for convenience, you would probably not use that inside your application chart)
* A `Deployment`
* A `Rollout` (see [progressive rollout](./PROGRESSIVE_ROLLOUT.md))
* `Services` to access the application pod endpoint
* An `Ingress` to access the application service

The `ApplicationSet` is using json file generators to generate the two corresponding instance: test and prod:

```yaml
spec:
  generators:
    - git:
        repoURL: https://github.com/AmadeusITGroup/argo-projects-demo.git
        revision: HEAD
        files:
          - path: "argo-projects/app/generators/*.json"
```

The application folder is structured as a kustomize app:

```
base/
    --chart definition
overlays/
    test/
        --test values, including app version
    prod/
        --prod values, including app version
```

**This structure here is convenient for the demo use case, do not take it as a best practice for applications deployment.**

In real life, you would probably publish your chart to a remote helm registry, and reference it directly in your Argo CD `Application`.

The application version could also be linked to the chart version, if a new version of the chart is pushed alongside the image of the application. In this case, bumping the chart version would be enough to bump the application version.