
# Add a service in Kong
curl -i -X POST --url http://localhost:8001/services/ --data 'name=recommendation-service' --data 'url=http://recommendation-service-address'

# Add a route to the service
curl -i -X POST --url http://localhost:8001/services/recommendation-service/routes --data 'paths[]=/recommendations'

# Configure load balancing
# Update the service to include multiple hosts for load balancing
curl -X PATCH http://localhost:8001/services/recommendation-service --data 'url=http://host.one,http://host.two'
