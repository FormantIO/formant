FROM ros:melodic-robot

RUN apt-key adv --fetch-keys https://keys.formant.io/formant.pub.gpg
RUN echo "deb https://repo.formant.io/formant/debian bionic main" | tee -a /etc/apt/sources.list > /dev/null

RUN echo formant-agent formant-agent/service_enable boolean "false" | debconf-set-selections

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y formant-agent --no-install-recommends

RUN apt update && apt install -y \
    libvips-dev \
    vim \
    tmux \
    git

RUN mkdir -p /catkin_ws

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
