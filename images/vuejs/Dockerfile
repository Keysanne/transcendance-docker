# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY front/package*.json ./
RUN npm install
COPY ./front .
RUN npm run build

# production stage
FROM debian:bookworm as production-stage
RUN apt update && apt upgrade  -y
RUN apt-get install nginx -y
RUN apt-get install libmaxminddb-dev -y
RUN apt-get install -y bison
RUN apt-get install -y libperl-dev          
RUN apt-get install -y build-essential
RUN apt-get install -y ca-certificates
RUN apt-get install -y curl
RUN apt-get install -y dh-autoreconf
RUN apt-get install -y doxygen
RUN apt-get install -y flex
RUN apt-get install -y gawk
RUN apt-get install -y git
RUN apt-get install -y make
RUN apt-get install -y iputils-ping
RUN apt-get install -y libcurl4-gnutls-dev
RUN apt-get install -y libexpat1-dev
RUN apt-get install -y libgeoip-dev
RUN apt-get install -y liblmdb-dev
RUN apt-get install -y libpcre3-dev
RUN apt-get install -y libssl-dev 
RUN apt-get install -y libtool
RUN apt-get install -y libxml2
RUN apt-get install -y libxml2-dev
RUN apt-get install -y libyajl-dev
RUN apt-get install -y locales
RUN apt-get install -y lua5.3-dev
RUN apt-get install -y pkg-config
RUN apt-get install -y wget
RUN apt-get install -y yajl-tools
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y libxslt-dev
RUN apt-get install -y libgd-dev
RUN apt-get install -y systemctl

WORKDIR /opt
RUN git clone https://github.com/SpiderLabs/ModSecurity
WORKDIR /opt/ModSecurity
RUN git submodule init 
RUN git submodule update
RUN ./build.sh
RUN ./configure
RUN make -j16
RUN make install
#COPY ./modSecurity/usr/local/modsecurity /usr/local/modsecurity

WORKDIR /opt
RUN git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git
RUN wget http://nginx.org/download/nginx-1.22.1.tar.gz
RUN tar -xvzmf nginx-1.22.1.tar.gz
WORKDIR /opt/nginx-1.22.1
RUN ./configure --add-dynamic-module=../ModSecurity-nginx --with-cc-opt='-g -O2 -ffile-prefix-map=/build/nginx-AoTv4W/nginx-1.22.1=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=stderr --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-compat --with-debug --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --with-http_addition_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_secure_link_module --with-http_sub_module --with-mail_ssl_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-stream_realip_module --with-http_geoip_module=dynamic --with-http_image_filter_module=dynamic --with-http_perl_module=dynamic --with-http_xslt_module=dynamic --with-mail=dynamic --with-stream=dynamic --with-stream_geoip_module=dynamic
RUN make modules
RUN mkdir /etc/nginx/modules
RUN cp objs/ngx_http_modsecurity_module.so /etc/nginx/modules

WORKDIR /
RUN rm -rf /etc/nginx/nginx.conf
COPY ./modSecurity/etc/nginx/nginx.conf /etc/nginx/nginx.conf
#COPY ./modSecurity/usr/local/modsecurity-crs /usr/local/modsecurity-crs
RUN git clone https://github.com/coreruleset/coreruleset /usr/local/modsecurity-crs
RUN mv /usr/local/modsecurity-crs/crs-setup.conf.example /usr/local/modsecurity-crs/crs-setup.conf
RUN mv /usr/local/modsecurity-crs/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example /usr/local/modsecurity-crs/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf
COPY ./modSecurity/etc/nginx/modsec /etc/nginx/modsec
#RUN mv /etc/nginx/modsec/main.conf-ex /etc/nginx/modsec/main.conf
#RUN mv /etc/nginx/modsec/modsecurity.conf-ex /etc/nginx/modsec/modsecurity.conf
#RUN echo "Include /usr/local/modsecurity-crs/crs-setup.conf" >> main.conf
RUN rm -rf /etc/nginx/sites-available/default
COPY ./modSecurity/etc/nginx/sites-available/default /etc/nginx/sites-available/default
RUN cp /opt/nginx-1.22.1/objs/*.so /etc/nginx/modules/
COPY ./modSecurity/etc/nginx/modules-enabled/test.conf /etc/nginx/modules-enabled/test.conf

COPY --from=build-stage /app/dist /usr/share/nginx/html
RUN mkdir -p /etc/nginx/ssl
COPY ./ssl/bump.crt /etc/nginx/ssl/transcendance.com.crt
COPY ./ssl/bump.key /etc/nginx/ssl/transcendance.com.key
EXPOSE 8080
RUN systemctl restart nginx

CMD ["nginx", "-g", "daemon off;"]

#COPY ./script.sh ./script.sh
#RUN chmod 777 script.sh
#ENTRYPOINT ./script.sh
# sudo docker system prune --volumes --all
# cat /var/log/journal/nginx.service.log
# ngx_http_geoip_module.so	 ngx_http_perl_module.so	 ngx_stream_geoip_module.so
# ngx_http_image_filter_module.so  ngx_http_xslt_filter_module.so  ngx_stream_module.so
# ngx_http_modsecurity_module.so	 ngx_mail_module.so

