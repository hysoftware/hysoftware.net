# !! IMPORTANT: ARCHLINUX BASE IMAGE IS OBSOLETE

FROM base/archlinux

MAINTAINER Hiroaki Yamamoto
RUN pacman -Sy --noconfirm archlinux-keyring
RUN pacman -Su --noconfirm python git python-pip libffi \
  openssl ca-certificates-utils

RUN useradd -m hysoft
USER hysoft

WORKDIR /home/hysoft
RUN git clone https://github.com/hiroaki-yamamoto/hysoftware.net webapp

USER root
WORKDIR /home/hysoft/webapp
RUN pip install -r requirements.txt
USER hysoft

ENV host 0.0.0.0
ENV port 80
ENTRYPOINT ["python"]
CMD ["run_app.py", "runserver"]
EXPOSE 80
