1. get minikube running
locate minikube directory fo to it in console and type minikube start
make sure docker desktop is running

now wait for it to be done
open a new terminal and type minikube dashboard
let it run a browser should open up

no open another terminal and go to the directory called deployment
so cd base - > cd deployment
one here type in kubectl apply -k .
let it push eveything to kubernetes

now open a new terminal and run minikube tunnel

this will allow you to go to teh webpage via url of localhost if not working then try localhost/getcatalog

that is how to get it working


!!Troubleshooting
make sure you are in correct directories when using the commands

if ingress is not working then use the following command minikube addons enable ingress
this will add ingress as an addon. 

now close everything down, for the tunnel its just ctrl +c
for dashboard its ctrl + c 
for minikube itself, use minikube stop
then wait 5 min and run it again