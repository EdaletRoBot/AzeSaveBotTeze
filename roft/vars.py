# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by Shin-Yue, < https://github.com/Shin-yue >.
# and is released under the "GNU v3.0 License Agreement
#
# All rights reserved.
# Vars of the bot

import os


class RoftConfiguration:

    __roft_version__ = '1.5.8'

    ApiID = os.environ.get('API_ID', 123456)
    ApiHASH = os.environ.get('API_HASH', "123567") 

    TelegramBot = os.environ.get('TELEGRAM', "5426644613:AAG_BoErvt2wVV73lYjVkEllfREOAdA0EJk")
    SpecialUsers = int(os.environ.get('CREATOR_ID', "5540993505"))

    MongoDatabaseURI = os.environ.get('DATABASE_URI', "mongodb+srv://XataVarEdalet:XataVarEdalet@edalet.qj5i9cs.mongodb.net/?retryWrites=true&w=majority")
    LogGroupChatID = int(os.environ.get('LOG_CHAT_ID', "-1001890451886"))

    MusicDurationLimit = int(os.getenv("MusicDurationLimit", "3600"))
    CommandPrefixesBOT = list(os.getenv("CommandPrefixesBOT", '. / !').split())

    GeniusLyricsAPI = os.getenv('GeniusLyricsAPI', '1QNnajK5oSh2Ut_bJVXbKzwFV_BqyZxUssSpWdcjpVHr5qRcql0BMx3pMSVWSFoj')
    UserMustJoinChannel = os.getenv('UserMustJoinChannel', 'edaletproject')


vars = RoftConfiguration() 
