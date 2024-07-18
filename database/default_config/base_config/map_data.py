map_data = {
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
}
