FROM node:lts-alpine as build-stage

WORKDIR /app
COPY . .
WORKDIR front
RUN npm install 
RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/front/dist /usr/share/nginx/html
copy nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
