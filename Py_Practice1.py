def solution(players, callings):
    RankDic = {}
    PlayerDic = {}

    for idx, player in enumerate(players):          #플레이어의 사전과 플레이어 순서의 사전을 만들어주는 모습
        RankDic[idx + 1] = player                   #플레이어의 순위를 키로 이름을 벨류값으로 하는 사전형
        PlayerDic[player] = idx + 1                 #플레이어의 이름을 키로, 순위를 벨류값으로 하는 사전형

    for cur_player in callings:                              
        cur_rank = PlayerDic[cur_player]            #플레이어의 이름을 키로 사전에서 순위 검색 (이름을 검색해서 숫자(순위를 찾음))
        prev_rank = cur_rank - 1                    #역전당한 플레이어의 순위를 prev_rank로 설정
        prev_player = RankDic[prev_rank]            #prev_rank를 키 값으로 역전당한 플레이어 검색

        RankDic[prev_rank],RankDic[cur_rank] = RankDic[cur_rank],RankDic[prev_rank]                     #스왑해주기 (순위 바꿔주기)
        PlayerDic[prev_player],PlayerDic[cur_player] = PlayerDic[cur_player],PlayerDic[prev_player]     #스왑해주기 (플레이어의 순위바꿔주기)
        
    return list(RankDic.values())                   #최종 순위의 벨류값을 리스트로 아웃풋

    # map해주는 방법에 대해서 알고 있어야함
    # 내가 풀었던 list.index() 의 방법은 작은 경우의 수에는 몰라도
    # 이러한 문제같은 경우의 큰 값이 주어지는 경우 힘듦.


print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))

# 또 다른 예시 풀이

def solution(players, callings):
    player_indices = {player: index for index, player in enumerate(players)}            # 오 한줄짜기 멋있다.

    for j in callings:                                                                  # 기본적으로 같은 내용이지만 플레이어 순위의 사전형을 따로 만들지 않고 주어져있는 players를 사용
        current_index = player_indices[j]
        desired_index = current_index - 1
        if current_index > 0 and players[desired_index] != j:
            players[current_index], players[desired_index] = players[desired_index], players[current_index]
            player_indices[players[current_index]] = current_index
            player_indices[players[desired_index]] = desired_index                      #깔끔해보인다

    return players
