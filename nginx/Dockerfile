FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

COPY unimagdalena_edu_co.cert /etc/nginx/
COPY wildcard_unimagdalena_edu_co.key /etc/nginx/