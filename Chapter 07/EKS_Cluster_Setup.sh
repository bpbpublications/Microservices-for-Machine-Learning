
# Initial deployment: Setup an EKS Cluster
eksctl create cluster --name music-recommendation-cluster --region us-west-2 --nodegroup-name standard-workers --node-type t2.medium --nodes 3
