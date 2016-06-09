# !! IMPORTANT: ARCHLINUX BASE IMAGE IS OBSOLETE

FROM hysoftware/baseimage

MAINTAINER Hiroaki Yamamoto

ENV host 0.0.0.0
ENV port 80
ENV node_mode production
ENV mode production

RUN useradd -m hysoft
USER hysoft

WORKDIR /home/hysoft
RUN git clone https://github.com/hiroaki-yamamoto/hysoftware.net webapp

USER root
WORKDIR /home/hysoft/webapp
RUN pip install -r requirements.txt
RUN npm install

USER hysoft

ENTRYPOINT ["python"]
CMD ["run_app.py", "runserver"]
EXPOSE 80
