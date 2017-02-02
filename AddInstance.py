'''
Created on Feb 2, 2017

@author: sourjain
'''

import troposphere.ec2 as ec2
from troposphere import Template, Ref

####Define existing AWS Environment####
#AccessCIDR=""                    #CIDR range that you want to have access through the security group
#VPC_ID= ""                       #ID of the existing VPC you want to use
SubnetID = "subnet-202c6a56"      #ID of the existing subnet you want to use
ImageID = "ami-b9b394ca"          #ID of the AMI to use for your instance
SGID = "sg-ff35ab99"              #ID of the SGID to use for your instance

####Define existing AWS Environment####

template = Template() 

####Create Instance####
i01 = ec2.Instance("DoctorApp")
i01.ImageId = ImageID
i01.InstanceType = "t2.micro"
i01.SubnetId = SubnetID
i01.SecurityGroupIds = [SGID]
template.add_resource(i01)
####Create Instance####

####Create Instance####
i02 = ec2.Instance("DoctorDB")
i02.ImageId = ImageID
i02.InstanceType = "t2.micro"
i02.SubnetId = SubnetID
i02.SecurityGroupIds = [SGID]
template.add_resource(i02)
####Create Instance####

####Create Elastic IP####
EIP01 = ec2.EIP("ElasticIP")
EIP01.InstanceId = Ref(i01)
EIP01.Domain = "vpc"
template.add_resource(EIP01)
####Create Elastic IP####

print(template.to_json())