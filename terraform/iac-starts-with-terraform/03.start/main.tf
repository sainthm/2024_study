terraform {
  backend "local" {
    path = "state/terraform.rfstate"
  }
  required_version = ">= 1.0.0"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = ">= 2.0.0"
    }
  }
}

resource "local_file" "abc" {
  content  = "123456!"
  filename = "${path.module}/abc.txt"
}

# resource "local_file" "def" {
#   content  = "def!"
#   filename = "${path.module}/def.txt"
# }