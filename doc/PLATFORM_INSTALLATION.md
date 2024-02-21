# Platform installation

## Pre-requisistes

To be able to install the platform and its components, you need first a kubernetes cluster running.

You can use [k3d](https://k3d.io/), [minikube](https://minikube.sigs.k8s.io/docs/start/) or [kind](https://kind.sigs.k8s.io/docs/user/quick-start/) for example.

You will also need:
* [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [Argo CD CLI](https://argo-cd.readthedocs.io/en/stable/getting_started/#2-download-argo-cd-cli)

## Platform components

In your kubernetes cluster, we'll start by installing Argo CD.

```bash
./argo-projects/install-argo-cd.sh
```

Once installed, we'll use Argo CD to deploy absolutely everything in the cluster. It will even watch and patch itself !

// insert image

Using Argo CD, we will deploy some infrastructure components:
* [Ingress Nginx controller](https://github.com/kubernetes/ingress-nginx): to be able to expose ingresses to the Argo CD and Argo Workflows interfaces, and also act as a load balancer for our canary tests using Argo Rollouts
* [Docker-registry](https://artifacthub.io/packages/helm/phntom/docker-registry): to handle and serve our microservice images
* [Prometheus stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack): to gather microservice's prometheus metrics and use them as analysis in our progressive rollout

It will also take care of installing the Argo Projects:
* Argo CD, patching itself !
* Argo Workflow
* Argo Events
* Argo Rollouts

## Components installation

Once the Argo CD installation run, you can access the UI with a simple port-forward:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:80
```

This is only needed as long as we have not patched the installation with an additional ingress.

You can now access the Argo CD interface at "http://localhost:8080".
You can connect using the "admin" user and the password retrieved by executing the command:

```bash
argocd admin initial-password -n argocd
```

You can now create an application using the 'New App' button.

// insert button picture

You can use the following parameters as reference:

// insert app picture

You should now have all components deployed in your cluster:

// insert argocd app state

**This is it**. This was the last manual action you had to perform on the platform !

## Access the UI

You can now access the UI at:

- Argo CD: https://argocd.127.0.0.1.nip.io/
- Argo Workflows (+ Events): https://argo-workflows.127.0.0.1.nip.io/workflows 