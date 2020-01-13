FROM openjdk

WORKDIR /usr/src/app
RUN yum -y install wget
RUN yum -y install vim
RUN yum -y install rsync

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.10/swagger-codegen-cli-2.4.10.jar -O swagger-codegen-cli.jar

COPY canopy-swagger-no-allof.json .
