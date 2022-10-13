# 🦊 Priority based expander for cluster-autoscaler.

## 🥷🏻 Introduction

Priority based expander selects an expansion option based on priorities assigned by a user to scaling groups. The assignment is based on matching of the scaling group's name to regular expressions. The correct and meaningful naming of scaling groups is left up to the user.

## 🍔 Motivation

This expander gives the user a lot of control over which scaling group specifically will be used by cluster-autoscaler. It makes a lot of sense when configured manually by the user to match the specific needs. It also makes a lot of sense for environments where user's preferences change frequently based on properties outside of cluster scope. A good example here is the constant change of pricing and termination probability on AWS Spot Market for EC2 instances.
The expander is configured using a single ConfigMap, which is watched by the expander for any changes. The priority expander can be easily integrated with external optimization engines, that can just change the value of the ConfigMap configuration object. That way it's possible to dynamically change the decision of cluster-autoscaler using ConfigMap updates only.

-----


# 🌟 Some explanations

## Node Group
```
A node group is one or more Amazon EC2 instances that are deployed in an Amazon EC2 Auto Scaling group.
All instances in a node group must have the following characteristics: Be the same instance type.
Be running the same Amazon Machine Image (AMI) Use the same Amazon EKS node IAM role.
```