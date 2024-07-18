from database.id_generator import id_generator

cron = {
    "cron_id": id_generator(1),
    "time": "00 6 * * *",
    "type": "",
    "message": "",
    "channel_id": "",
    "onetime": False,
    "play": True
}
