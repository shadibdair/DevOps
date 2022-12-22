import boto3
# pip install python-decouple
from decouple import config

# Global Variable
reached = 0

# Environment Variables
ACCESS_KEY = config('ACCESS_KEY')
SECRET_KEY = config('SECRET_KEY')
TOKEN_KEY = config('TOKEN_KEY')
REGION = config('REGION')
MAX_NLB = config('MAX_NLB')
MAX_ALB = config('MAX_ALB')
MAX_CLB = config('MAX_CLB')


session = boto3.Session(
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=TOKEN_KEY,
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
            if nlb_percentage >= 80:
                print("NLB count reached = ", float(nlb_percentage))
                reached +=1

            alb_percentage = precentage(cnt_alb, MAX_ALB)
            if alb_percentage >= 80:
                print("ALB count reached = ", float(alb_percentage))
                reached +=1
        
    except Exception as exc:
        print(exc)
        exit(1)

# Func that gets the percentage of values.
def precentage(value, max):
    # Calculating %
    response=(int(value)/int(max))*100 
    return response

# Check If any of load balancers reached 80 %
def check():
    global reached
    if reached != 0:
        print("Stop program")
        exit()

# Main func
def main():
    global reached
    print("Classic Load Balancer")
    count_alb = all_lb(lb_type='elb')
    elb_percentage = precentage(count_alb, MAX_CLB)
    if elb_percentage >= 80:
        print("ALB count reached = ", float(elb_percentage))
        reached +=1


    print("\nNetwork/Application Load Balancer")
    all_lb(lb_type='elbv2')

    check()


if __name__ == "__main__":
    main()