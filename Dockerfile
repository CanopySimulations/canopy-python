FROM openapitools/openapi-generator-cli:v6.0.1
ENV PATH="/opt/openapi-generator/modules/openapi-generator-cli/target:${PATH}"
RUN mkdir /canopy
RUN ln -s /opt/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar /canopy/openapi-generator-cli.jar
WORKDIR /canopy
COPY ./generate_client.sh .
RUN chmod +x ./generate_client.sh 
