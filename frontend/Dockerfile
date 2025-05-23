FROM node:18-alpine

WORKDIR /app

# First, only copy package files and run npm install
# It allows to rebuild image faster if source code changed
# We do not need to reinstall all packages every time
COPY frontend/package*.json ./

RUN npm install

# Then, copy the rest of source code
COPY frontend ./

EXPOSE 3000

CMD ["npm", "start"]