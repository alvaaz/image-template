FROM python:latest
RUN pip install Pillow
RUN pip install Flask
RUN pip install zipfile
WORKDIR /usr/src/app
COPY . ./
CMD ["python3", "./main.py"]
# RUN pip install -r requirements.txt
# ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "main:app", "--reload"]
