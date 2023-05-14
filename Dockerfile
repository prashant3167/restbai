FROM python:3.9.10
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY src/ /app
WORKDIR /app
RUN pip3 install flask-cors
RUN pip3 install cloudinary
RUN mkdir /static_files
RUN mkdir /app/static
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
