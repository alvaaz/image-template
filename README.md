## Inicializar

```
docker build -t ${image-name} .
```

```
docker run -it -p 5000:5000 -v $PWD:/usr/src/app ${image-name}
```
