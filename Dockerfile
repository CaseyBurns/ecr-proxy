FROM nginx

EXPOSE 443

COPY ./templates /etc/nginx/templates
