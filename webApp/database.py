#!/usr/bin/python3
import pymysql


class Database:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> Cursor:
        self.connect = pymysql.connect(**self.configuration)
        self.cursor = self.connect.cursor()
        return self.cursor


    def __exit__(self):
        pass
