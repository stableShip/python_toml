# coding=utf-8
__author__ = 'JIE'



import toml

with open(u"./configs/st_build_type.toml") as build_type:
    config = toml.loads(build_type.read())
    print config["4"].get("name")