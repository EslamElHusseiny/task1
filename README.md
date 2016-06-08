#CoreOS

#Installation steps 

1-Export Enviromental Variables

```
 # export AWS_ACCESS_KEY_ID='Your AWS access key'
 # export AWS_SECRET_ACCESS_KEY='Your AWS secret key'
 # export AWS_DEFAULT_REGION=<Region you wanna create stack in>
 # export Repo=<Enter The repo that contain Yaml and Template file>
``` 

2-Build the container

```
 # docker build -t afarid/stack  .
```
3-Launch Your stack 
`
```
 # docker run -it -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
                  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY  \
                  -e StackName=$StackName \
		  -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION \
		  -e Repo=$Repo afarid/stack
```
