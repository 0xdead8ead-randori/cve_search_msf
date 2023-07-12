# Dockerfile for Metasploit

FROM debian:bookworm

# Version Pinning - Can also be supplied by --build-arg in docker command
# this version can be a (tag / commit / feature branch) of metasploit
# Release tags found here - https://github.com/rapid7/metasploit-framework/tags
ARG MSF_VERSION=6.3.24
ENV MSF_VERSION=$MSF_VERSION

# Pymetasploit3 Library (Pinned Commit)- https://github.com/DanMcInerney/pymetasploit3/commits/master
ARG PYMETASPLOIT3_VERSION=9776da55b0abacfa843a32204f3972ec7d9b3de7
ENV PYMETASPLOIT3_VERSION=$PYMETASPLOIT3_VERSION

# deps - https://docs.metasploit.com/docs/development/get-started/setting-up-a-metasploit-development-environment.html#linux
# additionally the following deps are also necessary - curl, libssl-dev, ruby-full
RUN apt update && apt install -y git autoconf build-essential libpcap-dev libpq-dev zlib1g-dev libsqlite3-dev python3-pip

# Install pymetasploit3 library via pip - https://github.com/DanMcInerney/pymetasploit3/commits/master
RUN pip install git+https://github.com/DanMcInerney/pymetasploit3.git@$PYMETASPLOIT3_VERSION --break-system-packages

# Create Metasploit Directory
RUN mkdir -p /app/metasploit-framework
WORKDIR /app/metasploit-framework/

# Set Home Directory
ENV HOME=/home/user

#Clone In Metasploit Code
RUN git clone --depth 1 -b $MSF_VERSION https://github.com/rapid7/metasploit-framework.git /app/metasploit-framework

# Install ruby from apt and all the gems
RUN apt install -y ruby-full
RUN gem install bundler && bundle install
EXPOSE 55553

