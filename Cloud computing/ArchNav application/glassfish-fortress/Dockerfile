FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive

# Fortress OpenLDAP
EXPOSE 389
RUN apt-get update -qq > /dev/null && \
    apt-get install git -qq > /dev/null && \
    git config --global advice.detachedHead false && \
    git clone -q --branch 2.0.0-RC2 https://git-wip-us.apache.org/repos/asf/directory-fortress-core.git /fortress && \
    apt-get remove git -qq > /dev/null && \
    apt-get autoremove -qq > /dev/null && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /fortress
COPY fortress/build.properties fortress/slapd.properties ./
COPY fortress/ldap/symas-openldap-silver.deb ./ldap/symas-openldap-silver.deb
RUN apt-get update -qq > /dev/null && \
    apt-get install maven openjdk-8-jdk -qq > /dev/null && \
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 && \
    M2_HOME=/usr/share/maven && \
    mvn -q clean install && \
    mvn -q test -Pinit-slapd && \
    mvn -q test -Pstart-slapd && \
    apt-get remove maven openjdk-8-jdk -qq > /dev/null && \
    apt-get autoremove -qq > /dev/null && \
    rm -rf /var/lib/apt/lists/*

# Installing Java 7
RUN apt-get update -qq > /dev/null && \
    apt-get install software-properties-common -qq > /dev/null && \
    add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update -qq > /dev/null && \
    apt-get install openjdk-7-jdk -qq > /dev/null && \
    apt-get remove software-properties-common -qq > /dev/null && \
    apt-get autoremove -qq > /dev/null && \
    rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64 \
    PATH=$PATH:$JAVA_HOME/bin
    

# Glassfish 4
EXPOSE 4848 8080 8181
WORKDIR /
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh && \
    apt-get update -qq > /dev/null && \
    apt-get install unzip wget -qq > /dev/null && \
    wget -q http://download.oracle.com/glassfish/4.1.2/release/glassfish-4.1.2.zip && \
    unzip -q -o glassfish-4.1.2.zip && \
    rm glassfish-4.1.2.zip && \
    apt-get remove unzip wget -qq > /dev/null && \
    apt-get autoremove -qq > /dev/null && \
    rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["/entrypoint.sh"]
CMD ["asadmin", "start-domain", "-v"]
ENV GLASSFISH_PASSWORD=password \
    PATH=$PATH:/glassfish4/bin

# ADF Essentials
WORKDIR /glassfish4/glassfish/domains/domain1/lib/
COPY glassfish4/glassfish/domains/domain1/lib/adf-essentials.zip .
RUN apt-get update -qq > /dev/null && \
    apt-get install unzip -qq > /dev/null && \
    unzip -q adf-essentials.zip && \
    rm adf-essentials.zip && \
    apt-get remove unzip -qq > /dev/null && \
    apt-get autoremove -qq > /dev/null && \
    rm -rf /var/lib/apt/lists/*

# Archemy
WORKDIR /
COPY archemy.ear .
COPY glassfish4/glassfish/domains/domain1/lib/archemy-security-1.0-SNAPSHOT-jar-with-dependencies.jar /opt/glassfish4/glassfish/domains/domain1/lib/archemy-security-1.0-SNAPSHOT-jar-with-dependencies.jar
COPY glassfish4/glassfish/lib/mysql-connector-java-5.1.40-bin.jar /opt/glassfish4/glassfish/lib/mysql-connector-java-5.1.40-bin.jar