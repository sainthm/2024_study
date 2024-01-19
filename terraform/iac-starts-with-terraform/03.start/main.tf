# terraform {
#   backend "local" {
#     path = "state/terraform.rfstate"
#   }
#   required_version = ">= 1.0.0"
#   required_providers {
#     local = {
#       source  = "hashicorp/local"
#       version = ">= 2.0.0"
#     }
#   }
# }

resource "local_file" "abc" {
  content  = "lifecycle - step 5"
  filename = "${path.module}/abc.txt"

  lifecycle {
    # create_before_destroy = true
    # prevent_destroy = true
    ignore_changes = [
      content
    ]
  }
}

# resource "local_file" "def" {
#   depends_on = [
#     local_file.abc
#   ]
#   # content  = local_file.abc.content
#   content  = "456!"
#   filename = "${path.module}/def.txt"
# }

# resource "aws_instance" "web" {
#   ami           = "ami-02d081c743d676996"
#   instance_type = "t2.micro"
# }