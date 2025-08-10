module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = var.cluster_name
  cluster_version = "1.26"
  subnets         = var.subnets
  vpc_id          = var.vpc_id
  node_groups = {
    default = {
      desired_capacity = 2
      max_capacity     = 3
      min_capacity     = 1
      instance_type    = "m5.large"
    }
  }
}

output "kubeconfig" {
  value = module.eks.kubeconfig
}
