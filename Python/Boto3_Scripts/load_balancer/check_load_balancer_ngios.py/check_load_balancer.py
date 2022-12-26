#!/bin/python3
import boto3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('AccessKey' , type=str, help='AccessKey')
parser.add_argument('SecretKey' , type=str, help='SecretKey')
parser.add_argument('Region' , type=str, help='Region')
parser.add_argument('MAX_NLB' , type=str, help='MAX_NLB')
parser.add_argument('MAX_ALB' , type=str, help='MAX_ALB')
parser.add_argument('MAX_CLB' , type=str, help='MAX_CLB')

args = parser.parse_args()

# Environment Variables
ACCESS_KEY = args.AccessKey
SECRET_KEY = args.SecretKey
REGION = args.Region
MAX_NLB = args.MAX_NLB
MAX_ALB = args.MAX_ALB
MAX_CLB = args.MAX_CLB


session = boto3.Session(
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
    )

# Func that get lb's
def all_lb(lb_type,*args):
    try:
        global reached
        if lb_type == 'elb':
            elb = session.client('elb')
            return len(elb.describe_load_balancers()['LoadBalancerDescriptions'])
            
        elif lb_type == 'elbv2':
            elb = session.client('elbv2')
            name = 'LoadBalancers'

            lb = elb.describe_load_balancers()
            # Count LB
            cnt_nlb = 0
            cnt_alb = 0


            # Filter types 
            for item in lb[name]:
                if item['Type'] == "network":
                    cnt_nlb +=1
                elif item['Type'] == "application":
                    cnt_alb +=1
            
            nlb_percentage = precentage(cnt_nlb, MAX_NLB)
            alb_percentage = precentage(cnt_alb, MAX_ALB)
            return (nlb_percentage, alb_percentage)
        
    except Exception as exc:
        print(exc)
        exit(1)

# Func that gets the percentage of values.
def precentage(value, max):
    # Calculating %
    response=(int(value)/int(max))*100 
    return response

# Check If any of load balancers reached 80 %
def check(reached):
    if reached > 0:
        # 2 --> Critical, 1 Warning
        exit(2)

# Main func
def main():

    reached = 0

    # Checking Classic load balancer (elb)
    count_alb = all_lb(lb_type='elb')

    elb_percentage = precentage(count_alb, MAX_CLB)
    if elb_percentage >= 80:
        print("CLB=%d;;;;" % int(elb_percentage))
        reached += 1
    
    # Checking Application & Network load balancer (elbv2)
    count_elbv2 = all_lb(lb_type='elbv2')
    # Checking Network load balancer
    if count_elbv2[0] >= 80:
        # For ngios
        print("NLB=%d;;;;" % int(count_elbv2[0]))
        reached += 1
    # Checking Application load balancer
    if count_elbv2[1] >= 80:
        # For ngios
        print("ALB=%d;;;;" % int(count_elbv2[1]))
        reached += 1


    check(reached)


if __name__ == "__main__":
    main()