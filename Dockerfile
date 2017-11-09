FROM python:2.7.12

# set working directory
RUN mkdir -p /usr/src/asdf
WORKDIR /usr/src/asdf

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/asdf/requirements.txt

# install requirements
RUN pip install -r requirements.txt
RUN npm install
RUN . setup.sh
RUN bower install

# run server
CMD python manage.py runserver -h 0.0.0.0
