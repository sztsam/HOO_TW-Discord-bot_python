import uuid

db_sample = {
    "guild": {
        "id":  str(uuid.uuid1())[:-13].replace("-", ""),
        "name": "",
        "guild_id": "",
        "pass": str(uuid.uuid4())[:-13].replace("-", ""),
        "active": True,
        "ban": False,
        "ban_reason": "",
        "market": "",
        "preferred_language": "",
        "global_world": "",
        "global_guild": "",
        "config": {
                "swear_words_punishment": {
                    "enabled": True,
                    "use_global_preset": True,
                    "words": [],
                    "ai_bot_chat": {
                        "use": False,
                        "percentage": 50,
                        "black_list": {},
                        "white_list": {},
                        "force_list": {}
                    },
                    "react_emojis": {
                        "use": True,
                        "percentage": 20,
                        "emojis": [],
                        "black_list": {},
                        "white_list": {},
                        "force_list": {}
                    },
                    "black_list": {},
                    "white_list": {}
                },
            "live_ennoblements": {
                    "use_default": True,
                    "guest_mode": False,
                    "village_points": True,
                    "player_points": False,
                    "tribe_points": False,
                    "old_owner": True,
                    "date_time": True,
                    "relative_time": True
                    },
            "ai_bot_chat_channels": [],
            "coord_info": {
                    "active": True,
                    "channels": {}
                    },
            "roles": [],
            "cronjobs": []
        },
    },
    "base_config": {
        "roles": {
            "role_id": str(uuid.uuid1())[:-13].replace("-", ""),
            "channel_id": "",
            "message_id": "",
            "type": "",
            "roles": []
        },
        "role_in_roles": {
            "role_name": "",
            "emoji_id": "",
            "role_id": ""
        },
        "role_type": [
            "normal",
            "unique"
        ],
        "cron": {
            "cron_id": str(uuid.uuid1())[:-13].replace("-", ""),
            "time": "00 6 * * *",
            "type": "",
            "message": "",
            "channel_id": "",
            "onetime": False,
            "play": True
        },
        "cron_type": {
            "basic": [
                "update_config",
                "update_cached_data",
                "update_map_data",
                "update_daily_stats",
                "update_live_servers",
                "ennoblements",
                "speed_table"
            ],
            "guild": [
                "map",
                "message",
                "stat"
            ],
            "control": [
                "start",
                "stop",
                "delete",
                "modify",
                "create"
            ]
        },
        "map_data": {
            "village": {
                "type": "gz",
                "data": ["id", "name", "x", "y", "player", "points", "rank"]
            },
            "player": {
                "type": "gz",
                "data": ["id", "name", "ally", "villages", "points", "rank"]
            },
            "ally": {
                "type": "gz",
                "data": ["id", "name", "tag", "members", "villages", "points", "all_points", "rank"]
            },
            "conquer": {
                "type": "gz",
                "data": ["village_id", "unix_timestamp", "new_owner", "old_owner"]
            },
            "kill_att": {
                "type": "txt",
                "data": ["rank", "id", "kills"]
            },
            "kill_def": {
                "type": "txt",
                "data": ["rank", "id", "kills"]
            },
            "kill_sup": {
                "type": "txt",
                "data": ["rank", "id", "kills"]
            },
            "kill_all": {
                "type": "txt",
                "data": ["rank", "id", "kills"]
            },
            "kill_att_tribe": {
                "type": "txt",
                "data": ["rank", "id", "kills"]
            },
            "kill_def_tribe": {
                "type": "txt",
                "data": ["rank", "id", "kills"]
            },
            "kill_all_tribe": {
                "type": "txt",
                "data": ["rank", "id", "kills"]
            }
        },
        "map_pic_types": [
            "players_points",
            "players_oda",
            "players_odd",
            "tribes_points",
            "tribes_oda",
            "tribes_odd",
            "conquers_points"
        ],
        "chart_tribe_stats": {
            "scope": [
                "loot_res + scavenge",
                "loot_res",
                "scavenge",
                "conquer",
                "kill_att",
                "kill_def",
                "kill_sup",
                "kill_all",
                "rank-villages",
                "rank-points",
                "rank-kill_all",
                "points-villages",
                "villages-kill_all",
                "rank",
                "points",
                "villages"
            ],
            "size": [5, 10, 15, 20, 25],
            "type": ["bar", "line", "pie", "violin"],
            "style": ["individual", "stacked", "combined"],
            "color": ["transparent", "black", "slategray", "white", "blue", "indigo", "teal", "darkgreen", "darkred"]
        },
        "translations": {
            "map_pic": {
                "en": {
                    "players_points": "Players points",
                    "players_oda": "Players ODA",
                    "players_odd": "Players ODD",
                    "tribes_points": "Tribes points",
                    "tribes_oda": "Tribes ODA",
                    "tribes_odd": "Tribes ODD",
                    "conquers_points": "Conquers"
                },
                "hu": {
                    "players_points": "Játékos pontok",
                    "players_oda": "Játékos LET",
                    "players_odd": "Játékos LEV",
                    "tribes_points": "Klán pontok",
                    "tribes_oda": "Klán LET",
                    "tribes_odd": "Klán LEV",
                    "conquers_points": "Foglalások"
                }
            },
            "chart": {
                "en": {
                    "tribe_scope": {
                        "daily": {
                            "loot_res + scavenge": "farm + scavenge",
                            "loot_res": "farm",
                            "scavenge": "scavenge",
                            "conquer": "conquer",
                            "kill_att": "kill att",
                            "kill_def": "kill def",
                            "kill_sup": "kill sup",
                            "kill_all": "kill all"
                        },
                        "monthly": {
                            "rank-villages": "Rank - Villages",
                            "rank-points": "Rank - Points",
                            "rank-kill_all": "Rank - OD",
                            "points-villages": "Points - Villages",
                            "villages-kill_all": "Villages - OD",
                            "rank": "Rank",
                            "points": "Points",
                            "villages": "Villages",
                            "kill_att": "ODA",
                            "kill_def": "ODD",
                            "kill_sup": "ODS",
                            "kill_all": "OD"
                        },
                        "od": {
                            "kill_att": "kill att",
                            "kill_def": "kill def",
                            "kill_sup": "kill sup",
                            "kill_all": "kill all"
                        },
                        "conquer": "conquer"
                    },
                    "type": {
                        "bar": "bar",
                        "line": "line",
                        "pie": "pie",
                        "violin": "violin"
                    },
                    "style": {
                        "individual": "individual",
                        "stacked": "stacked",
                        "combined": "combined"
                    },
                    "color": {
                        "transparent": "transparent",
                        "black": "black",
                        "slategray": "slategray",
                        "white": "white",
                        "blue": "blue",
                        "indigo": "indigo",
                        "teal": "teal",
                        "darkgreen": "darkgreen",
                        "darkred": "darkred"
                    },
                    "error": {
                        "scope_error": "choosing scope is a must!",
                        "server_error": "choosing server is a must!",
                        "type_error": "choosing type is a must!"
                    },
                    "title": {
                        "daily": "Daily",
                        "stat": "statistics",
                        "loot_res + scavenge": "farm + scavenge",
                        "loot_res": "farm",
                        "scavenge": "scavenge",
                        "conquer": "Conquer",
                        "kill_att": "ODA",
                        "kill_def": "ODD",
                        "kill_sup": "ODS",
                        "kill_all": "OD",
                        "rank-villages": "Rank - Villages",
                        "rank-points": "Rank - Points",
                        "rank-kill_all": "Rank - OD",
                        "points-villages": "Points - Villages",
                        "villages-kill_all": "Villages - OD",
                        "rank": "Rank",
                        "points": "Points",
                        "villages": "Villages"
                    },
                    "dataset_label": {
                        "loot_res + scavenge": {
                            "individual": {
                                "a": "farm",
                                "b": "scavenge"
                            },
                            "stacked": {
                                "a": "farm",
                                "b": "scavenge"
                            },
                            "combined": {
                                "sum": "farm + scavenge"
                            }
                        },
                        "loot_res": {
                            "combined": {
                                "sum": "farm"
                            }
                        },
                        "scavenge": {
                            "combined": {
                                "sum": "scavenge"
                            }
                        },
                        "conquer": {
                            "combined": {
                                "sum": "conquer"
                            }
                        },
                        "kill_att": {
                            "combined": {
                                "sum": "ODA"
                            }
                        },
                        "kill_def": {
                            "combined": {
                                "sum": "ODD"
                            }
                        },
                        "kill_sup": {
                            "combined": {
                                "sum": "ODS"
                            }
                        },
                        "kill_all": {
                            "individual": {
                                "a": "ODA",
                                "b": "ODD",
                                "c": "ODS"
                            },
                            "stacked": {
                                "a": "ODA",
                                "b": "ODD",
                                "c": "ODS"
                            },
                            "combined": {
                                "sum": "ODA + ODD + ODS"
                            }
                        },
                        "rank-villages": {
                            "individual": {
                                "a": "Rank",
                                "b": "Villages"
                            },
                            "stacked": {
                                "a": "Rank",
                                "b": "Villages"
                            },
                            "combined": {
                                "sum": "Rank"
                            }
                        },
                        "rank-points": {
                            "individual": {
                                "a": "Rank",
                                "b": "Points"
                            },
                            "stacked": {
                                "a": "Rank",
                                "b": "Points"
                            },
                            "combined": {
                                "sum": "Rank"
                            }
                        },
                        "rank-kill_all": {
                            "individual": {
                                "a": "Rank",
                                "b": "OD"
                            },
                            "stacked": {
                                "a": "Rank",
                                "b": "OD"
                            },
                            "combined": {
                                "sum": "Rank"
                            }
                        },
                        "points-villages": {
                            "individual": {
                                "a": "Points",
                                "b": "Villages"
                            },
                            "stacked": {
                                "a": "Points",
                                "b": "Villages"
                            },
                            "combined": {
                                "sum": "Points"
                            }
                        },
                        "villages-kill_all": {
                            "individual": {
                                "a": "Villages",
                                "b": "OD"
                            },
                            "stacked": {
                                "a": "Villages",
                                "b": "OD"
                            },
                            "combined": {
                                "sum": "Villages"
                            }
                        },
                        "rank": {
                            "combined": {
                                "sum": "Rank"
                            }
                        },
                        "points": {
                            "combined": {
                                "sum": "Points"
                            }
                        },
                        "villages": {
                            "combined": {
                                "sum": "Villages"
                            }
                        }
                    }
                },
                "hu": {
                    "tribe_scope": {
                        "daily": {
                            "loot_res + scavenge": "farm + gyűjtögetés",
                            "loot_res": "farm",
                            "scavenge": "gyűjtögetés",
                            "conquer": "foglalás",
                            "kill_att": "LET",
                            "kill_def": "LEV",
                            "kill_sup": "LES",
                            "kill_all": "LE"
                        },
                        "monthly": {
                            "rank-villages": "Helyezés - Falu",
                            "rank-points": "Helyezés - Pont",
                            "rank-kill_all": "Helyezés - LE",
                            "points-villages": "Pont - Falu",
                            "villages-kill_all": "Falu - LE",
                            "rank": "Helyezés",
                            "points": "Pont",
                            "villages": "Falu",
                            "kill_att": "LET",
                            "kill_def": "LEV",
                            "kill_sup": "LES",
                            "kill_all": "LE"
                        },
                        "od": {
                            "kill_att": "LET",
                            "kill_def": "LEV",
                            "kill_sup": "LES",
                            "kill_all": "LE"
                        },
                        "conquer": "foglalás"
                    },
                    "type": {
                        "bar": "oszlop",
                        "line": "vonal",
                        "pie": "kör",
                        "violin": "eloszlás"
                    },
                    "style": {
                        "individual": "egyéni",
                        "stacked": "halmozott",
                        "combined": "kombinált"
                    },
                    "color": {
                        "transparent": "átlátszó",
                        "black": "fekete",
                        "slategray": "palaszürke",
                        "white": "fehér",
                        "blue": "kék",
                        "indigo": "indigó",
                        "teal": "kékeszöld",
                        "darkgreen": "sötétzöld",
                        "darkred": "sötétpiros"
                    },
                    "error": {
                        "scope_error": "hatókör választása kötelező!",
                        "server_error": "szerver választása kötelező!",
                        "type_error": "típus választása kötelező!"
                    },
                    "title": {
                        "daily": "Napi",
                        "stat": "statisztika",
                        "loot_res + scavenge": "farm + gyűjtögetés",
                        "loot_res": "farm",
                        "scavenge": "gyűjtögetés",
                        "conquer": "foglalás",
                        "kill_att": "LET",
                        "kill_def": "LEV",
                        "kill_sup": "LES",
                        "kill_all": "LE",
                        "rank-villages": "Helyezés - Falu",
                        "rank-points": "Helyezés - Pont",
                        "rank-kill_all": "Helyezés - LE",
                        "points-villages": "Pont - Falu",
                        "villages-kill_all": "Falu - LE",
                        "rank": "Helyezés",
                        "points": "Pont",
                        "villages": "Falu"
                    },
                    "dataset_label": {
                        "loot_res + scavenge": {
                            "individual": {
                                "a": "farm",
                                "b": "gyűjtögetés"
                            },
                            "stacked": {
                                "a": "farm",
                                "b": "gyűjtögetés"
                            },
                            "combined": {
                                "sum": "farm + gyűjtögetés"
                            }
                        },
                        "loot_res": {
                            "combined": {
                                "sum": "farm"
                            }
                        },
                        "scavenge": {
                            "combined": {
                                "sum": "gyűjtögetés"
                            }
                        },
                        "conquer": {
                            "combined": {
                                "sum": "foglalás"
                            }
                        },
                        "kill_att": {
                            "combined": {
                                "sum": "LET"
                            }
                        },
                        "kill_def": {
                            "combined": {
                                "sum": "LEV"
                            }
                        },
                        "kill_sup": {
                            "combined": {
                                "sum": "LES"
                            }
                        },
                        "kill_all": {
                            "individual": {
                                "a": "LET",
                                "b": "LEV",
                                "c": "LES"
                            },
                            "stacked": {
                                "a": "LET",
                                "b": "LEV",
                                "c": "LES"
                            },
                            "combined": {
                                "sum": "LET + LEV + LES"
                            }
                        },
                        "rank-villages": {
                            "individual": {
                                "a": "Helyezés",
                                "b": "Falu"
                            },
                            "stacked": {
                                "a": "Helyezés",
                                "b": "Falu"
                            },
                            "combined": {
                                "sum": "Helyezés"
                            }
                        },
                        "rank-points": {
                            "individual": {
                                "a": "Helyezés",
                                "b": "Pont"
                            },
                            "stacked": {
                                "a": "Helyezés",
                                "b": "Pont"
                            },
                            "combined": {
                                "sum": "Helyezés"
                            }
                        },
                        "rank-kill_all": {
                            "individual": {
                                "a": "Helyezés",
                                "b": "LE"
                            },
                            "stacked": {
                                "a": "Helyezés",
                                "b": "LE"
                            },
                            "combined": {
                                "sum": "Helyezés"
                            }
                        },
                        "points-villages": {
                            "individual": {
                                "a": "Pont",
                                "b": "Falu"
                            },
                            "stacked": {
                                "a": "Pont",
                                "b": "Falu"
                            },
                            "combined": {
                                "sum": "Pont"
                            }
                        },
                        "villages-kill_all": {
                            "individual": {
                                "a": "Falu",
                                "b": "LE"
                            },
                            "stacked": {
                                "a": "Falu",
                                "b": "LE"
                            },
                            "combined": {
                                "sum": "Falu"
                            }
                        },
                        "rank": {
                            "combined": {
                                "sum": "Helyezés"
                            }
                        },
                        "points": {
                            "combined": {
                                "sum": "Pont"
                            }
                        },
                        "villages": {
                            "combined": {
                                "sum": "Falu"
                            }
                        }
                    }
                }
            },
            "info": {
                "en": {
                    "server_error": "Choosing server is a must! No global server set for the discord server",
                    "village_error": "Village is not found!",
                    "ally_error": "Ally is not found!",
                    "player_error": "Player is not found!",
                    "barbarian": "Barbarian village",
                    "link": "Link",
                    "ingame": "Ingame",
                    "guest": "Guest",
                    "twstat": "Twstat",
                    "ally": "Ally",
                    "ally_not_joined": "Not in ally",
                    "rank": "Rank",
                    "points": "Points",
                    "members": "Members",
                    "villages": "Villages",
                    "conquers": "Conquers",
                    "gain": "Gained",
                    "lose": "Lost",
                    "barb": "Barbarian",
                    "self": "Self",
                    "internal": "Internal",
                    "sum": "All",
                    "kills_text": "Opponents defeated",
                    "oda": "ODA",
                    "odd": "ODD",
                    "ods": "ODS",
                    "od": "OD",
                    "kills": "Kills"
                },
                "hu": {
                    "server_error": "Szerver kiválasztása kötelező! Nincs globális szerver beállítva a discord szerverhez",
                    "village_error": "Falu nem található!",
                    "ally_error": "Klán nem található!",
                    "player_error": "Játékos nem található!",
                    "barbarian": "Barbár falu",
                    "link": "Link",
                    "ingame": "Játék",
                    "guest": "Vendég",
                    "twstat": "Twstat",
                    "ally": "Klán",
                    "ally_not_joined": "Klán nélküli",
                    "rank": "Helyezés",
                    "points": "Pont",
                    "members": "Tagok",
                    "villages": "Faluk",
                    "conquers": "Foglalások",
                    "gain": "Foglalt",
                    "lose": "Elvesztett",
                    "barb": "Barbár",
                    "self": "Önhódítás",
                    "internal": "Belső",
                    "sum": "Összesen",
                    "kills_text": "Legyőzött ellenfelek",
                    "oda": "LET",
                    "odd": "LEV",
                    "ods": "LES",
                    "od": "LE",
                    "kills": "Legyőzött"
                }
            },
            "coord_info": {
                "en": {
                    "server_error": "Server error! Market may not be enabled, report an enhancement ticket!",
                    "market_error": "Market not enabled. Please contact bot administrator!",
                    "channel_error": "Channel error. Couldn't get channel id!",
                    "modified": "Coord info settings modified successfully"
                },
                "hu": {
                    "server_error": "Szerver hiba! Lehet a piac nincs engedélyezve, jelentsd ötletként!",
                    "market_error": "Piac nincs engedélyezve. Kérlek vedd fel a kapcsolatot a bot adminnal!",
                    "channel_error": "Csatorna hiba. Nem sikerült lekérni a csatorna azonosítót!",
                    "modified": "Koordináta infó beállítások sikeresen módosítva"
                }
            },
            "speed": {
                "en": {
                    "title": "Upcoming speed rounds",
                    "description": "Market | Number | Start - End | Speed"
                },
                "hu": {
                    "title": "Tervezett speed körök",
                    "description": "Piac | Szám | Kezdet - Befejezés | Sebesség"
                }
            },
            "ennoblements": {
                "en": {
                    "barbarian": "Barbarian",
                    "nobled": "nobled",
                    "old_owner": "Old owner",
                    "channel": "Channel",
                    "play": "Play",
                    "command_message": {
                            "server": "Server error! Market may not be enabled, report an enhancement ticket!",
                            "tribe_error": "No such tribe exists on the server!",
                            "cron_id": "No ennoblement registered with this ID!",
                            "created": "Ennoblement notification created successfully",
                            "deleted": "Ennoblement notification deleted successfully",
                            "all_deleted": "All ennoblement notification deleted successfully",
                            "modified": "Ennoblement notification modified successfully",
                            "channel": "No ennoblement notification registered on this channel!",
                            "guild": "No ennoblement notification registered to this guild!",
                            "list_embed": {
                                "title": "Ennoblement notifications list",
                                "server": "Server",
                                "tribe": "Tribe",
                                "gain": "Gain",
                                "loss": "loss",
                                "self": "Self",
                                "internal": "Internal",
                                "barbarian": "Barbarian",
                                "continent": "Continent",
                                "channel": "Channel",
                                "play": "Play"
                            },
                        "settings_embed": {
                                "title": "Ennoblements settings",
                                "use_default": "Use default settings",
                                "guest_mode": "Guest mode links",
                                "village_points": "Show village points",
                                "player_points": "Show player points",
                                "tribe_points": "Show tribe points",
                                "old_owner": "Show old owner",
                                "date_time": "Show date time",
                                "relative_time": "Show relative time"
                                }
                    }
                },
                "hu": {
                    "barbarian": "Barbár",
                    "nobled": "elfoglalta",
                    "old_owner": "Régi tulajdonos",
                    "channel": "Csatorna",
                    "play": "Megy",
                    "command_message": {
                            "server": "Szerver hiba! Lehet a piac nincs engedélyezve, jelentsd ötletként!",
                            "tribe_error": "Nem létezik ilyen klán a szerveren!",
                            "cron_id": "Nincs foglalásjelző regisztrálva ezzel az ID-vel!",
                            "created": "Foglalásjelző sikeresen létrehozva",
                            "deleted": "Foglalásjelző sikeresen törölve",
                            "all_deleted": "Összes foglalásjelző sikeresen törölve",
                            "modified": "Foglalásjelző sikeresen módosítva",
                            "channel": "Nincs foglalásjelző regisztrálva erre a csatornára!",
                            "guild": "Nincs foglalásjelző regisztrálva erre a szerverre!",
                            "list_embed": {
                                "title": "Foglalásjelző lista",
                                "server": "Szerver",
                                "tribe": "klán",
                                "gain": "Nyereség",
                                "loss": "Veszteség",
                                "self": "Önhódítás",
                                "internal": "Belsőzés",
                                "barbarian": "Barbár",
                                "continent": "Kontinens",
                                "channel": "Csatorna",
                                "play": "Megy"
                            },
                        "settings_embed": {
                                "title": "Foglalásjelző beállítások",
                                "use_default": "Alapbeállítások",
                                "guest_mode": "Vendég mód linkek",
                                "village_points": "Falu pont",
                                "player_points": "Játékos pont",
                                "tribe_points": "Klán pont",
                                "old_owner": "Régi tulajdonos",
                                "date_time": "Dátum és idő",
                                "relative_time": "Relatív idő"
                                }
                    }
                }
            },
            "swear_words": {
                "en": {
                    "modified": "Swear words punishment settings modified successfully",
                    "no_option_given": "No option given to modify settings",
                    "not_all_option_given": "Not all options given to modify settings",
                    "list_embed": {
                        "title": "Swear words settings",
                        "true": "Yes",
                        "false": "No",
                        "basic_settings": "Basic settings",
                        "ai_bot_chat_settings": "AI chatbot settings",
                        "react_emojis_settings": "React emoji settings",
                        "enabled": "enabled",
                        "use_global_preset": "use global preset",
                        "words": "words",
                        "emojis": "emojis",
                        "black_list": "black list",
                        "white_list": "white list",
                        "force_list": "force list",
                        "use": "use",
                        "percentage": "percentage"
                    }
                },
                "hu": {
                    "modified": "Káromkodás büntetés beállítások sikeresen módosítva",
                    "no_option_given": "Nem adtál meg semmilyen módosítási opciót",
                    "not_all_option_given": "Nem adtad meg az összes opciót a beállítások módosításához",
                    "list_embed": {
                        "title": "Káromkodás büntetés beállítások",
                        "true": "igen",
                        "false": "nem",
                        "basic_settings": "Alap beállítások",
                        "ai_bot_chat_settings": "AI chatbot beállítások",
                        "react_emojis_settings": "Reakciós emoji beállítások",
                        "enabled": "engedélyezve",
                        "use_global_preset": "alap beállítások használata",
                        "words": "szavak",
                        "emojis": "emojik",
                        "black_list": "black list",
                        "white_list": "white list",
                        "force_list": "force list",
                        "use": "használ",
                        "percentage": "százalék"
                    }
                }
            },
            "help": {
                "en": {
                    "error": "There was an error submitting your request. Please try again!",
                    "success": "request submitted successfully!",
                    "bug": "Bug",
                    "idea": "Idea"
                },
                "hu": {
                    "error": "Hiba történt a kérés elküldésében. Kérlek, próbáld meg újra!",
                    "success": "kérés sikeresen elküldve!",
                    "bug": "Hiba",
                    "idea": "Ötlet"
                }
            },
            "guild_settings": {
                "en": {
                    "errors": "Errors",
                    "server_error": "Choosing server is a must!",
                    "password_error": "Password must be at least 6 characters!",
                    "market_error": "Market not enabled. Please contact bot administrator!",
                    "translation_error": "Translation not available. Please contact bot administrator!",
                    "no_option_given": "No option given to modify settings",
                    "modified": "Bot guild settings modified successfully",
                    "list_embed": {
                        "title": "Bot basic settings on server",
                        "true": "Yes",
                        "false": "No",
                        "active": "Active",
                        "password": "Password",
                        "ban": "Ban",
                        "ban_reason": "Ban reason",
                        "market": "Market",
                        "preferred_language": "Preferred language",
                        "global_world": "Global world",
                        "global_guild": "Global guild",
                        "coord_info": "Show coord info",
                        "errors": {
                                "password": "Only server owner can see!"
                        }
                    }
                },
                "hu": {
                    "errors": "Hibák",
                    "server_error": "Szerver választása kötelező!",
                    "password_error": "Jelszó hossza legalább 6 karakter!",
                    "market_error": "Piac nincs engedélyezve. Kérlek vedd fel a kapcsolatot a bot adminnal!",
                    "translation_error": "Fordítás nem elérhető. Kérlek vedd fel a kapcsolatot a bot adminnal!",
                    "no_option_given": "Nem adtál meg semmilyen módosítási opciót",
                    "modified": "Bot szerver beállítások sikeresen módosítva",
                    "list_embed": {
                        "title": "Bot alap beállítások a szerveren",
                        "true": "Igen",
                        "false": "Nem",
                        "active": "Aktív",
                        "password": "Jelszó",
                        "ban": "Bann",
                        "ban_reason": "bann oka",
                        "market": "Piac",
                        "preferred_language": "Preferált nyelv",
                        "global_world": "Globális világ",
                        "global_guild": "Globális klán",
                        "coord_info": "Koordináta infó mutatása",
                        "errors": {
                                "password": "Csak szerver tulajdonos láthatja!"
                        }
                    }
                }
            }
        },
        "daily_stat_types": [
            "loot_res",
            "scavenge",
            "loot_vil",
            "kill_att",
            "kill_def",
            "kill_sup",
            "conquer"
        ],
        "ennoblements": {
            "options": {
                "server": "",
                "tribe": "",
                "loss": False,
                "self": False,
                "gain": False,
                "internal": False,
                "barbarian": False,
                "continent": ""
            },
            "settings": {
                "guest_mode": False,
                "village_points": True,
                "player_points": False,
                "tribe_points": False,
                "old_owner": True,
                "date_time": True,
                "relative_time": True
            },
            "colors": {
                "gain": "#4a9422",  # green
                "loss": "#CB0E0E",  # red
                "self": "#B51EBC",  # purple
                "internal": "#111111",  # black
                "barbarian": "#6a6b69"  # grey
            }
        },
        "markets": [
            {
                "market": "hu",
                "link": ".klanhaboru.hu",
                "twstat": "https://hu.twstats.com/",
                "enabled": True,
                "timezone": 1
            },
            {
                "market": "en",
                "link": ".tribalwars.net",
                "twstat": "https://www.twstats.com/",
                "enabled": False,
                "timezone": 0
            },
            {
                "market": "de",
                "link": ".die-staemme.de",
                "twstat": "https://de.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "ch",
                "link": ".staemme.ch",
                "twstat": "https://ch.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "nl",
                "link": ".tribalwars.nl",
                "twstat": "https://nl.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "pl",
                "link": ".plemiona.pl",
                "twstat": "https://pl.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "br",
                "link": ".tribalwars.com.br",
                "twstat": "https://br.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "pt",
                "link": ".tribalwars.com.pt",
                "twstat": "https://pt.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "cs",
                "link": ".divokekmeny.cz",
                "twstat": "https://cz.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "ro",
                "link": ".triburile.ro",
                "twstat": "https://ro.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "ru",
                "link": ".voynaplemyon.com",
                "twstat": "https://ru.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "gr",
                "link": ".fyletikesmaxes.gr",
                "twstat": "https://gr.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "sk",
                "link": ".divoke-kmene.sk",
                "twstat": "https://sk.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "it",
                "link": ".tribals.it",
                "twstat": "https://it.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "tr",
                "link": ".klanlar.org",
                "twstat": "https://tr.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "fr",
                "link": ".guerretribale.fr",
                "twstat": "https://fr.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "es",
                "link": ".guerrastribales.es",
                "twstat": "https://es.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "uk",
                "link": ".tribalwars.co.uk",
                "twstat": "https://www.twstats.co.uk/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "zz",
                "link": ".tribalwars.works",
                "twstat": "https://beta.twstats.com/",
                "enabled": False,
                "timezone": 1
            },
            {
                "market": "us",
                "link": ".tribalwars.us",
                "twstat": "https://us.twstats.com/",
                "enabled": False,
                "timezone": 1
            }
        ],
        "bot_activity": {
            "name": ["HOO", "Klánháború", "ASG Királya", "ASG", "Barcsag", "ARMA", "Védekezés", "PP bank", "Megbeszélés", "Discord", "Asgardia Rejtelmei", "Asgard törvénykönyv", "Vegyetek pp-t gyerekek!"],
            "type": ["Playing", "Streaming", "Listening", "Watching", "Custom", "Competing"],
            "status": ["online", "idle", "dnd"]
        },
        "swear_words": {
            "words": ["fasz"],
            "ai_bot_chat": {
                "use": False,
                "percentage": 10,
                "black_list": {},
                "white_list": {},
                "force_list": {}
            },
            "react_emojis": {
                "use": True,
                "percentage": 40,
                "emojis": ["<:GoodMorning:973864597700374558>", "<:catyikes:973864726201266206>", "<:cooldude:973864712435552276>", "<:cry:973864672266694696>", "<:goblok:973864613772951572>", "<:harold1:973864581388718150>", "<:heat:973864566918352906>", "<:hmm:973864533015801856>", "<:pissoff:973864448743845939>", "👀", "🙄"],
                "black_list": {},
                "white_list": {},
                "force_list": {}
            }
        },
        "dev_channels": {
            "prod_errors": "1088405030631129130",
            "bugs": "1090590497417998418",
            "idea": "1090590531303780422"
        },
        "running_servers": [],
        "running_servers_continents": {},
        "basic_cronjobs": [],
        "prefix": "¤"
    }
}
