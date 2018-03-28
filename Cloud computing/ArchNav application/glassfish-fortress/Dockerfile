FROM ubuntu

# TODOs:
# check entrypoint works with password
# test all ports
ENV DEBIAN_FRONTEND=noninteractive

# Glassfish
EXPOSE 4848 8080 8181
WORKDIR /
RUN apt-get update -qq > /dev/null && \
    apt-get install unzip wget -qq > /dev/null && \
    wget -q http://download.oracle.com/glassfish/5.0/release/glassfish-5.0.zip && \
    unzip -q -o glassfish-5.0.zip && \
    rm glassfish-5.0.zip && \
    apt-get remove unzip wget -qq > /dev/null && \
    apt-get autoremove -qq > /dev/null && \
    rm -rf /var/lib/apt/lists/*
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["asadmin", "start-domain", "-v"]

# Java 8
RUN apt-get update -qq > /dev/null && \
    apt-get install openjdk-8-jdk -qq > /dev/null && \
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 && \
    apt-get autoremove -qq > /dev/null && \
    rm -rf /var/lib/apt/lists/*

# Fortress OpenLDAP
EXPOSE 389
RUN apt-get update -qq > /dev/null && \
    apt-get install git -qq > /dev/null && \
    git config --global advice.detachedHead false && \
    git clone -q --branch 2.0.0-RC2 https://git-wip-us.apache.org/repos/asf/directory-fortress-core.git /fortress && \
    apt-get remove git -qq > /dev/null && \
    apt-get autoremove -qq > /dev/null && \
    rm -rf /var/lib/apt/lists/*
COPY ./fortress/build.properties ./fortress/slapd.properties /fortress/    
COPY ./fortress/ldap/symas-openldap-silver.deb /fortress/ldap/
RUN apt-get update -qq > /dev/null && \
    apt-get install maven -qq > /dev/null && \
    export M2_HOME=/usr/share/maven && \
    cd /fortress && \
    mvn -q clean install && \
    mvn -q test -Pinit-slapd && \
    mvn -q test -Pstart-slapd && \
    apt-get remove maven -qq > /dev/null && \
    apt-get autoremove -qq > /dev/null && \
    rm -rf /var/lib/apt/lists/*

# ADF Essentials
WORKDIR /
COPY ./adf-essentials.zip /
RUN apt-get update -qq > /dev/null && \
    apt-get install unzip -qq > /dev/null && \
    unzip -q /adf-essentials.zip && \
    rm /adf-essentials.zip && \
    find /modules -name '*.jar' -exec cp {} /glassfish5/glassfish/domains/domain1/lib/ \; && \
    apt-get remove unzip -qq > /dev/null && \
    apt-get autoremove -qq > /dev/null && \
    rm -rf /var/lib/apt/lists/*

# Archemy
COPY ./opt/glassfish5/glassfish/lib/mysql-connector-java-5.1.40-bin.jar /opt/glassfish5/glassfish/lib/
COPY ./opt/glassfish5/glassfish/domains/domain1/lib/archemy-security-1.0-SNAPSHOT-jar-with-dependencies.jar /opt/glassfish5/glassfish/domains/domain1/lib/

# Installing Java 7
#RUN apt-get update -qq > /dev/null && \
#    apt-get install software-properties-common -qq > /dev/null && \
#    add-apt-repository ppa:openjdk-r/ppa && \
#    apt-get update -qq > /dev/null && \
#    apt-get install openjdk-7-jdk -qq > /dev/null && \
#    export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64 && \
#    apt-get remove software-properties-common -qq > /dev/null && \
#    apt-get autoremove -qq > /dev/null && \
#    rm -rf /var/lib/apt/lists/*
ENV GLASSFISH_PASSWORD=password \
    PATH=$PATH:$JAVA_HOME/bin:/glassfish5/bin