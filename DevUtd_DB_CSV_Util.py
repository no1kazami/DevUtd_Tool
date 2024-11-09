import operator
import json
import DevUtd_FireBase_DB
import pandas as pd

# DB에 저장된 파일 읽기
with open('last_FireBaseDB_MatchInfo.json', 'r', encoding='utf-8') as f:
    matchInfo_json = json.load(f)

def UpdateDetailVersion():
    # 저장된 파일 읽기
    fRead = open("last_DevUtd_Version.txt", 'r', encoding='UTF8')
    readData = fRead.read()
    fRead.close()

    # 버전 업
    if isinstance(readData, str):
        fbmVersion = int(readData) + 1
        fWrite = open("last_DevUtd_Version.txt", 'w', encoding='UTF8')
        fWrite.write(str(fbmVersion))
        fWrite.close()

        DevUtd_FireBase_DB.UpdateDetailVer(fbmVersion)

def UpdateTeamInfoData():
    # csv 파일 일기
    colnames = ["TeamName", "TeamLogoURL"]
    df = pd.read_csv('Data/DevUtd_TeamInfo.csv', sep=',', skiprows=[0], engine='python', names=colnames,
                     encoding='utf-16')

    # 행 돌면서 개별 데이터 삽입
    ########################################################
    # csv 의 특정 데이터만 삽입 하고 싶을때 아래 인덱스 기입
    isIndividual = False
    startIndex = 252
    endIndex = 253
    ########################################################
    for i in df.index:
        if isIndividual:
            if startIndex-1 > i:
                continue
            if endIndex-1 < i:
                break
        teamName = df.at[i, 'TeamName']
        teamName = teamName.replace("\n", "")
        teamLogoURL = str(df.at[i, 'TeamLogoURL']).replace("\n", "")
        DevUtd_FireBase_DB.UpdateTeamData(teamName, 'TeamName', teamName)
        DevUtd_FireBase_DB.UpdateTeamData(teamName, 'TeamLogoURL', teamLogoURL)
        print('TeamData Insert : ' + teamName + "[" + teamLogoURL + "]")

def UpdatePlayerInfoData():
    # csv 파일 일기
    colnames = ["PlayerName", "TeamName", "PictureURL", "MvpNum", "TopScorerNum", "TopAssistNum", "TopAttendanceNum", "TopPointNum"]
    df = pd.read_csv('Data/DevUtd_PlayerInfo.csv', sep=',', skiprows=[0], engine='python', names=colnames,
                     encoding='utf-16')

    # 행 돌면서 개별 데이터 삽입
    ########################################################
    # csv 의 특정 데이터만 삽입 하고 싶을때 아래 인덱스 기입
    isIndividual = False
    startIndex = 252
    endIndex = 253
    ########################################################
    for i in df.index:
        if isIndividual:
            if startIndex-1 > i:
                continue
            if endIndex-1 < i:
                break
        playerName = df.at[i, 'PlayerName']
        playerName = playerName.replace("\n", "")
        teamName = str(df.at[i, 'TeamName']).replace("\n", "")
        pictureURL = str(df.at[i, 'PictureURL']).replace("\n", "")
        mvpNum = int(df.at[i, 'MvpNum'])
        topScorerNum = int(df.at[i, 'TopScorerNum'])
        topAssistNum = int(df.at[i, 'TopAssistNum'])
        topAttendanceNum = int(df.at[i, 'TopAttendanceNum'])
        topPointNum = int(df.at[i, 'TopPointNum'])
        DevUtd_FireBase_DB.UpdatePlayerData(playerName, 'PlayerName', playerName)
        DevUtd_FireBase_DB.UpdatePlayerData(playerName, 'TeamName', teamName)
        DevUtd_FireBase_DB.UpdatePlayerData(playerName, 'PictureURL', pictureURL)
        DevUtd_FireBase_DB.UpdatePlayerData(playerName, 'MvpNum', mvpNum)
        DevUtd_FireBase_DB.UpdatePlayerData(playerName, 'TopScorerNum', topScorerNum)
        DevUtd_FireBase_DB.UpdatePlayerData(playerName, 'TopAssistNum', topAssistNum)
        DevUtd_FireBase_DB.UpdatePlayerData(playerName, 'TopAttendanceNum', topAttendanceNum)
        DevUtd_FireBase_DB.UpdatePlayerData(playerName, 'TopPointNum', topPointNum)

        print('PlayerData Insert : ' + playerName + "[" + teamName + "]")

