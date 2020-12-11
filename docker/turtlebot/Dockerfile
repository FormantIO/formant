FROM ros:melodic-robot-bionic
COPY scripts/install.sh /scripts/install.sh
RUN scripts/install.sh
COPY scripts/run.sh /scripts/run.sh
CMD ["scripts/run.sh"]