from database.id_generator import id_generator

main = {
    "id":  id_generator(1),
    "name": "",
    "guild_id": "",
    "pass": id_generator(4),
    "active": True,
    "ban": False,
    "ban_reason": "",
    "market": "",
    "preferred_language": "",
    "global_world": "",
    "global_guild": "",
}
