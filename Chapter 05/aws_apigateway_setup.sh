
# Create a VPC link
aws apigateway create-vpc-link --name "recommendation-vpc-link" --target-arns "arn:aws:elasticloadbalancing:region:account-id:loadbalancer/target-group-arn"

# Create a new API
aws apigatewayv2 create-api --name "RecommendationAPI" --protocol-type "HTTP"

# Create a route
aws apigatewayv2 create-route --api-id "your-api-id" --route-key "GET /recommendations" --target "integrations/your-integration-id"

# Create an integration
aws apigatewayv2 create-integration --api-id "your-api-id" --integration-type "HTTP_PROXY" --integration-method "GET" --integration-uri "http://your-service-url/recommendations" --connection-type "VPC_LINK" --connection-id "your-vpc-link-id"
