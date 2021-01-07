from Bot.version_number_updater import version_number_updater

version_updater = version_number_updater()
summoner_version_num = version_updater.get_version_number()

summoner_spells = {
    'Heal': f'//opgg-static.akamaized.net/images/lol/spell/SummonerHeal.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Ghost': f'//opgg-static.akamaized.net/images/lol/spell/SummonerHaste.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Barrier': f'//opgg-static.akamaized.net/images/lol/spell/SummonerBarrier.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Exhaust': f'//opgg-static.akamaized.net/images/lol/spell/SummonerExhaust.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Flash': f'//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Teleport': f'//opgg-static.akamaized.net/images/lol/spell/SummonerTeleport.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Smite': f'//opgg-static.akamaized.net/images/lol/spell/SummonerSmite.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Cleanse': f'//opgg-static.akamaized.net/images/lol/spell/SummonerBoost.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Ignite': f'//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_42&v={summoner_version_num}'
}

summoner_spells_emoji = {
    '<:heal:795017461325365288>': f'//opgg-static.akamaized.net/images/lol/spell/SummonerHeal.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    '<:ghost_:795017461283160074>': f'//opgg-static.akamaized.net/images/lol/spell/SummonerHaste.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    '<:barrier:795017459346178110>': f'//opgg-static.akamaized.net/images/lol/spell/SummonerBarrier.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    '<:exhaust:795017459668090891>': f'//opgg-static.akamaized.net/images/lol/spell/SummonerExhaust.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    '<:flash:795017461106999316>': f'//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    '<:teleport:795017461451587594>': f'//opgg-static.akamaized.net/images/lol/spell/SummonerTeleport.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    '<:smite:795017461346861056>': f'//opgg-static.akamaized.net/images/lol/spell/SummonerSmite.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    '<:cleanse:795017459740311572>': f'//opgg-static.akamaized.net/images/lol/spell/SummonerBoost.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    '<:ignite:795017461275295817>': f'//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_42&v={summoner_version_num}'
}

summoner_spells_names = {
    'Heal': f'//opgg-static.akamaized.net/images/lol/spell/SummonerHeal.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Ghost': f'//opgg-static.akamaized.net/images/lol/spell/SummonerHaste.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Barrier': f'//opgg-static.akamaized.net/images/lol/spell/SummonerBarrier.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Exhaust': f'//opgg-static.akamaized.net/images/lol/spell/SummonerExhaust.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Flash': f'//opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Teleport': f'//opgg-static.akamaized.net/images/lol/spell/SummonerTeleport.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Smite': f'//opgg-static.akamaized.net/images/lol/spell/SummonerSmite.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Cleanse': f'//opgg-static.akamaized.net/images/lol/spell/SummonerBoost.png?image=c_scale,q_auto,w_42&v={summoner_version_num}',
    'Ignite': f'//opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=c_scale,q_auto,w_42&v={summoner_version_num}'
}
