# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY front/package*.json ./
RUN npm install
COPY ./front .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/
RUN mkdir -p /etc/nginx/ssl
COPY ./ssl/bump.crt /etc/nginx/ssl/transcendance.com.crt
COPY ./ssl/bump.key /etc/nginx/ssl/transcendance.com.key
RUN rm /etc/nginx/conf.d/default.conf
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]

