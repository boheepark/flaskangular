FROM python:3.6.1

# set working directory
RUN mkdir -p /usr/src/asdf
WORKDIR /usr/src/asdf

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/asdf/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# setup node
# Change to the Node.js version that matches the install script below
ENV NODE_VERSION 8.9.1

# Build and install Node.js, upgrade NPM to the latest version and install JPSM
RUN \
  cd /tmp && \
  wget http://nodejs.org/dist/v8.9.1/node-v8.9.1.tar.gz && \
  tar xvzf node-v*.tar.gz && \
  rm -f node-v*.tar.gz && \
  cd node-v* && \
  ./configure && \
  CXX="g++ -Wno-unused-local-typedefs" make && \
  CXX="g++ -Wno-unused-local-typedefs" make install && \
  cd /tmp && \
  rm -rf /tmp/node-v* && \
  npm install -g npm && \
  npm install -g jspm && \
  printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc && \
  cd

# Used by Beyond build scripts
ENV NODE_BIN /usr/local/bin/node
ENV NPM_BIN /usr/local/bin/npm
ENV JSPM_BIN /usr/local/bin/jspm

# setup npm
RUN npm install

# run server
CMD python manage.py runserver -h 0.0.0.0
