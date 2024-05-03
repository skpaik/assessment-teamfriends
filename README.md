# Team Friends

### Setup the project
- Clone the project
- Open code in your favourite editor
- Open Terminal on `_bash` folder of the project and run
```shell
./install.sh
```


### Run Redis
- Keep running the docker in your local machine
- Open Terminal on `_bash` folder of the project and run
  ```shell
  ./docker.sh
  ```
- This command will install and run redis in docker for your local computer


### Run the project
- Open Terminal on `root` folder of the project and run
```shell
./run.sh
```

### Migrate the database
- Open Terminal on `_bash` folder of the project and run
```shell
./migrate_db.sh
```

### Add sample data
- Open Terminal on `_bash` folder of the project and run
```shell
./seed.sh
```

### Run celery schedular
- Open Terminal on `_bash` folder of the project and run
```shell
./schedular.sh
```