import io
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase DataBase 인증 및 앱 초기화
cred = credentials.Certificate('DevUtd_Firebase_key.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://devutd-8c34e-default-rtdb.firebaseio.com'})

def UpdateTeamData(teamID : str, key1 : str, value: str):
    ref = db.reference()
    ref.update({'TeamInfo/'+ teamID + '/' + key1: value})

def RemoveTeamData(teamID: str):
    ref = db.reference('TeamInfo/' + teamID)
    ref.delete()

def UpdateStadiumData(stadiumID: str, key1: str, value: str):
    ref = db.reference()
    ref.update({'StadiumInfo/' + stadiumID + '/' + key1: value})

def RemoveStadiumData(stadiumID: str):
    ref = db.reference('StadiumInfo/' + stadiumID)
    ref.delete()

def UpdatePlayerData(playerName : str, key1 : str, value: str):
    ref = db.reference()
    ref.update({'PlayerInfo/'+ playerName + '/' + key1: value})

def RemovePlayerData(playerID: str):
    ref = db.reference('PlayerInfo/' + playerID)
    ref.delete()

def UpdateMatchData(matchDate : str, key1 : str, value: str):
    ref = db.reference()
    ref.update({'MatchInfo/'+ matchDate + '/' + key1: value})

def RemoveMatchData(matchID: str):
    ref = db.reference('MatchInfo/' + matchID)
    ref.delete()

def RemoveMatchDetailData(matchID: str, key : str):
    ref = db.reference('MatchInfo/' + matchID + '/' + key)
    ref.delete()

def UpdateDetailData(productID : str, key1 : str, value: str):
    ref = db.reference()
    ref.update({'BootsDetail/'+ productID + '/' + key1: value})

def RemoveDetailData(removePath: str):
    ref = db.reference('BootsDetail/' + removePath)
    ref.delete()

def UpdateData(productID : str, key1 : str, key2 : str, value : str):
    ref = db.reference('BootsInfo/'+ productID + '/' + key1)
    ref.update({key2: value})

def UpdateLowPriceData(productID: str, key1: str, key2: str, key3: str, value: str):
    ref = db.reference('BootsInfo/' + productID + '/' + key1+ '/' + key2)
    ref.update({key3: value})

def RemoveData(removePath : str):
    ref = db.reference('BootsInfo/'+ removePath)
    ref.delete()

def UpdateVer(newFbmVer: str):
    ref = db.reference()
    ref.update({'FBM_Ver': newFbmVer})

def UpdateDetailVer(newFbmVer: str):
    ref = db.reference()
    ref.update({'FBM_Detail_Ver': newFbmVer})

def LoadFireBaseDB():
    ####################################################################
    # 팀 정보
    ref = db.reference('TeamInfo')
    row = ref.get()
    with io.open('last_FireBaseDB_TeamInfo.json', 'w') as make_file:
      json.dump(row, make_file, indent="\t")
    ####################################################################

    ####################################################################
    # 구장 정보
    ref = db.reference('StadiumInfo')
    row = ref.get()
    with io.open('last_FireBaseDB_StadiumInfo.json', 'w') as make_file:
        json.dump(row, make_file, indent="\t")
    ####################################################################

    ####################################################################
    # 플레이어 정보
    refDetail = db.reference('PlayerInfo')
    rowDetail = refDetail.get()
    with io.open('last_FireBaseDB_PlayerInfo.json', 'w') as make_file:
      json.dump(rowDetail, make_file, indent="\t")
    ####################################################################

    ####################################################################
    # 매치 정보
    refMatch = db.reference('MatchInfo')
    rowMatch = refMatch.get()
    with io.open('last_FireBaseDB_MatchInfo.json', 'w') as make_file:
      json.dump(rowMatch, make_file, indent="\t")
    ####################################################################

    ####################################################################
    # 버전 가져오기
    refVer = db.reference('FBM_Detail_Ver')
    rowVer = refVer.get()
    fWrite = open("last_DevUtd_Version.txt", 'w', encoding='UTF8')
    fWrite.write(str(rowVer))
    fWrite.close()
    ####################################################################
    '''
    # Json파일에 쓰기
    with io.open('last_FBM_Version.json', 'w') as make_file:
        json.dump(rowVer, make_file, indent="\t")
    '''

def main():
    LoadFireBaseDB()

if __name__ == '__main__':
    main()