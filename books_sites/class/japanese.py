#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://www.sejuku.net/blog/28182

class Japanese():
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
 
    def print_info(self):
        print("""
        名前：{}
        性別：{}
        年齢：{}
        """.format(self.name, self.sex, self.age))
 
    def say(self, word):
        print("{}：「{}」".format(self.name, word))
        
    def reply(self, word):
        if word == "How are you?":
            print("{}：「{}」".format(self.name, "I'm fine, thank you!"))
        else:
            print("{}：「{}」".format(self.name, "..."))
            
taro = Japanese("taro", "man", "31")
taro.print_info()
taro.say("こんにちは！みなさん。")
taro.reply("How are you?")
taro.reply("What's up?")