def UpdateMatchInfoData():
    # csv 파일 일기
    colnames = ["MatchDate", "MatchTime", "MatchType", "InfoType", "Comment", "HomeTeamName", "AwayTeamName", "HomeGoal", "AwayGoal", "HomeGoalInfo", "AwayGoalInfo", "HomeAssistInfo", "AwayAssistInfo", "HomePlayerInfo", "AwayPlayerInfo"]
    df = pd.read_csv('Data/DevUtd_MatchInfo.csv', sep=',', skiprows=[0], engine='python', names=colnames,
                     encoding='utf-16')

    # 행 돌면서 개별 데이터 삽입
    ########################################################
    # csv 의 특정 데이터만 삽입 하고 싶을때 아래 인덱스 기입
    isIndividual = True
    startIndex = 61
    endIndex = 61
    ########################################################
    for i in df.index:
        if isIndividual:
            if startIndex-1 > i:
                continue
            if endIndex-1 < i:
                break
        matchDate = str(df.at[i, 'MatchDate']).replace("\n", "")
        matchTime = str(df.at[i, 'MatchTime']).replace("\n", "")
        matchType = int(df.at[i, 'MatchType'])
        infoType = int(df.at[i, 'InfoType'])
        comment = str(df.at[i, 'Comment']).replace("\n", "")
        homeTeamName = str(df.at[i, 'HomeTeamName']).replace("\n", "")
        awayTeamName = str(df.at[i, 'AwayTeamName']).replace("\n", "")
        homeGoal = int(df.at[i, 'HomeGoal'])
        awayGoal = int(df.at[i, 'AwayGoal'])
        homeGoalList = df.at[i, 'HomeGoalInfo']
        if type(homeGoalList) is str:
            homeGoalListSplit = homeGoalList.split(',')
            homeIndex = 1
            for homeGoalData in homeGoalListSplit:
                homeGoalData = homeGoalData.replace('("', "")
                homeGoalData = homeGoalData.replace('")', "")
                homeGoalData = homeGoalData.replace('\"', "")
                DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'HomeGoalInfo/' + str(homeIndex) + '/Name', homeGoalData.strip())
                homeIndex += 1

        awayGoalList = df.at[i, 'AwayGoalInfo']
        if type(awayGoalList) is str:
            awayGoalListSplit = awayGoalList.split(',')
            awayIndex = 1
            for awayGoalData in awayGoalListSplit:
                awayGoalData = awayGoalData.replace('("', "")
                awayGoalData = awayGoalData.replace('")', "")
                awayGoalData = awayGoalData.replace('\"', "")
                DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'AwayGoalInfo/' + str(awayIndex) + '/Name', awayGoalData.strip())
                awayIndex += 1

        homeAssistList = df.at[i, 'HomeAssistInfo']
        if type(homeAssistList) is str:
            homeAssistListSplit = homeAssistList.split(',')
            homeIndex = 1
            for homeAssist in homeAssistListSplit:
                homeAssist = homeAssist.replace('("', "")
                homeAssist = homeAssist.replace('")', "")
                homeAssist = homeAssist.replace('\"', "")
                DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'HomeAssistInfo/' + str(homeIndex) + '/Name', homeAssist.strip())
                homeIndex += 1

        awayAssistList = df.at[i, 'AwayAssistInfo']
        if type(awayAssistList) is str:
            awayAssistListSplit = awayAssistList.split(',')
            awayIndex = 1
            for awayAssist in awayAssistListSplit:
                awayAssist = awayAssist.replace('("', "")
                awayAssist = awayAssist.replace('")', "")
                awayAssist = awayAssist.replace('\"', "")
                DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'AwayAssistInfo/' + str(awayIndex) + '/Name', awayAssist.strip())
                awayIndex += 1

        homePlayerList = df.at[i, 'HomePlayerInfo']
        if type(homePlayerList) is str:
            homePlayerListSplit = homePlayerList.split(',')
            homeIndex = 1
            for homePlayer in homePlayerListSplit:
                homePlayer = homePlayer.replace('("', "")
                homePlayer = homePlayer.replace('")', "")
                homePlayer = homePlayer.replace('\"', "")
                DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'HomePlayerInfo/' + str(homeIndex) + '/Name', homePlayer.strip())
                homeIndex += 1

        awayPlayerList = df.at[i, 'AwayPlayerInfo']
        if type(awayPlayerList) is str:
            awayPlayerListSplit = awayPlayerList.split(',')
            awayIndex = 1
            for awayPlayer in awayPlayerListSplit:
                awayPlayer = awayPlayer.replace('("', "")
                awayPlayer = awayPlayer.replace('")', "")
                awayPlayer = awayPlayer.replace('\"', "")
                DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'AwayPlayerInfo/' + str(awayIndex) + '/Name', awayPlayer.strip())
                awayIndex += 1

        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'MatchDate', matchDate)
        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'MatchTime', matchTime)
        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'MatchType', matchType)
        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'InfoType', infoType)
        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'Comment', comment)
        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'HomeTeamName', homeTeamName)
        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'AwayTeamName', awayTeamName)
        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'HomeGoal', homeGoal)
        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'AwayGoal', awayGoal)

        print('MatchData Insert : ' + homeTeamName + " VS " + awayTeamName + " [" + matchDate + "]")

def main():
    # FireBase DB 업데이트
    DevUtd_FireBase_DB.LoadFireBaseDB()

    # 팀 데이터 업데이트
    #UpdateTeamInfoData()

    # 플레이어 데이터 업데이트
    UpdatePlayerInfoData()

    # 매치 데이터 업데이트
    #UpdateMatchInfoData()

    # 버전 업
    UpdateDetailVersion()

if __name__ == '__main__':
    main()