#store the terraform state file in s3
terraform {
    backend "s3" {
        bucket   = "terraform-remote-statee"
        key      = "EarlyBeam-website-ecs.tfstate"
        region   = "us-east-1"
        profile  = "XXXXXXXX"
    }
}