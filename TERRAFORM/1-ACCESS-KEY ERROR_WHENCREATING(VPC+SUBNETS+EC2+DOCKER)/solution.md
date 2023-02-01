I tried to create a VPC and two Subnets(Private+Public)+EC2 instance+Docker with Terraform file. But it failed. I found the solution by putting the "code block" shown below and then I executed again. This time there was no error. It worked.


# Generates a secure private key and encodes it as PEM

 ``resource "tls_private_key" "key_pair" {
    
      algorithm = "RSA"
    
      rsa_bits  = 4096
}``
# Create the Key Pair

resource "aws_key_pair" "key_pair" {
  
     key_name   = "mykey"  
  
     public_key = tls_private_key.key_pair.public_key_openssh

} 

# Save file

``resource "local_file" "ssh_key" {
  
    filename = "${aws_key_pair.key_pair.key_name}.pem"
    
    content  = tls_private_key.key_pair.private_key_pem

}``


This code block created automaticlly a key_pair(.pem) in AWS without any manuel tryings in AWS managemant console.