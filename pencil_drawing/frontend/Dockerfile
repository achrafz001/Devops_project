FROM python:3.8
WORKDIR "/code"
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY . /code
EXPOSE 8501
ENTRYPOINT ["streamlit", "run" ]
CMD ["models.py"]
