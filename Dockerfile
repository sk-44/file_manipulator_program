FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y vim nano sudo python3
ENV TZ=Asia/Tokyo

RUN mkdir file_mp
WORKDIR /file_mp