#write a Python script to build and push the images to Dockerhub.  Ensure the script can take the tag, build variable (dev or prod), Docker registry (writing this as a Python script means it can be run on any operating system)

#the images  will not change as well as the docker registry (andriuskl). The only variables that will change are the tag and build variable. The script should be able to be run from the command line and take the tag and build variable as arguments, and for loop through the three images so they all have te same tag and build variables.

#test the function using andriuskl as the docker registry, dev as the build variable and v1.0 as the tag and shop-front-svc as the folder

import subprocess
import sys

def build_and_push_images(tag):
    images = ['catalog-svc', 'product-admin-svc', 'shop-front-svc']
    docker_registry = 'andriuskl'

    for image in images:
        image_name = f"{docker_registry}/{image}:{tag}"
        print(f"Building {image_name}...")
        
        # Build the Docker image
        build_command = f"docker build -t {image_name} ./{image}"
        subprocess.run(build_command, shell=True, check=True)
        
        # Push the Docker image to Dockerhub
        push_command = f"docker push {image_name}"
        subprocess.run(push_command, shell=True, check=True)




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python build.py <tag>")
        sys.exit(1)

    tag = sys.argv[1]

    
    build_and_push_images(tag,)

