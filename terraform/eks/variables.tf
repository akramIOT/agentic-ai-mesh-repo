variable "aws_region" {}
variable "cluster_name" { default = "agentic-eks" }
variable "vpc_id" {}
variable "subnets" { type = list(string) }
