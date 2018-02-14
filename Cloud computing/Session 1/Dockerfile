FROM ubuntu
RUN apt-get update
RUN apt-get install -y curl build-essential zlibc zlib1g-dev ruby ruby-dev openssl libxslt-dev libxml2-dev libssl-dev libreadline6 libreadline6-dev libyaml-dev libsqlite3-dev sqlite3 ruby-full
RUN curl https://s3.amazonaws.com/bosh-init-artifacts/bosh-init-0.0.103-linux-amd64 > bosh-init && mv bosh-init /usr/local/bin/bosh-init chmod +x /usr/local/bin/bosh-init
RUN curl https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-2.0.48-linux-amd64 > bosh && mv bosh /usr/local/bin/bosh && chmod +x /usr/local/bin/bosh
# try with bosh-init -v and bosh -v (should be 2.0...)