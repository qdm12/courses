FROM ubuntu
RUN apt-get update
RUN apt-get install -y git curl unzip build-essential ruby ruby-dev openssl zlibc zlib1g-dev libxslt-dev libxml2-dev libssl-dev libreadline6 libreadline6-dev libyaml-dev libsqlite3-dev sqlite3
RUN curl "https://releases.hashicorp.com/terraform/0.11.3/terraform_0.11.3_linux_amd64.zip" --output terraform.zip && unzip terraform.zip && rm terraform.zip && mv terraform /usr/local/bin/terraform && chmod +x /usr/local/bin/terraform
RUN curl "https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-2.0.48-linux-amd64" --output /usr/local/bin/bosh && chmod +x /usr/local/bin/bosh
RUN curl -L "https://github.com/cloudfoundry/bosh-bootloader/releases/download/v6.1.1/bbl-v6.1.1_linux_x86-64" --output /usr/local/bin/bbl && chmod +x /usr/local/bin/bbl
RUN curl -L "https://packages.cloudfoundry.org/stable?release=linux64-binary&source=github" --output cf.tgz && tar -xvzf cf.tgz && mv cf /usr/local/bin && rm LICENSE NOTICE cf.tgz
RUN mkdir /bbl
WORKDIR /bbl