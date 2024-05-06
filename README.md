# Team Friends

### Set up the project
- Clone the project
- Open code in your favourite editor
- Open Terminal on `_bash` folder of the project and run
```shell
./install.sh
```


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

### Run a schedular
- Open Terminal on `_bash` folder of the project and run
```shell
./schedular.sh
```
- You can change cron schedule at `app/settings.py` line `130 to 135`
- Example
- `*/1 * * * *` Run schedule every minute
- `0 8 * * *` Run schedule every day 8 am
