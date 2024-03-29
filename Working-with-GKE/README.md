# Setting Up Google Cloud and Creating a Kubernetes Cluster with GKE

This guide provides a step-by-step walkthrough to set up a Google Cloud account, install the Google Cloud CLI (Command Line Interface), and create a Kubernetes cluster using Google Kubernetes Engine (GKE).

## 1. Create Google Cloud Account

If you haven't already, you need to create a Google Cloud account:

1. Go to the [Google Cloud Platform website](https://cloud.google.com/).
2. Click on the "Get started for free" button or "Go to Console" if you already have an account.
3. Follow the instructions to create your account.
4. Provide the necessary information, including billing details.

## 2. Setting Up Google Cloud CLI

Once you have a Google Cloud account, you need to set up the Google Cloud CLI:

1. Install the Google Cloud SDK by following the instructions provided [here](https://cloud.google.com/sdk/docs/install).
2. After installation, run the following command in your terminal to authenticate the gcloud CLI tool:

    ```bash
    gcloud auth login
    ```

3. Follow the prompts to authenticate using your Google Cloud account.

4. Set the default project for the gcloud CLI by running:

    ```bash
    gcloud config set project YOUR_PROJECT_ID
    ```

   Replace `YOUR_PROJECT_ID` with the ID of your Google Cloud project.

## 3. Create Kubernetes Cluster with GKE

Now that you have Google Cloud CLI set up, you can create a Kubernetes cluster using Google Kubernetes Engine (GKE):

1. Open your terminal and run the following command to create a new Kubernetes cluster:

    ```bash
    gcloud container clusters create YOUR_CLUSTER_NAME --num-nodes=3 --zone=YOUR_ZONE
    ```

    Replace `YOUR_CLUSTER_NAME` with the desired name for your cluster and `YOUR_ZONE` with the desired zone for your cluster.

    For example:

    ```bash
    gcloud container clusters create my-cluster --num-nodes=3 --zone=us-central1-a
    ```

2. Wait for the cluster creation process to complete. It may take a few minutes.

3. Once the cluster is created, configure `kubectl`, the Kubernetes command-line tool, to use the new cluster:

    ```bash
    gcloud container clusters get-credentials YOUR_CLUSTER_NAME --zone=YOUR_ZONE
    ```

    Replace `YOUR_CLUSTER_NAME` and `YOUR_ZONE` with the appropriate values.

    For example:

    ```bash
    gcloud container clusters get-credentials my-cluster --zone=us-central1-a
    ```

4. Verify that `kubectl` is configured correctly by running:

    ```bash
    kubectl get nodes
    ```

    You should see the nodes of your Kubernetes cluster listed.

Congratulations! You have successfully created a Google Cloud account, set up Google Cloud CLI, and created a Kubernetes cluster using Google Kubernetes Engine (GKE). You can now deploy and manage your applications on Kubernetes.

# Delete Steps


    gcloud container clusters delete my-cluster --zone=us-central1-a