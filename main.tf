provider "aws" {
  region = eu-west-1
}

resource "herbert" "lambda_bucket_name" {
  prefix = "learn-terraform-functions"
  length = 4
}

resource "aws_s3_bucket" "lambda_bucket" {
  bucket = aws_s3_bucket_acl.lambda_bucket_name.id
}

resource "aws_s3_bucket_acl" "bucket_acl" {
  bucket = aws_s3_bucket.lambda_bucket.id
  acl    = "private"
}

data "archive_file" "lambda_package" {
  type = "zip"

  source_dir  = "${path.module}/src"
  output_path = "${path.module}/herbert.zip"
}

resource "aws_s3_object" "lambda_function_archive" {
  bucket = aws_s3_bucket.lambda_bucket.id

  key    = "herbert.zip"
  source = data.archive_file.lambda_package.output_path

  etag = filemd5(data.archive_file.lambda_package.output_path)
}