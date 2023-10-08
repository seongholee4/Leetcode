
all_players = {
    "사뮈엘 에토" : ["카타르 SC", "코니아스포르", "프라포트 TAV 안탈랴스포르", "삼프도리아", "에버턴", "첼시", "안지 마하치칼라", "인테르", "FC 바르셀로나", "RCD 마요르카", "레알 마드리드", "RCD 에스파뇰", "CD 레가네스", "카스티야"],
    "앙헬 디마리아" : ["유벤투스", "파리 생제르맹", "맨체스터 유나이티드", "레알 마드리드", "SL 벤피카", "로사리오 센트랄"],
    "TEST" : ["유벤투스", "파리 생제르맹"],
    "곤잘레스" : ["카타르 SC"]

}

for player in all_players:
    player_team = all_players[player]
    print("-----", player, "-----")
    for other_player in all_players:
        if player != other_player:
            other_player_team = all_players[other_player]
            for each_team in player_team:
                if each_team in other_player_team:
                    print(other_player, ": ", each_team)
            # find common teams between a player with other players.
            '''
            에토
            '''
        