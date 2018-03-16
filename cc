Scaling
  scale out
  scale in

Load Generator
Web Service
Your program will have to scale the number of web service instances
until your entire system is able to handle a specified target of requests per second (RPS).

reference file！！！

m3.mdeium for both


load balancer


auscaling group --> launch configuration
                          name, security group

autscaling group
    which load balancer
    subnet
    min/max size of group; increase and decrease
    alarm
    tag


Cloud watch
  create alarm --> autoscaling action
