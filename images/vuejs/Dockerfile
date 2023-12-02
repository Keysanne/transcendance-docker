FROM node:lts-alpine as build-stage
WORKDIR /app
COPY ./front/package*.json ./
RUN npm install
COPY . .
RUN npm run build ./front

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/front/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
