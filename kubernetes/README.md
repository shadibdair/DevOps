## Automate snapshot creation for specifec container/pod

- Trigger snapshot weekly on Sunday. 
- Using default Kubernetes object: CronJob.
- The image can be kubectl so a kubectl apply -f filename.yaml can be invoked.
- Need to dynamically change the VolumeSnapshot name to include the according to date.
