import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import DevUtd_FireBase_DB
import time
import json

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.isOk = False

    def setupUI(self):
        self.setGeometry(600, 550, 300, 100)
        self.setWindowTitle("로그인")
        self.setWindowIcon(QIcon('icon.png'))

        self.labelPassword = QLabel("비밀번호: ")

        self.lineEdit1 = QLineEdit()
        self.pushButton1 = QPushButton("확인")
        self.pushButton1.clicked.connect(self.okButtonClicked)
        self.pushButton2 = QPushButton("취소")
        self.pushButton2.clicked.connect(self.cancelButtonClicked)

        layout = QGridLayout()
        layout.addWidget(self.labelPassword, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(self.pushButton2, 1, 2)

        self.setLayout(layout)

    def okButtonClicked(self):
        if self.lineEdit1.text() == '01025457372':
            self.isOk = True
        else:
            self.isOk = False

        self.close()

    def cancelButtonClicked(self):
        self.isOk = False
        self.close()

class TeamDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.id = None
        self.teamName = None
        self.logoURL = None
        self.isOk = False

    def setupUI(self):
        self.setGeometry(200, 200, 500, 100)
        self.setWindowTitle("팀 추가")
        self.setWindowIcon(QIcon('icon.png'))

        self.labelTeamName = QLabel("팀 이름: ")
        labelLogoURL = QLabel("로고 URL: ")

        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.pushButton1= QPushButton("확인")
        self.pushButton1.clicked.connect(self.okButtonClicked)
        self.pushButton2 = QPushButton("취소")
        self.pushButton2.clicked.connect(self.cancelButtonClicked)

        layout = QGridLayout()
        layout.addWidget(self.labelTeamName, 0, 0)
        layout.addWidget(self.lineEdit2, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(labelLogoURL, 1, 0)
        layout.addWidget(self.lineEdit3, 1, 1)
        layout.addWidget(self.pushButton2, 1, 2)

        self.setLayout(layout)
    
    def modifyMode(self, teamID : str, teamName : str, teamLogo : str):
        self.setWindowTitle("팀 수정")
        self.labelTeamName.setText('팀 이름: ' + teamID)
        self.lineEdit2.setVisible(False)
        self.lineEdit2.setText(teamName)
        self.lineEdit3.setText(teamLogo)

    def okButtonClicked(self):
        self.isOk = True
        self.teamName = self.lineEdit2.text()
        self.id = self.teamName
        self.logoURL = self.lineEdit3.text()
        self.close()

    def cancelButtonClicked(self):
        self.isOk = False
        self.close()

class StadiumDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.id = None
        self.stadiumName = None
        self.TMapURL = None
        self.KakaoURL = None
        self.NaverMapURL = None
        self.Address = None
        self.isOk = False

    def setupUI(self):
        self.setGeometry(200, 200, 500, 100)
        self.setWindowTitle("구장 추가")
        self.setWindowIcon(QIcon('icon.png'))

        self.labelStadiumName = QLabel("구장 이름: ")
        self.labelTMapURL = QLabel("T-Map URL: ")
        self.labelKakaoURL = QLabel("카카오 내비 URL: ")
        self.labelNaverURL = QLabel("네이버 지도 URL: ")
        self.labelAddress = QLabel("주소: ")

        self.lineEditStadium = QLineEdit()
        self.lineEditTMap = QLineEdit()
        self.lineEditKakao = QLineEdit()
        self.lineEditNaver = QLineEdit()
        self.lineEditAddress = QLineEdit()
        self.pushButton1 = QPushButton("확인")
        self.pushButton1.clicked.connect(self.okButtonClicked)
        self.pushButton2 = QPushButton("취소")
        self.pushButton2.clicked.connect(self.cancelButtonClicked)

        layout = QGridLayout()
        layout.addWidget(self.labelStadiumName, 0, 0)
        layout.addWidget(self.lineEditStadium, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(self.labelTMapURL, 1, 0)
        layout.addWidget(self.lineEditTMap, 1, 1)
        layout.addWidget(self.pushButton2, 1, 2)
        layout.addWidget(self.labelKakaoURL, 2, 0)
        layout.addWidget(self.lineEditKakao, 2, 1)
        layout.addWidget(self.labelNaverURL, 3, 0)
        layout.addWidget(self.lineEditNaver, 3, 1)
        layout.addWidget(self.labelAddress, 4, 0)
        layout.addWidget(self.lineEditAddress, 4, 1)

        self.setLayout(layout)

    def modifyMode(self, stadiumID: str, stadiumName: str, TMapURL: str, KakaoURL: str, NaverURL: str, Address: str):
        self.setWindowTitle("구장 수정")
        self.labelStadiumName.setText('구장 이름: ' + stadiumID)
        self.lineEditStadium.setVisible(False)
        self.lineEditStadium.setText(stadiumName)
        self.lineEditTMap.setText(TMapURL)
        self.lineEditKakao.setText(KakaoURL)
        self.lineEditNaver.setText(NaverURL)
        self.lineEditAddress.setText(Address)

    def okButtonClicked(self):
        self.isOk = True
        self.stadiumName = self.lineEditStadium.text()
        self.TMapURL = self.lineEditTMap.text()
        self.KakaoURL = self.lineEditKakao.text()
        self.NaverMapURL = self.lineEditNaver.text()
        self.Address = self.lineEditAddress.text()
        self.id = self.stadiumName
        self.close()

    def cancelButtonClicked(self):
        self.isOk = False
        self.close()

class PlayerDialog(QDialog):
    def __init__(self):
        super().__init__()
        #self.setupUI()

        self.id = None
        self.playerName = None
        self.teamName = None
        self.pictureURL = None
        self.mvpNum = None
        self.goalKingNum = None
        self.assistKingNum = None
        self.attendanceKingNum = None
        self.pointKingNum = None
        self.defenceKingNum = None
        self.isOk = False

    def setupUI(self, teamID):
        self.setGeometry(200, 200, 500, 100)
        self.setWindowTitle("플레이어 추가")
        self.setWindowIcon(QIcon('icon.png'))
        self.labelPlayerName = QLabel("플레이어 이름: ")
        labelPlayerTeamName = QLabel("소속팀: ")
        labelPictureURL = QLabel("사진 URL: ")
        labelMvpNum = QLabel("MVP 횟수: ")
        labelGoalKingNum = QLabel("득점왕 횟수: ")
        labelAssistKingNum = QLabel("도움왕 횟수: ")
        labelAttendanceKingNum = QLabel("츨석왕 횟수: ")
        labelPointKingNum = QLabel("공격 포인트왕 횟수: ")
        labelDefenceKingNum = QLabel("수비왕 횟수: ")

        self.teamIDs = teamID
        self.cbTeam = QComboBox(self)
        for team in teamID:
            self.cbTeam.addItem(team)

        onlyInt = QIntValidator()
        self.lineEdit2 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit5.setValidator(onlyInt)
        self.lineEdit5.setText(str(0))
        self.lineEdit6 = QLineEdit()
        self.lineEdit6.setValidator(onlyInt)
        self.lineEdit6.setText(str(0))
        self.lineEdit7 = QLineEdit()
        self.lineEdit7.setValidator(onlyInt)
        self.lineEdit7.setText(str(0))
        self.lineEdit8 = QLineEdit()
        self.lineEdit8.setValidator(onlyInt)
        self.lineEdit8.setText(str(0))
        self.lineEdit9 = QLineEdit()
        self.lineEdit9.setValidator(onlyInt)
        self.lineEdit9.setText(str(0))
        self.lineEdit10 = QLineEdit()
        self.lineEdit10.setValidator(onlyInt)
        self.lineEdit10.setText(str(0))
        self.pushButton1 = QPushButton("확인")
        self.pushButton1.clicked.connect(self.okButtonClicked)
        self.pushButton2 = QPushButton("취소")
        self.pushButton2.clicked.connect(self.cancelButtonClicked)

        layout = QGridLayout()
        layout.addWidget(self.labelPlayerName, 0, 0)
        layout.addWidget(self.lineEdit2, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(labelPlayerTeamName, 1, 0)
        layout.addWidget(self.cbTeam, 1, 1)
        layout.addWidget(self.pushButton2, 1, 2)
        layout.addWidget(labelPictureURL, 2, 0)
        layout.addWidget(self.lineEdit4, 2, 1)
        layout.addWidget(labelMvpNum, 3, 0)
        layout.addWidget(self.lineEdit5, 3, 1)
        layout.addWidget(labelGoalKingNum, 4, 0)
        layout.addWidget(self.lineEdit6, 4, 1)
        layout.addWidget(labelAssistKingNum, 5, 0)
        layout.addWidget(self.lineEdit7, 5, 1)
        layout.addWidget(labelAttendanceKingNum, 6, 0)
        layout.addWidget(self.lineEdit8, 6, 1)
        layout.addWidget(labelPointKingNum, 7, 0)
        layout.addWidget(self.lineEdit9, 7, 1)
        layout.addWidget(labelDefenceKingNum, 8, 0)
        layout.addWidget(self.lineEdit10, 8, 1)

        self.setLayout(layout)

    def modifyMode(self, playerID: str, playerName: str, teamName: str, pictureURL: str,
                   mvpNum: int, goalKingNum: int, assistKingNum: int, attendanceKingNum: int, pointKingNum: int, defenceKingNum: int):
        self.setWindowTitle("플레이어 수정")
        self.labelPlayerName.setText('플레이어 이름: ' + playerID)
        self.lineEdit2.setVisible(False)
        self.lineEdit2.setText(playerName)
        self.lineEdit4.setText(pictureURL)
        self.lineEdit5.setText(str(mvpNum))
        self.lineEdit6.setText(str(goalKingNum))
        self.lineEdit7.setText(str(assistKingNum))
        self.lineEdit8.setText(str(attendanceKingNum))
        self.lineEdit9.setText(str(pointKingNum))
        self.lineEdit10.setText(str(defenceKingNum))

        teamIndex = 0
        for team in self.teamIDs:
            if team == teamName:
                self.cbTeam.setCurrentIndex(teamIndex)
                break
            teamIndex = teamIndex + 1

    def okButtonClicked(self):
        self.isOk = True
        self.playerName = self.lineEdit2.text()
        self.id = self.playerName
        self.teamName = self.cbTeam.currentText()
        self.pictureURL = self.lineEdit4.text()
        self.mvpNum = self.lineEdit5.text()
        self.goalKingNum = self.lineEdit6.text()
        self.assistKingNum = self.lineEdit7.text()
        self.attendanceKingNum = self.lineEdit8.text()
        self.pointKingNum = self.lineEdit9.text()
        self.defenceKingNum = self.lineEdit10.text()
        self.close()

    def cancelButtonClicked(self):
        self.isOk = False
        self.close()

class PlayerEditDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.id = None
        self.editPlayerDatas = []
        self.teamName = None
        self.logoURL = None
        self.isOk = False

    def setupUI(self, playerID, curHomeGoalInfo):
        self.setGeometry(800, 200, 500, 800)
        self.setWindowTitle("선수 편집")
        self.setWindowIcon(QIcon('icon.png'))

        self.playerID = playerID
        self.pushButton1 = QPushButton("확인")
        self.pushButton1.clicked.connect(self.okButtonClicked)

        #############################################################
        # Left
        self.playerListview = QListView(self)
        playerModel = QStandardItemModel()
        for player in self.playerID:
            playerModel.appendRow(QStandardItem(player))
        self.playerListview.setModel(playerModel)
        self.playerListview.resize(50, 500)

        leftGroupBox = QGroupBox("선수 리스트")
        leftInnerLayOut = QVBoxLayout()
        leftInnerLayOut.addWidget(self.playerListview)
        leftGroupBox.setLayout(leftInnerLayOut)

        leftLayOut = QVBoxLayout()
        leftLayOut.addWidget(leftGroupBox)

        #############################################################
        # center button
        addButton = QPushButton("->")
        addButton.clicked.connect(self.addButtonClicked)
        removeButton = QPushButton("<-")
        removeButton.clicked.connect(self.removeButtonClicked)

        editButtonLayOut = QVBoxLayout()
        editButtonLayOut.addWidget(addButton)
        editButtonLayOut.addWidget(removeButton)
        editButtonLayOut.setAlignment(Qt.AlignCenter)

        #############################################################
        # Center
        self.playerEditview = QListView(self)
        self.editModel = QStandardItemModel()
        for info in curHomeGoalInfo:
            self.editModel.appendRow(QStandardItem(info))
        self.playerEditview.setModel(self.editModel)
        self.playerEditview.resize(50, 500)

        centerGroupBox = QGroupBox("추가 리스트")
        centerInnerLayOut = QVBoxLayout()
        centerInnerLayOut.addWidget(self.playerEditview)
        centerGroupBox.setLayout(centerInnerLayOut)

        centerLayOut = QVBoxLayout()
        centerLayOut.addWidget(centerGroupBox)

        #############################################################
        # Right
        rightLayOut = QVBoxLayout()
        rightLayOut.addWidget(self.pushButton1)
        rightLayOut.addStretch(3)

        #############################################################
        # Final
        layout = QHBoxLayout()
        layout.addLayout(leftLayOut)
        layout.addLayout(editButtonLayOut)
        layout.addLayout(centerLayOut)
        layout.addLayout(rightLayOut)

        self.setLayout(layout)

    def modifyMode(self, teamID: str, teamName: str, teamLogo: str):
        self.setWindowTitle("팀 수정")
        self.labelID.setText('ID: ' + teamID)
        self.lineEdit1.setVisible(False)
        self.lineEdit2.setText(teamName)
        self.lineEdit3.setText(teamLogo)

    def okButtonClicked(self):
        self.isOk = True
        self.editPlayerDatas = []
        for index in range(self.editModel.rowCount()):
            item = self.editModel.item(index)
            self.editPlayerDatas.append(item.data(Qt.DisplayRole))

        self.close()

    def addButtonClicked(self):
        curIndex = self.playerListview.currentIndex()
        if curIndex.row() > -1:
            curPlayer = curIndex.data(Qt.DisplayRole)
            self.editModel.appendRow(QStandardItem(curPlayer))

    def removeButtonClicked(self):
        curIndex = self.playerEditview.currentIndex()
        if curIndex.row() > -1:
            self.editModel.removeRow(curIndex.row())

class MatchDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.id = None
        self.matchDate = None
        self.matchTime = None
        self.matchType = None
        self.infoType = None
        self.comment = None
        self.homeTeamName = None
        self.awayTeamName = None
        self.homeGoal = None
        self.awayGoal = None
        self.homeGoalInfo = []
        self.awayGoalInfo = []
        self.homeAssistInfo = []
        self.awayAssistInfo = []
        self.homePlayerInfo = []
        self.awayPlayerInfo = []
        self.isOk = False

    def setupUI(self, teamID, playerID, stadiumID):
        self.setGeometry(200, 200, 500, 100)
        self.setWindowTitle("경기 추가")
        self.setWindowIcon(QIcon('icon.png'))
        self.labelMatchDate = QLabel("날짜: ")
        labelMatchTime = QLabel("시간: ")
        labelMatchType = QLabel("경기 타입: ")
        labelInfoType = QLabel("정보 타입: ")
        labelComment = QLabel("구장 정보: ")
        labelHomeTeamName = QLabel("홈팀: ")
        labelAwayTeamName = QLabel("원정팀: ")
        labelHomeTeamGoal = QLabel("홈골: ")
        labelAwayTeamGoal = QLabel("원정골: ")
        labelHomeGoalInfo = QLabel("홈 득점자: ")
        labelAwayGoalInfo = QLabel("원정 득점자: ")
        labelHomeAssistInfo = QLabel("홈 도움: ")
        labelAwayAssistInfo = QLabel("원정 도움: ")
        labelHomePlayerInfo = QLabel("홈팀 인원: ")
        labelAwayPlayerInfo = QLabel("원정팀 인원: ")

        self.teamIDs = teamID
        self.stadiumIDs = stadiumID
        self.playerID = playerID
        self.cbHomeTeam = QComboBox(self)
        self.cbAwayTeam = QComboBox(self)
        for team in teamID:
            self.cbHomeTeam.addItem(team)
            self.cbAwayTeam.addItem(team)

        self.cbStadium = QComboBox(self)
        for stadium in stadiumID:
            self.cbStadium.addItem(stadium)

        self.cbMatchType = QComboBox(self)
        self.cbMatchType.addItem('A매치')
        self.cbMatchType.addItem('자체전')
        self.cbInfoType = QComboBox(self)
        self.cbInfoType.addItem('경기 전')
        self.cbInfoType.addItem('경기 종료')

        self.cbHomeGoalInfo = QComboBox(self)
        self.cbAwayGoalInfo = QComboBox(self)
        self.cbHomeAssistInfo = QComboBox(self)
        self.cbAwayAssistInfo = QComboBox(self)
        self.cbHomePlayerInfo = QComboBox(self)
        self.cbAwayPlayerInfo = QComboBox(self)

        onlyInt = QIntValidator()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit5.setValidator(onlyInt)
        self.lineEdit5.setText(str(0))
        self.lineEdit6 = QLineEdit()
        self.lineEdit6.setValidator(onlyInt)
        self.lineEdit6.setText(str(0))
        self.pushButton1 = QPushButton("확인")
        self.pushButton1.clicked.connect(self.okButtonClicked)
        self.pushButton2 = QPushButton("취소")
        self.pushButton2.clicked.connect(self.cancelButtonClicked)
        self.homeGoalInfoBtn = QPushButton("홈 득점자 입력")
        self.homeGoalInfoBtn.clicked.connect(self.homeGoalInfoBtnClicked)
        self.awayGoalInfoBtn = QPushButton("원정 득점자 입력")
        self.awayGoalInfoBtn.clicked.connect(self.awayGoalInfoBtnClicked)
        self.homeAssistInfoBtn = QPushButton("홈 도움 입력")
        self.homeAssistInfoBtn.clicked.connect(self.homeAssistInfoBtnClicked)
        self.awayAssistInfoBtn = QPushButton("원정 도움 입력")
        self.awayAssistInfoBtn.clicked.connect(self.awayAssistInfoBtnClicked)
        self.homePlayerInfoBtn = QPushButton("홈팀 인원 입력")
        self.homePlayerInfoBtn.clicked.connect(self.homePlayerInfoBtnClicked)
        self.awayPlayerInfoBtn = QPushButton("원정팀 인원 입력")
        self.awayPlayerInfoBtn.clicked.connect(self.awayPlayerInfoBtnClicked)

        layout = QGridLayout()
        layout.addWidget(self.labelMatchDate, 0, 0)
        layout.addWidget(self.lineEdit2, 0, 1)
        layout.addWidget(self.pushButton1, 0, 3)
        layout.addWidget(labelMatchTime, 1, 0)
        layout.addWidget(self.lineEdit3, 1, 1)
        layout.addWidget(self.pushButton2, 1, 3)
        layout.addWidget(labelMatchType, 2, 0)
        layout.addWidget(self.cbMatchType, 2, 1)
        layout.addWidget(labelInfoType, 3, 0)
        layout.addWidget(self.cbInfoType, 3, 1)
        layout.addWidget(labelComment, 4, 0)
        layout.addWidget(self.cbStadium, 4, 1)
        layout.addWidget(labelHomeTeamName, 5, 0)
        layout.addWidget(self.cbHomeTeam, 5, 1)
        layout.addWidget(labelAwayTeamName, 6, 0)
        layout.addWidget(self.cbAwayTeam, 6, 1)
        layout.addWidget(labelHomeTeamGoal, 7, 0)
        layout.addWidget(self.lineEdit5, 7, 1)
        layout.addWidget(labelAwayTeamGoal, 8, 0)
        layout.addWidget(self.lineEdit6, 8, 1)
        layout.addWidget(labelHomeGoalInfo, 9, 0)
        layout.addWidget(self.cbHomeGoalInfo, 9, 1)
        layout.addWidget(self.homeGoalInfoBtn, 9, 2)
        layout.addWidget(labelAwayGoalInfo, 10, 0)
        layout.addWidget(self.cbAwayGoalInfo, 10, 1)
        layout.addWidget(self.awayGoalInfoBtn, 10, 2)
        layout.addWidget(labelHomeAssistInfo, 11, 0)
        layout.addWidget(self.cbHomeAssistInfo, 11, 1)
        layout.addWidget(self.homeAssistInfoBtn, 11, 2)
        layout.addWidget(labelAwayAssistInfo, 12, 0)
        layout.addWidget(self.cbAwayAssistInfo, 12, 1)
        layout.addWidget(self.awayAssistInfoBtn, 12, 2)
        layout.addWidget(labelHomePlayerInfo, 13, 0)
        layout.addWidget(self.cbHomePlayerInfo, 13, 1)
        layout.addWidget(self.homePlayerInfoBtn, 13, 2)
        layout.addWidget(labelAwayPlayerInfo, 14, 0)
        layout.addWidget(self.cbAwayPlayerInfo, 14, 1)
        layout.addWidget(self.awayPlayerInfoBtn, 14, 2)

        self.setLayout(layout)

    def modifyMode(self, matchDate: str, matchTime: str, matchType: int, infoType: int,
                   comment: str, homeTeamName: str, awayTeamName: str, homeGoal: int, awayGoal: int,
                   homeGoalInfo, awayGoalInfo, homeAssistInfo, awayAssistInfo, homePlayerInfo, awayPlayerInfo):
        self.setWindowTitle("경기 수정")
        self.labelMatchDate.setText('날짜: ' + matchDate)
        self.lineEdit2.setText(matchDate)
        self.lineEdit3.setText(matchTime)
        self.lineEdit5.setText(str(homeGoal))
        self.lineEdit6.setText(str(awayGoal))
        self.cbMatchType.setCurrentIndex(matchType)
        self.cbInfoType.setCurrentIndex(infoType)

        teamIndex = 0
        for team in self.teamIDs:
            if team == homeTeamName:
                self.cbHomeTeam.setCurrentIndex(teamIndex)
            elif team == awayTeamName:
                self.cbAwayTeam.setCurrentIndex(teamIndex)
            teamIndex = teamIndex + 1

        stadiumIndex = 0
        for stadium in self.stadiumIDs:
            if stadium == comment:
                self.cbStadium.setCurrentIndex(stadiumIndex)
            stadiumIndex = stadiumIndex + 1

        self.cbHomeGoalInfo.clear()
        self.homeGoalInfo = []
        for info in homeGoalInfo:
            if info:
                self.cbHomeGoalInfo.addItem(info['Name'])
                self.homeGoalInfo.append(info['Name'])

        self.cbAwayGoalInfo.clear()
        self.awayGoalInfo = []
        for info in awayGoalInfo:
            if info:
                self.cbAwayGoalInfo.addItem(info['Name'])
                self.awayGoalInfo.append(info['Name'])

        self.cbHomeAssistInfo.clear()
        self.homeAssistInfo = []
        for info in homeAssistInfo:
            if info:
                self.cbHomeAssistInfo.addItem(info['Name'])
                self.homeAssistInfo.append(info['Name'])

        self.cbAwayAssistInfo.clear()
        self.awayAssistInfo = []
        for info in awayAssistInfo:
            if info:
                self.cbAwayAssistInfo.addItem(info['Name'])
                self.awayAssistInfo.append(info['Name'])

        self.cbHomePlayerInfo.clear()
        self.homePlayerInfo = []
        for info in homePlayerInfo:
            if info:
                self.cbHomePlayerInfo.addItem(info['Name'])
                self.homePlayerInfo.append(info['Name'])

        self.cbAwayPlayerInfo.clear()
        self.awayPlayerInfo = []
        for info in awayPlayerInfo:
            if info:
                self.cbAwayPlayerInfo.addItem(info['Name'])
                self.awayPlayerInfo.append(info['Name'])


    def okButtonClicked(self):
        self.isOk = True
        self.matchDate = self.lineEdit2.text()
        self.id = self.matchDate
        self.matchTime = self.lineEdit3.text()
        self.matchType = self.cbMatchType.currentText()
        self.infoType = self.cbInfoType.currentText()
        self.comment = self.cbStadium.currentText()
        self.homeTeamName = self.cbHomeTeam.currentText()
        self.awayTeamName = self.cbAwayTeam.currentText()
        self.homeGoal = self.lineEdit5.text()
        self.awayGoal = self.lineEdit6.text()
        self.close()

    def cancelButtonClicked(self):
        self.isOk = False
        self.close()

    def homeGoalInfoBtnClicked(self):
        dlg = PlayerEditDialog()
        dlg.setupUI(self.playerID, self.homeGoalInfo)
        dlg.exec_()
        self.cbHomeGoalInfo.clear()
        self.homeGoalInfo = dlg.editPlayerDatas
        for info in self.homeGoalInfo:
            self.cbHomeGoalInfo.addItem(info)

    def awayGoalInfoBtnClicked(self):
        dlg = PlayerEditDialog()
        dlg.setupUI(self.playerID, self.awayGoalInfo)
        dlg.exec_()
        self.cbAwayGoalInfo.clear()
        self.awayGoalInfo = dlg.editPlayerDatas
        for info in self.awayGoalInfo:
            self.cbAwayGoalInfo.addItem(info)

    def homeAssistInfoBtnClicked(self):
        dlg = PlayerEditDialog()
        dlg.setupUI(self.playerID, self.homeAssistInfo)
        dlg.exec_()
        self.cbHomeAssistInfo.clear()
        self.homeAssistInfo = dlg.editPlayerDatas
        for info in self.homeAssistInfo:
            self.cbHomeAssistInfo.addItem(info)

    def awayAssistInfoBtnClicked(self):
        dlg = PlayerEditDialog()
        dlg.setupUI(self.playerID, self.awayAssistInfo)
        dlg.exec_()
        self.cbAwayAssistInfo.clear()
        self.awayAssistInfo = dlg.editPlayerDatas
        for info in self.awayAssistInfo:
            self.cbAwayAssistInfo.addItem(info)

    def homePlayerInfoBtnClicked(self):
        dlg = PlayerEditDialog()
        dlg.setupUI(self.playerID, self.homePlayerInfo)
        dlg.exec_()
        self.cbHomePlayerInfo.clear()
        self.homePlayerInfo = dlg.editPlayerDatas
        for info in self.homePlayerInfo:
            self.cbHomePlayerInfo.addItem(info)

    def awayPlayerInfoBtnClicked(self):
        dlg = PlayerEditDialog()
        dlg.setupUI(self.playerID, self.awayPlayerInfo)
        dlg.exec_()
        self.cbAwayPlayerInfo.clear()
        self.awayPlayerInfo = dlg.editPlayerDatas
        for info in self.awayPlayerInfo:
            self.cbAwayPlayerInfo.addItem(info)

class DevToolApp(QWidget):
    curVer = '0'
    teamInfos = {}
    team_ID = []
    stadiumInfos = {}
    stadium_ID = []
    playerInfos = {}
    player_ID = []
    matchInfos = {}
    match_ID = []

    def __init__(self):
        super().__init__()

        #self.readData()
        self.initUI()

    def readVer(self):
        f = open("last_DevUtd_Version.txt", 'r', encoding='utf-8')
        curVer_List = f.readlines()
        if len(curVer_List) > 0:
            self.curVer = curVer_List[0]
            print(self.curVer)

        f.close()

    def readTeamInfos(self):
        self.team_ID = []

        with open('last_FireBaseDB_TeamInfo.json', 'r', encoding='utf-8') as f:
            self.teamInfos = json.load(f)

        for teamID in self.teamInfos:
            self.team_ID.append(teamID)

    def readStadiumInfos(self):
        self.stadium_ID = []

        with open('last_FireBaseDB_StadiumInfo.json', 'r', encoding='utf-8') as f:
            self.stadiumInfos = json.load(f)

        for stadiumID in self.stadiumInfos:
            self.stadium_ID.append(stadiumID)

    def readPlayerInfos(self):
        self.player_ID = []

        with open('last_FireBaseDB_PlayerInfo.json', 'r', encoding='utf-8') as f:
            self.playerInfos = json.load(f)

        for playerID in self.playerInfos:
            self.player_ID.append(playerID)

    def readMatchInfos(self):
        self.match_ID = []

        with open('last_FireBaseDB_MatchInfo.json', 'r', encoding='utf-8') as f:
            self.matchInfos = json.load(f)

        for MatchID in self.matchInfos:
            self.match_ID.append(MatchID)

    def readData(self):
        # 최신 버전
        self.readVer()

        # 팀 정보
        self.readTeamInfos()

        # 구장 정보
        self.readStadiumInfos()

        # 선수 정보
        self.readPlayerInfos()

        # 매치 정보
        self.readMatchInfos()

    def initUI(self):
        tabs = QTabWidget()
        self.mainTab = self.make_mainTab()
        self.teamTab = self.make_teamAddTab()
        self.stadiumTab = self.make_stadiumAddTab()
        self.playerTab = self.make_playerAddTab()
        self.matchTab = self.make_matchAddTab()

        tabs.addTab(self.mainTab, 'Main')
        tabs.addTab(self.teamTab, '팀 관리')
        tabs.addTab(self.stadiumTab, '구장 관리')
        tabs.addTab(self.playerTab, '선수 관리')
        tabs.addTab(self.matchTab, '매치 관리')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('DevUtd Tool')
        self.setGeometry(100, 100, 1300, 800)
        self.show()

    def UpdateDetailVersion(self):
        # 버전 업
        newVersion = int(self.curVer) + 1
        fWrite = open("last_DevUtd_Version.txt", 'w', encoding='UTF8')
        fWrite.write(str(newVersion))
        fWrite.close()

        DevUtd_FireBase_DB.UpdateDetailVer(newVersion)
        self.curVer = newVersion

    def make_mainTab(self):
        self.label1 = QLabel('현재 버전 : ' + self.curVer, self)
        self.label1.setAlignment(Qt.AlignCenter)
        font1 = self.label1.font()
        font1.setPointSize(20)
        self.label1.setFont(font1)

        loginBtn = QPushButton('로그인', self)
        loginBtn.clicked.connect(self.loginBtn_clicked)
        loginBtn.setEnabled(True)

        logoPixmap = QPixmap('Logo_256.png')
        lbl_img = QLabel()
        lbl_img.setPixmap(logoPixmap)
        lbl_img.setAlignment(Qt.AlignCenter)

        vBox = QVBoxLayout()
        vBox.setAlignment(Qt.AlignCenter)
        vBox.addWidget(lbl_img)
        vBox.addWidget(self.label1)
        vBox.addSpacing(20)
        vBox.addWidget(loginBtn)
        vBox.addStretch(3)

        tab = QWidget()
        tab.setLayout(vBox)
        return tab

    def loginBtn_clicked(self):
        print("loginBtn_clicked 클릭")
        btn = self.sender()
        btn.setEnabled(False)

        dlg = LoginDialog()
        dlg.exec_()
        isOk = dlg.isOk

        if isOk:
            btn.setEnabled(False)
            # FireBase DB 업데이트
            DevUtd_FireBase_DB.LoadFireBaseDB()
            # DB 데이터 읽기
            self.readData()
            # 데이터 초기화
            self.label1.setText('현재 버전 : ' + self.curVer)
            self.initTeamInfoTable()
            self.initStadiumInfoTable()
            self.initPlayerInfoTable()
            self.initMatchInfoTable()
            self.teamTab.setEnabled(True)
            self.stadiumTab.setEnabled(True)
            self.playerTab.setEnabled(True)
            self.matchTab.setEnabled(True)
        else:
            QMessageBox.about(self, '로그인 실패', '로그인에 실패하였습니다.')
            btn.setEnabled(True)

    def initTeamInfoTable(self):
        self.teamTableWidget.setRowCount(0)
        RowCount = len(self.team_ID)
        self.teamTableWidget.setRowCount(RowCount)
        for i in range(RowCount):
            if len(self.team_ID) <= i:
                break
            self.teamTableWidget.setItem(i, 0, QTableWidgetItem(self.team_ID[i]))
            self.teamTableWidget.setItem(i, 1, QTableWidgetItem(self.teamInfos[self.team_ID[i]]['TeamName']))
            self.teamTableWidget.setItem(i, 2, QTableWidgetItem(self.teamInfos[self.team_ID[i]]['TeamLogoURL']))

    def make_teamAddTab(self):
        tab = QWidget()

        groupBox = QGroupBox("팀정보")
        self.teamAddBtn = QPushButton('팀 추가', self)
        self.teamAddBtn.clicked.connect(self.teamAddBtn_clicked)
        self.teamRemoveBtn = QPushButton('팀 삭제', self)
        self.teamRemoveBtn.clicked.connect(self.teamRemoveBtn_clicked)
        self.teamModifyStartBtn = QPushButton('팀 수정', self)
        self.teamModifyStartBtn.clicked.connect(self.teamModifyStartBtn_clicked)

        RowCount = len(self.team_ID)
        ColumnCount = 3
        self.teamTableWidget = QTableWidget(RowCount, ColumnCount)
        self.teamTableWidget.setHorizontalHeaderLabels(["ID", "팀 이름", "Logo URL"])
        self.teamTableWidget.resizeColumnsToContents()
        self.teamTableWidget.resizeRowsToContents()
        self.teamTableWidget.horizontalHeader().setStretchLastSection(True)
        #self.teamTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.teamTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.teamTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.teamTableWidget.setStyleSheet("QHeaderView::section { color:white; background-color:#3E4040; }")
        self.initTeamInfoTable()


        leftInnerLayOut = QVBoxLayout()
        leftInnerLayOut.addWidget(self.teamAddBtn)
        leftInnerLayOut.addWidget(self.teamRemoveBtn)
        leftInnerLayOut.addWidget(self.teamModifyStartBtn)
        leftInnerLayOut.addStretch(3)
        groupBox.setLayout(leftInnerLayOut)

        leftLayOut = QVBoxLayout()
        leftLayOut.addWidget(groupBox)

        rightLayOut = QVBoxLayout()
        rightLayOut.addWidget(self.teamTableWidget)

        layout = QHBoxLayout()
        layout.addLayout(leftLayOut)
        layout.addLayout(rightLayOut)

        tab.setLayout(layout)
        tab.setEnabled(False)
        return tab

    def teamAddBtn_clicked(self):
        print("teamAddBtn_clicked 클릭")
        btn = self.sender()

        dlg = TeamDialog()
        dlg.exec_()
        teamID = dlg.id
        teamName = dlg.teamName
        teamLogoURL = dlg.logoURL
        isOk = dlg.isOk
        
        if teamID == '' or teamName == '':
            QMessageBox.about(self, '팀 추가', '잘못된 입력 입니다.')
            return

        if isOk:
            strInfo = 'ID : ' + teamID + '\n팀 이름 : ' + teamName + '\n로고 URL : ' + teamLogoURL
            reply = QMessageBox.question(self, '팀 추가', '정말로 DB에 팀을 추가하시겠습니까?\n\n' + strInfo,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                DevUtd_FireBase_DB.UpdateTeamData(teamID, 'TeamName', teamName)
                DevUtd_FireBase_DB.UpdateTeamData(teamID, 'TeamLogoURL', teamLogoURL)

                self.UpdateDetailVersion()
                DevUtd_FireBase_DB.LoadFireBaseDB()
                self.readTeamInfos()
                self.initTeamInfoTable()

    def teamRemoveBtn_clicked(self):
        print("teamRemoveBtn_clicked 클릭")
        btn = self.sender()

        removeTeamIndex, ok = QInputDialog.getInt(self, '팀 삭제', '삭제할 팀의 Index 번호를 입력하세요.')
        removeTeamIndex = removeTeamIndex - 1
        if ok:
            if len(self.team_ID) >= removeTeamIndex and removeTeamIndex >= 0:
                strInfo = 'ID : ' + self.team_ID[removeTeamIndex] + '\n팀 이름 : ' + self.teamInfos[self.team_ID[removeTeamIndex]]['TeamName']
                reply = QMessageBox.question(self, '팀 삭제', '정말로 DB에서 팀을 삭제하시겠습니까?\n\n' + strInfo,
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    DevUtd_FireBase_DB.RemoveTeamData(self.team_ID[removeTeamIndex])

                    self.UpdateDetailVersion()
                    DevUtd_FireBase_DB.LoadFireBaseDB()
                    self.readTeamInfos()
                    self.initTeamInfoTable()
            else:
                QMessageBox.about(self, '팀 삭제', '잘못된 인덱스 입니다.')

    def teamModifyStartBtn_clicked(self):
        print("teamModifyStartBtn_clicked 클릭")
        btn = self.sender()

        ModifyTeamIndex, ok = QInputDialog.getInt(self, '팀 수정', '수정할 팀의 Index 번호를 입력하세요.')
        ModifyTeamIndex = ModifyTeamIndex - 1
        if ok:
            if len(self.team_ID) >= ModifyTeamIndex and ModifyTeamIndex >= 0:
                dlg = TeamDialog()
                dlg.modifyMode(self.team_ID[ModifyTeamIndex], self.teamInfos[self.team_ID[ModifyTeamIndex]]['TeamName'],
                               self.teamInfos[self.team_ID[ModifyTeamIndex]]['TeamLogoURL'])
                dlg.exec_()
                teamID = self.team_ID[ModifyTeamIndex]
                teamName = dlg.teamName
                teamLogoURL = dlg.logoURL
                isOk = dlg.isOk

                if isOk:
                    strInfo = 'ID : ' + teamID + '\n팀 이름 : ' + teamName + '\n로고 URL : ' + teamLogoURL
                    reply = QMessageBox.question(self, '팀 수정', '정말로 DB에 팀을 수정하시겠습니까?\n\n' + strInfo,
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        DevUtd_FireBase_DB.UpdateTeamData(teamID, 'TeamName', teamName)
                        DevUtd_FireBase_DB.UpdateTeamData(teamID, 'TeamLogoURL', teamLogoURL)
                        self.UpdateDetailVersion()
                        DevUtd_FireBase_DB.LoadFireBaseDB()
                        self.readTeamInfos()
                        self.initTeamInfoTable()
            else:
                QMessageBox.about(self, '팀 수정', '잘못된 인덱스 입니다.')

    def initStadiumInfoTable(self):
        self.stadiumTableWidget.setRowCount(0)
        RowCount = len(self.stadium_ID)
        self.stadiumTableWidget.setRowCount(RowCount)
        for i in range(RowCount):
            if len(self.stadium_ID) <= i:
                break
            self.stadiumTableWidget.setItem(i, 0, QTableWidgetItem(self.stadium_ID[i]))
            self.stadiumTableWidget.setItem(i, 1, QTableWidgetItem(self.stadiumInfos[self.stadium_ID[i]]['StadiumName']))
            self.stadiumTableWidget.setItem(i, 2, QTableWidgetItem(self.stadiumInfos[self.stadium_ID[i]]['TMap']))
            self.stadiumTableWidget.setItem(i, 3, QTableWidgetItem(self.stadiumInfos[self.stadium_ID[i]]['Kakao']))
            self.stadiumTableWidget.setItem(i, 4, QTableWidgetItem(self.stadiumInfos[self.stadium_ID[i]]['Naver']))
            self.stadiumTableWidget.setItem(i, 5, QTableWidgetItem(self.stadiumInfos[self.stadium_ID[i]]['Address']))

    def make_stadiumAddTab(self):
        tab = QWidget()

        groupBox = QGroupBox("구장 정보")
        self.stadiumAddBtn = QPushButton('구장 추가', self)
        self.stadiumAddBtn.clicked.connect(self.stadiumAddBtn_clicked)
        self.stadiumRemoveBtn = QPushButton('구장 삭제', self)
        self.stadiumRemoveBtn.clicked.connect(self.stadiumRemoveBtn_clicked)
        self.stadiumModifyStartBtn = QPushButton('구장 수정', self)
        self.stadiumModifyStartBtn.clicked.connect(self.stadiumModifyStartBtn_clicked)

        RowCount = len(self.stadium_ID)
        ColumnCount = 6
        self.stadiumTableWidget = QTableWidget(RowCount, ColumnCount)
        self.stadiumTableWidget.setHorizontalHeaderLabels(["ID", "구장 이름", "TMap URL", "카카오 내비 URL", "네이버 지도 URL", "주소"])
        self.stadiumTableWidget.resizeColumnsToContents()
        self.stadiumTableWidget.resizeRowsToContents()
        self.stadiumTableWidget.horizontalHeader().setStretchLastSection(True)
        #self.stadiumTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.stadiumTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.stadiumTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.stadiumTableWidget.setStyleSheet("QHeaderView::section { color:white; background-color:#3E4040; }")
        self.initStadiumInfoTable()


        leftInnerLayOut = QVBoxLayout()
        leftInnerLayOut.addWidget(self.stadiumAddBtn)
        leftInnerLayOut.addWidget(self.stadiumRemoveBtn)
        leftInnerLayOut.addWidget(self.stadiumModifyStartBtn)
        leftInnerLayOut.addStretch(3)
        groupBox.setLayout(leftInnerLayOut)

        leftLayOut = QVBoxLayout()
        leftLayOut.addWidget(groupBox)

        rightLayOut = QVBoxLayout()
        rightLayOut.addWidget(self.stadiumTableWidget)

        layout = QHBoxLayout()
        layout.addLayout(leftLayOut)
        layout.addLayout(rightLayOut)

        tab.setLayout(layout)
        tab.setEnabled(False)
        return tab

    def stadiumAddBtn_clicked(self):
        print("stadiumAddBtn_clicked 클릭")
        btn = self.sender()

        dlg = StadiumDialog()
        dlg.exec_()
        stadiumID = dlg.id
        stadiumName = dlg.stadiumName
        TMapURL = dlg.TMapURL
        KakaoURL = dlg.KakaoURL
        NaverMapURL = dlg.NaverMapURL
        Address = dlg.Address
        isOk = dlg.isOk

        if stadiumID == '' or stadiumName == '':
            QMessageBox.about(self, '구장 추가', '잘못된 입력 입니다.')
            return

        if isOk:
            strInfo = 'ID : ' + stadiumID + '\n구장 이름 : ' + stadiumName
            reply = QMessageBox.question(self, '구장 추가', '정말로 DB에 구장을 추가하시겠습니까?\n\n' + strInfo,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                DevUtd_FireBase_DB.UpdateStadiumData(stadiumID, 'StadiumName', stadiumName)
                DevUtd_FireBase_DB.UpdateStadiumData(stadiumID, 'TMap', TMapURL)
                DevUtd_FireBase_DB.UpdateStadiumData(stadiumID, 'Kakao', KakaoURL)
                DevUtd_FireBase_DB.UpdateStadiumData(stadiumID, 'Naver', NaverMapURL)
                DevUtd_FireBase_DB.UpdateStadiumData(stadiumID, 'Address', Address)

                self.UpdateDetailVersion()
                DevUtd_FireBase_DB.LoadFireBaseDB()
                self.readStadiumInfos()
                self.initStadiumInfoTable()

    def stadiumRemoveBtn_clicked(self):
        print("stadiumRemoveBtn_clicked 클릭")
        btn = self.sender()

        removeStadiumIndex, ok = QInputDialog.getInt(self, '구장 삭제', '삭제할 구장의 Index 번호를 입력하세요.')
        removeStadiumIndex = removeStadiumIndex - 1
        if ok:
            if len(self.stadium_ID) >= removeStadiumIndex and removeStadiumIndex >= 0:
                strInfo = 'ID : ' + self.stadium_ID[removeStadiumIndex] + '\n구장 이름 : ' + self.stadiumInfos[self.stadium_ID[removeStadiumIndex]]['StadiumName']
                reply = QMessageBox.question(self, '구장 삭제', '정말로 DB에서 구장을 삭제하시겠습니까?\n\n' + strInfo,
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    DevUtd_FireBase_DB.RemoveStadiumData(self.stadium_ID[removeStadiumIndex])

                    self.UpdateDetailVersion()
                    DevUtd_FireBase_DB.LoadFireBaseDB()
                    self.readStadiumInfos()
                    self.initStadiumInfoTable()
            else:
                QMessageBox.about(self, '구장 삭제', '잘못된 인덱스 입니다.')

    def stadiumModifyStartBtn_clicked(self):
        print("stadiumModifyStartBtn_clicked 클릭")
        btn = self.sender()

        ModifyStadiumIndex, ok = QInputDialog.getInt(self, '구장 수정', '수정할 구장의 Index 번호를 입력하세요.')
        ModifyStadiumIndex = ModifyStadiumIndex - 1
        if ok:
            if len(self.stadium_ID) >= ModifyStadiumIndex and ModifyStadiumIndex >= 0:
                dlg = StadiumDialog()
                dlg.modifyMode(self.stadium_ID[ModifyStadiumIndex], self.stadiumInfos[self.stadium_ID[ModifyStadiumIndex]]['StadiumName'],
                               self.stadiumInfos[self.stadium_ID[ModifyStadiumIndex]]['TMap'],
                               self.stadiumInfos[self.stadium_ID[ModifyStadiumIndex]]['Kakao'],
                               self.stadiumInfos[self.stadium_ID[ModifyStadiumIndex]]['Naver'],
                               self.stadiumInfos[self.stadium_ID[ModifyStadiumIndex]]['Address'])
                dlg.exec_()
                stadiumID = self.stadium_ID[ModifyStadiumIndex]
                stadiumName = dlg.stadiumName
                TMapURL = dlg.TMapURL
                KakaoURL = dlg.KakaoURL
                NaverMapURL = dlg.NaverMapURL
                Address = dlg.Address
                isOk = dlg.isOk

                if isOk:
                    strInfo = 'ID : ' + stadiumID + '\n구장 이름 : ' + stadiumName
                    reply = QMessageBox.question(self, '구장 수정', '정말로 DB에 구장을 수정하시겠습니까?\n\n' + strInfo,
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        DevUtd_FireBase_DB.UpdateStadiumData(stadiumID, 'StadiumName', stadiumName)
                        DevUtd_FireBase_DB.UpdateStadiumData(stadiumID, 'TMap', TMapURL)
                        DevUtd_FireBase_DB.UpdateStadiumData(stadiumID, 'Kakao', KakaoURL)
                        DevUtd_FireBase_DB.UpdateStadiumData(stadiumID, 'Naver', NaverMapURL)
                        DevUtd_FireBase_DB.UpdateStadiumData(stadiumID, 'Address', Address)

                        self.UpdateDetailVersion()
                        DevUtd_FireBase_DB.LoadFireBaseDB()
                        self.readStadiumInfos()
                        self.initStadiumInfoTable()
            else:
                QMessageBox.about(self, '구장 수정', '잘못된 인덱스 입니다.')

    def initPlayerInfoTable(self):
        self.playerTableWidget.setRowCount(0)
        RowCount = len(self.player_ID)
        self.playerTableWidget.setRowCount(RowCount)
        for i in range(RowCount):
            if len(self.player_ID) <= i:
                break
            self.playerTableWidget.setItem(i, 0, QTableWidgetItem(self.player_ID[i]))
            self.playerTableWidget.setItem(i, 1, QTableWidgetItem(self.playerInfos[self.player_ID[i]]['PlayerName']))
            self.playerTableWidget.setItem(i, 2, QTableWidgetItem(self.playerInfos[self.player_ID[i]]['TeamName']))
            self.playerTableWidget.setItem(i, 3, QTableWidgetItem(self.playerInfos[self.player_ID[i]]['PictureURL']))
            self.playerTableWidget.setItem(i, 4, QTableWidgetItem(str(self.playerInfos[self.player_ID[i]]['MvpNum'])))
            self.playerTableWidget.setItem(i, 5, QTableWidgetItem(str(self.playerInfos[self.player_ID[i]]['TopScorerNum'])))
            self.playerTableWidget.setItem(i, 6, QTableWidgetItem(str(self.playerInfos[self.player_ID[i]]['TopAssistNum'])))
            self.playerTableWidget.setItem(i, 7, QTableWidgetItem(str(self.playerInfos[self.player_ID[i]]['TopAttendanceNum'])))
            self.playerTableWidget.setItem(i, 8, QTableWidgetItem(str(self.playerInfos[self.player_ID[i]]['TopPointNum'])))
            self.playerTableWidget.setItem(i, 9, QTableWidgetItem(str(self.playerInfos[self.player_ID[i]]['TopDefenceNum'])))


    def make_playerAddTab(self):
        tab = QWidget()

        groupBox = QGroupBox("플레이어 정보")
        self.playerAddBtn = QPushButton('플레이어 추가', self)
        self.playerAddBtn.clicked.connect(self.playerAddBtn_clicked)
        self.playerRemoveBtn = QPushButton('플레이어 삭제', self)
        self.playerRemoveBtn.clicked.connect(self.playerRemoveBtn_clicked)
        self.playerModifyStartBtn = QPushButton('플레이어 수정', self)
        self.playerModifyStartBtn.clicked.connect(self.playerModifyStartBtn_clicked)

        RowCount = len(self.player_ID)
        ColumnCount = 10
        self.playerTableWidget = QTableWidget(RowCount, ColumnCount)
        self.playerTableWidget.setHorizontalHeaderLabels(["ID", "플레이어 이름", "소속팀", "사진 URL", "MVP 횟수",
                                                          "득점왕 횟수", "도움왕 횟수", "출석왕 횟수", "공격 포인트왕 횟수", "수비왕 횟수"])
        self.playerTableWidget.resizeColumnsToContents()
        self.playerTableWidget.resizeRowsToContents()
        self.playerTableWidget.horizontalHeader().setStretchLastSection(True)
        self.playerTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.playerTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.playerTableWidget.setStyleSheet("QHeaderView::section { color:white; background-color:#3E4040; }")
        self.initPlayerInfoTable()

        leftInnerLayOut = QVBoxLayout()
        leftInnerLayOut.addWidget(self.playerAddBtn)
        leftInnerLayOut.addWidget(self.playerRemoveBtn)
        leftInnerLayOut.addWidget(self.playerModifyStartBtn)
        leftInnerLayOut.addStretch(3)
        groupBox.setLayout(leftInnerLayOut)

        leftLayOut = QVBoxLayout()
        leftLayOut.addWidget(groupBox)

        rightLayOut = QVBoxLayout()
        rightLayOut.addWidget(self.playerTableWidget)

        layout = QHBoxLayout()
        layout.addLayout(leftLayOut)
        layout.addLayout(rightLayOut)

        tab.setLayout(layout)
        tab.setEnabled(False)

        return tab

    def playerAddBtn_clicked(self):
        print("playerAddBtn_clicked 클릭")
        btn = self.sender()

        dlg = PlayerDialog()
        dlg.setupUI(self.team_ID)
        dlg.exec_()
        playerId = dlg.id
        playerName = dlg.playerName
        teamName = dlg.teamName
        pictureURL = dlg.pictureURL
        mvpNum = dlg.mvpNum
        goalKingNum = dlg.goalKingNum
        assistKingNum = dlg.assistKingNum
        attendanceKingNum = dlg.attendanceKingNum
        pointKingNum = dlg.pointKingNum
        defenceKingNum = dlg.defenceKingNum
        isOk = dlg.isOk

        if playerId == '' or playerName == '' or teamName == '' or mvpNum == '' or goalKingNum == '' or assistKingNum == '':
            QMessageBox.about(self, '플레이어 추가', '잘못된 입력 입니다.')
            return

        if isOk:
            strInfo = 'ID : ' + playerId + '\n플레이어 이름 : ' + playerName + '\n소속팀 : ' + teamName + \
                      '\n사진 URL : ' + pictureURL + '\nMVP 횟수 : ' + mvpNum + '\n득점왕 횟수 : ' + goalKingNum + \
                      '\n도움왕 횟수 : ' + assistKingNum + '\n출석왕 횟수 : ' + attendanceKingNum + '\n공격 포인트왕 횟수 : ' + pointKingNum + '\n수비왕 횟수 : ' + defenceKingNum
            reply = QMessageBox.question(self, '플레이어 추가', '정말로 DB에 플레이어를 추가하시겠습니까?\n\n' + strInfo,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'PlayerName', playerName)
                DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TeamName', teamName)
                DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'PictureURL', pictureURL)
                DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'MvpNum', int(mvpNum))
                DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TopScorerNum', int(goalKingNum))
                DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TopAssistNum', int(assistKingNum))
                DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TopAttendanceNum', int(attendanceKingNum))
                DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TopPointNum', int(pointKingNum))
                DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TopDefenceNum', int(defenceKingNum))

                self.UpdateDetailVersion()
                DevUtd_FireBase_DB.LoadFireBaseDB()
                self.readPlayerInfos()
                self.initPlayerInfoTable()

    def playerRemoveBtn_clicked(self):
        print("playerRemoveBtn_clicked 클릭")
        btn = self.sender()

        removePlayerIndex, ok = QInputDialog.getInt(self, '플레이어 삭제', '삭제할 플레이어의 Index 번호를 입력하세요.')
        removePlayerIndex = removePlayerIndex - 1
        if ok:
            if len(self.player_ID) >= removePlayerIndex and removePlayerIndex >= 0:
                strInfo = 'ID : ' + self.player_ID[removePlayerIndex] + '\n플레이어 이름 : ' + self.playerInfos[self.player_ID[removePlayerIndex]]['PlayerName']
                reply = QMessageBox.question(self, '플레이어 삭제', '정말로 DB에서 플레이어를 삭제하시겠습니까?\n\n' + strInfo,
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    DevUtd_FireBase_DB.RemovePlayerData(self.player_ID[removePlayerIndex])
                    self.UpdateDetailVersion()
                    DevUtd_FireBase_DB.LoadFireBaseDB()
                    self.readPlayerInfos()
                    self.initPlayerInfoTable()
                    print(str(removePlayerIndex))
            else:
                QMessageBox.about(self, '플레이어 삭제', '잘못된 인덱스 입니다.')

    def playerModifyStartBtn_clicked(self):
        print("playerModifyStartBtn_clicked 클릭")
        btn = self.sender()

        ModifyPlayerIndex, ok = QInputDialog.getInt(self, '플레이어 수정', '수정할 플레이어의 Index 번호를 입력하세요.')
        ModifyPlayerIndex = ModifyPlayerIndex - 1
        if ok:
            if len(self.player_ID) >= ModifyPlayerIndex and ModifyPlayerIndex >= 0:
                dlg = PlayerDialog()
                dlg.setupUI(self.team_ID)
                dlg.modifyMode(self.player_ID[ModifyPlayerIndex], self.playerInfos[self.player_ID[ModifyPlayerIndex]]['PlayerName'],
                               self.playerInfos[self.player_ID[ModifyPlayerIndex]]['TeamName'], self.playerInfos[self.player_ID[ModifyPlayerIndex]]['PictureURL'],
                               self.playerInfos[self.player_ID[ModifyPlayerIndex]]['MvpNum'], self.playerInfos[self.player_ID[ModifyPlayerIndex]]['TopScorerNum'],
                               self.playerInfos[self.player_ID[ModifyPlayerIndex]]['TopAssistNum'], self.playerInfos[self.player_ID[ModifyPlayerIndex]]['TopAttendanceNum'],
                               self.playerInfos[self.player_ID[ModifyPlayerIndex]]['TopPointNum'], self.playerInfos[self.player_ID[ModifyPlayerIndex]]['TopDefenceNum'])
                dlg.exec_()
                playerId = self.player_ID[ModifyPlayerIndex]
                playerName = dlg.playerName
                teamName = dlg.teamName
                pictureURL = dlg.pictureURL
                mvpNum = dlg.mvpNum
                goalKingNum = dlg.goalKingNum
                assistKingNum = dlg.assistKingNum
                attendanceKingNum = dlg.attendanceKingNum
                pointKingNum = dlg.pointKingNum
                defenceKingNum = dlg.defenceKingNum
                isOk = dlg.isOk

                if isOk:
                    strInfo = 'ID : ' + playerId + '\n플레이어 이름 : ' + playerName + '\n소속팀 : ' + teamName + \
                              '\n사진 URL : ' + pictureURL + '\nMVP 횟수 : ' + mvpNum + '\n득점왕 횟수 : ' + goalKingNum + \
                              '\n도움왕 횟수 : ' + assistKingNum+ '\n출석왕 횟수 : ' + attendanceKingNum + '\n공격 포인트왕 횟수 : ' + pointKingNum + '\n수비왕 횟수 : ' + defenceKingNum
                    reply = QMessageBox.question(self, '플레이어 수정', '정말로 DB에 플레이어를 수정하시겠습니까?\n\n' + strInfo,
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'PlayerName', playerName)
                        DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TeamName', teamName)
                        DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'PictureURL', pictureURL)
                        DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'MvpNum', int(mvpNum))
                        DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TopScorerNum', int(goalKingNum))
                        DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TopAssistNum', int(assistKingNum))
                        DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TopAttendanceNum', int(attendanceKingNum))
                        DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TopPointNum', int(pointKingNum))
                        DevUtd_FireBase_DB.UpdatePlayerData(playerId, 'TopDefenceNum', int(defenceKingNum))

                        self.UpdateDetailVersion()
                        DevUtd_FireBase_DB.LoadFireBaseDB()
                        self.readPlayerInfos()
                        self.initPlayerInfoTable()
            else:
                QMessageBox.about(self, '플레이어 수정', '잘못된 인덱스 입니다.')

    def initMatchInfoTable(self):
        self.matchTableWidget.setRowCount(0)
        RowCount = len(self.match_ID)
        self.matchTableWidget.setRowCount(RowCount)
        for i in range(RowCount):
            if len(self.match_ID) <= i:
                break

            self.matchTableWidget.setItem(i, 0, QTableWidgetItem(self.match_ID[i]))
            self.matchTableWidget.setItem(i, 1, QTableWidgetItem(self.matchInfos[self.match_ID[i]]['MatchDate']))
            self.matchTableWidget.setItem(i, 2, QTableWidgetItem(self.matchInfos[self.match_ID[i]]['MatchTime']))
            if self.matchInfos[self.match_ID[i]]['MatchType'] == 0:
                self.matchTableWidget.setItem(i, 3, QTableWidgetItem('A매치'))
            else:
                self.matchTableWidget.setItem(i, 3, QTableWidgetItem('자체전'))
            if self.matchInfos[self.match_ID[i]]['InfoType'] == 0:
                self.matchTableWidget.setItem(i, 4, QTableWidgetItem('경기 전'))
            else:
                self.matchTableWidget.setItem(i, 4, QTableWidgetItem('경기 종료'))
            self.matchTableWidget.setItem(i, 5, QTableWidgetItem(self.matchInfos[self.match_ID[i]]['Comment']))
            self.matchTableWidget.setItem(i, 6, QTableWidgetItem(self.matchInfos[self.match_ID[i]]['HomeTeamName']))
            self.matchTableWidget.setItem(i, 7, QTableWidgetItem(self.matchInfos[self.match_ID[i]]['AwayTeamName']))
            self.matchTableWidget.setItem(i, 8, QTableWidgetItem(str(self.matchInfos[self.match_ID[i]]['HomeGoal'])))
            self.matchTableWidget.setItem(i, 9, QTableWidgetItem(str(self.matchInfos[self.match_ID[i]]['AwayGoal'])))

            if 'HomeGoalInfo' in self.matchInfos[self.match_ID[i]]:
                cbHomeGoal = QComboBox(self)
                for homeGoal in self.matchInfos[self.match_ID[i]]['HomeGoalInfo']:
                    if homeGoal:
                        cbHomeGoal.addItem(homeGoal['Name'])
                self.matchTableWidget.setCellWidget(i, 10, cbHomeGoal)

            if 'AwayGoalInfo' in self.matchInfos[self.match_ID[i]]:
                cbAwayGoal = QComboBox(self)
                for awayyGoal in self.matchInfos[self.match_ID[i]]['AwayGoalInfo']:
                    if awayyGoal:
                        cbAwayGoal.addItem(awayyGoal['Name'])
                self.matchTableWidget.setCellWidget(i, 11, cbAwayGoal)

            if 'HomeAssistInfo' in self.matchInfos[self.match_ID[i]]:
                cbHomeAssist = QComboBox(self)
                for homeAssist in self.matchInfos[self.match_ID[i]]['HomeAssistInfo']:
                    if homeAssist:
                        cbHomeAssist.addItem(homeAssist['Name'])
                self.matchTableWidget.setCellWidget(i, 12, cbHomeAssist)

            if 'AwayAssistInfo' in self.matchInfos[self.match_ID[i]]:
                cbAwayAssist = QComboBox(self)
                for awayAssist in self.matchInfos[self.match_ID[i]]['AwayAssistInfo']:
                    if awayAssist:
                        cbAwayAssist.addItem(awayAssist['Name'])
                self.matchTableWidget.setCellWidget(i, 13, cbAwayAssist)

            if 'HomePlayerInfo' in self.matchInfos[self.match_ID[i]]:
                cbHomePlayer = QComboBox(self)
                for homePlayer in self.matchInfos[self.match_ID[i]]['HomePlayerInfo']:
                    if homePlayer:
                        cbHomePlayer.addItem(homePlayer['Name'])
                self.matchTableWidget.setCellWidget(i, 14, cbHomePlayer)

            if 'AwayPlayerInfo' in self.matchInfos[self.match_ID[i]]:
                cbAwayPlayer = QComboBox(self)
                for awayPlayer in self.matchInfos[self.match_ID[i]]['AwayPlayerInfo']:
                    if awayPlayer:
                        cbAwayPlayer.addItem(awayPlayer['Name'])
                self.matchTableWidget.setCellWidget(i, 15, cbAwayPlayer)

    def make_matchAddTab(self):
        tab = QWidget()

        groupBox = QGroupBox("경기 정보")
        self.matchAddBtn = QPushButton('경기 추가', self)
        self.matchAddBtn.clicked.connect(self.matchAddBtn_clicked)
        self.matchRemoveBtn = QPushButton('경기 삭제', self)
        self.matchRemoveBtn.clicked.connect(self.matchRemoveBtn_clicked)
        self.matchModifyBtn = QPushButton('경기 수정', self)
        self.matchModifyBtn.clicked.connect(self.matchModifyBtn_clicked)

        RowCount = len(self.match_ID)
        ColumnCount = 16
        self.matchTableWidget = QTableWidget(RowCount, ColumnCount)
        self.matchTableWidget.setHorizontalHeaderLabels(["ID", "날짜", "시간", "경기타입", "정보타입",
                                                          "구장", "홈팀", "원정팀", "홈골", "원정골", "홈 득점자", "원정 득점자",
                                                         "홈 도움", "원정 도움", "홈팀 인원", "원정팀 인원"])
        self.matchTableWidget.resizeColumnsToContents()
        self.matchTableWidget.resizeRowsToContents()
        self.matchTableWidget.horizontalHeader().setStretchLastSection(True)
        self.matchTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.matchTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.matchTableWidget.setStyleSheet("QHeaderView::section { color:white; background-color:#3E4040; }")
        self.initMatchInfoTable()

        leftInnerLayOut = QVBoxLayout()
        leftInnerLayOut.addWidget(self.matchAddBtn)
        leftInnerLayOut.addWidget(self.matchRemoveBtn)
        leftInnerLayOut.addWidget(self.matchModifyBtn)
        leftInnerLayOut.addStretch(3)
        groupBox.setLayout(leftInnerLayOut)

        leftLayOut = QVBoxLayout()
        leftLayOut.addWidget(groupBox)

        rightLayOut = QVBoxLayout()
        rightLayOut.addWidget(self.matchTableWidget)

        layout = QHBoxLayout()
        layout.addLayout(leftLayOut)
        layout.addLayout(rightLayOut)

        tab.setLayout(layout)
        tab.setEnabled(False)

        return tab

    def matchAddBtn_clicked(self):
        print("matchAddBtn_clicked 클릭")
        btn = self.sender()

        dlg = MatchDialog()
        dlg.setupUI(self.team_ID, self.player_ID, self.stadium_ID)
        dlg.exec_()
        isOk = dlg.isOk
        if isOk:
            matchId = dlg.id
            matchDate = dlg.matchDate
            matchTime = dlg.matchTime
            if dlg.matchType == 'A매치':
                matchType = 0
            else:
                matchType = 1
            if dlg.infoType == '경기 전':
                infoType = 0
            else:
                infoType = 1
            comment = dlg.comment
            homeTeamName = dlg.homeTeamName
            awayTeamName = dlg.awayTeamName
            homeGoal = int(dlg.homeGoal)
            awayGoal = int(dlg.awayGoal)
            homeGoalInfo = dlg.homeGoalInfo
            awayGoalInfo = dlg.awayGoalInfo
            homeAssistInfo = dlg.homeAssistInfo
            awayAssistInfo = dlg.awayAssistInfo
            homePlayerInfo = dlg.homePlayerInfo
            awayPlayerInfo = dlg.awayPlayerInfo
            if matchId == '' or matchDate == '' or matchTime == '' or comment == '':
                QMessageBox.about(self, '경기 추가', '잘못된 입력 입니다.')
                return

            if isOk:
                strInfo = 'ID : ' + matchId + '\n날짜 : ' + matchDate + '\n시간 : ' + matchTime + \
                          '\n홈팀 : ' + homeTeamName + '\n원정팀 : ' + awayTeamName
                reply = QMessageBox.question(self, '경기 추가', '정말로 DB에 경기를 추가하시겠습니까?\n\n' + strInfo,
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    DevUtd_FireBase_DB.UpdateMatchData(matchId, 'MatchDate', matchDate)
                    DevUtd_FireBase_DB.UpdateMatchData(matchId, 'MatchTime', matchTime)
                    DevUtd_FireBase_DB.UpdateMatchData(matchId, 'MatchType', matchType)
                    DevUtd_FireBase_DB.UpdateMatchData(matchId, 'InfoType', infoType)
                    DevUtd_FireBase_DB.UpdateMatchData(matchId, 'Comment', comment)
                    DevUtd_FireBase_DB.UpdateMatchData(matchId, 'HomeTeamName', homeTeamName)
                    DevUtd_FireBase_DB.UpdateMatchData(matchId, 'AwayTeamName', awayTeamName)
                    DevUtd_FireBase_DB.UpdateMatchData(matchId, 'HomeGoal', homeGoal)
                    DevUtd_FireBase_DB.UpdateMatchData(matchId, 'AwayGoal', awayGoal)

                    homeIndex = 1
                    for homeGoalData in homeGoalInfo:
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'HomeGoalInfo/' + str(homeIndex) + '/Name',homeGoalData)
                        homeIndex += 1

                    awayIndex = 1
                    for awayGoalData in awayGoalInfo:
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'AwayGoalInfo/' + str(awayIndex) + '/Name', awayGoalData)
                        awayIndex += 1

                    homeIndex = 1
                    for homeAssist in homeAssistInfo:
                        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'HomeAssistInfo/' + str(homeIndex) + '/Name', homeAssist)
                        homeIndex += 1

                    awayIndex = 1
                    for awayAssist in awayAssistInfo:
                        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'AwayAssistInfo/' + str(awayIndex) + '/Name', awayAssist)
                        awayIndex += 1

                    homeIndex = 1
                    for homePlayer in homePlayerInfo:
                        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'HomePlayerInfo/' + str(homeIndex) + '/Name', homePlayer)
                        homeIndex += 1

                    awayIndex = 1
                    for awayPlayer in awayPlayerInfo:
                        DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'AwayPlayerInfo/' + str(awayIndex) + '/Name', awayPlayer)
                        awayIndex += 1

                    self.UpdateDetailVersion()
                    DevUtd_FireBase_DB.LoadFireBaseDB()
                    self.readMatchInfos()
                    self.initMatchInfoTable()

    def matchRemoveBtn_clicked(self):
        print("matchRemoveBtn_clicked 클릭")
        btn = self.sender()

        removeMatchIndex, ok = QInputDialog.getInt(self, '경기 삭제', '삭제할 경기의 Index 번호를 입력하세요.')
        removeMatchIndex = removeMatchIndex - 1
        if ok:
            if len(self.match_ID) >= removeMatchIndex and removeMatchIndex >= 0:
                strInfo = '날짜 : ' + self.match_ID[removeMatchIndex] + '\n시간 : ' + self.matchInfos[self.match_ID[removeMatchIndex]]['MatchTime'] + \
                          '\n홈팀 : ' + self.matchInfos[self.match_ID[removeMatchIndex]]['HomeTeamName'] + \
                          '\n원정팀 : ' + self.matchInfos[self.match_ID[removeMatchIndex]]['AwayTeamName']
                reply = QMessageBox.question(self, '경기 삭제', '정말로 DB에서 경기를 삭제하시겠습니까?\n\n' + strInfo,
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    DevUtd_FireBase_DB.RemoveMatchData(self.match_ID[removeMatchIndex])

                    self.UpdateDetailVersion()
                    DevUtd_FireBase_DB.LoadFireBaseDB()
                    self.readMatchInfos()
                    self.initMatchInfoTable()
            else:
                QMessageBox.about(self, '플레이어 삭제', '잘못된 인덱스 입니다.')

    def matchModifyBtn_clicked(self):
        print("matchModifyBtn_clicked 클릭")
        btn = self.sender()

        ModifyMatchIndex, ok = QInputDialog.getInt(self, '경기 수정', '수정할 경기 Index 번호를 입력하세요.')
        ModifyMatchIndex = ModifyMatchIndex - 1
        if ok:
            if len(self.match_ID) >= ModifyMatchIndex and ModifyMatchIndex >= 0:
                dlg = MatchDialog()
                dlg.setupUI(self.team_ID, self.player_ID, self.stadium_ID)
                HomeGoalInfo = []
                AwayGoalInfo = []
                HomeAssistInfo = []
                AwayAssistInfo= []
                HomePlayerInfo = []
                AwayPlayerInfo = []
                if 'HomeGoalInfo' in self.matchInfos[self.match_ID[ModifyMatchIndex]]:
                    HomeGoalInfo = self.matchInfos[self.match_ID[ModifyMatchIndex]]['HomeGoalInfo']
                if 'AwayGoalInfo' in self.matchInfos[self.match_ID[ModifyMatchIndex]]:
                    AwayGoalInfo = self.matchInfos[self.match_ID[ModifyMatchIndex]]['AwayGoalInfo']
                if 'HomeAssistInfo' in self.matchInfos[self.match_ID[ModifyMatchIndex]]:
                    HomeAssistInfo = self.matchInfos[self.match_ID[ModifyMatchIndex]]['HomeAssistInfo']
                if 'AwayAssistInfo' in self.matchInfos[self.match_ID[ModifyMatchIndex]]:
                    AwayAssistInfo = self.matchInfos[self.match_ID[ModifyMatchIndex]]['AwayAssistInfo']
                if 'HomePlayerInfo' in self.matchInfos[self.match_ID[ModifyMatchIndex]]:
                    HomePlayerInfo = self.matchInfos[self.match_ID[ModifyMatchIndex]]['HomePlayerInfo']
                if 'AwayPlayerInfo' in self.matchInfos[self.match_ID[ModifyMatchIndex]]:
                    AwayPlayerInfo = self.matchInfos[self.match_ID[ModifyMatchIndex]]['AwayPlayerInfo']

                dlg.modifyMode(self.matchInfos[self.match_ID[ModifyMatchIndex]]['MatchDate'],
                               self.matchInfos[self.match_ID[ModifyMatchIndex]]['MatchTime'], self.matchInfos[self.match_ID[ModifyMatchIndex]]['MatchType'],
                               self.matchInfos[self.match_ID[ModifyMatchIndex]]['InfoType'], self.matchInfos[self.match_ID[ModifyMatchIndex]]['Comment'],
                               self.matchInfos[self.match_ID[ModifyMatchIndex]]['HomeTeamName'], self.matchInfos[self.match_ID[ModifyMatchIndex]]['AwayTeamName'],
                               self.matchInfos[self.match_ID[ModifyMatchIndex]]['HomeGoal'], self.matchInfos[self.match_ID[ModifyMatchIndex]]['AwayGoal'],
                               HomeGoalInfo, AwayGoalInfo, HomeAssistInfo, AwayAssistInfo, HomePlayerInfo, AwayPlayerInfo)
                dlg.exec_()
                isOk = dlg.isOk
                if isOk:
                    matchId = dlg.id
                    matchDate = dlg.matchDate
                    matchTime = dlg.matchTime
                    if dlg.matchType == 'A매치':
                        matchType = 0
                    else:
                        matchType = 1
                    if dlg.infoType == '경기 전':
                        infoType = 0
                    else:
                        infoType = 1
                    comment = dlg.comment
                    homeTeamName = dlg.homeTeamName
                    awayTeamName = dlg.awayTeamName
                    homeGoal = int(dlg.homeGoal)
                    awayGoal = int(dlg.awayGoal)
                    homeGoalInfo = dlg.homeGoalInfo
                    awayGoalInfo = dlg.awayGoalInfo
                    homeAssistInfo = dlg.homeAssistInfo
                    awayAssistInfo = dlg.awayAssistInfo
                    homePlayerInfo = dlg.homePlayerInfo
                    awayPlayerInfo = dlg.awayPlayerInfo
                    strInfo = '날짜 : ' + self.match_ID[ModifyMatchIndex] + '\n시간 : ' + \
                              self.matchInfos[self.match_ID[ModifyMatchIndex]]['MatchTime'] + \
                              '\n홈팀 : ' + self.matchInfos[self.match_ID[ModifyMatchIndex]]['HomeTeamName'] + \
                              '\n원정팀 : ' + self.matchInfos[self.match_ID[ModifyMatchIndex]]['AwayTeamName']
                    reply = QMessageBox.question(self, '경기 수정', '정말로 DB에 경기를 수정하시겠습니까?\n\n' + strInfo,
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'MatchDate', matchDate)
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'MatchTime', matchTime)
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'MatchType', matchType)
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'InfoType', infoType)
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'Comment', comment)
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'HomeTeamName', homeTeamName)
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'AwayTeamName', awayTeamName)
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'HomeGoal', homeGoal)
                        DevUtd_FireBase_DB.UpdateMatchData(matchId, 'AwayGoal', awayGoal)

                        DevUtd_FireBase_DB.RemoveMatchDetailData(matchId, 'HomeGoalInfo')
                        DevUtd_FireBase_DB.RemoveMatchDetailData(matchId, 'AwayGoalInfo')
                        DevUtd_FireBase_DB.RemoveMatchDetailData(matchId, 'HomeAssistInfo')
                        DevUtd_FireBase_DB.RemoveMatchDetailData(matchId, 'AwayAssistInfo')
                        DevUtd_FireBase_DB.RemoveMatchDetailData(matchId, 'HomePlayerInfo')
                        DevUtd_FireBase_DB.RemoveMatchDetailData(matchId, 'AwayPlayerInfo')

                        homeIndex = 1
                        for homeGoalData in homeGoalInfo:
                            DevUtd_FireBase_DB.UpdateMatchData(matchId, 'HomeGoalInfo/' + str(homeIndex) + '/Name',
                                                               homeGoalData)
                            homeIndex += 1

                        awayIndex = 1
                        for awayGoalData in awayGoalInfo:
                            DevUtd_FireBase_DB.UpdateMatchData(matchId, 'AwayGoalInfo/' + str(awayIndex) + '/Name',
                                                               awayGoalData)
                            awayIndex += 1

                        homeIndex = 1
                        for homeAssist in homeAssistInfo:
                            DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'HomeAssistInfo/' + str(homeIndex) + '/Name',
                                                               homeAssist)
                            homeIndex += 1

                        awayIndex = 1
                        for awayAssist in awayAssistInfo:
                            DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'AwayAssistInfo/' + str(awayIndex) + '/Name',
                                                               awayAssist)
                            awayIndex += 1

                        homeIndex = 1
                        for homePlayer in homePlayerInfo:
                            DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'HomePlayerInfo/' + str(homeIndex) + '/Name',
                                                               homePlayer)
                            homeIndex += 1

                        awayIndex = 1
                        for awayPlayer in awayPlayerInfo:
                            DevUtd_FireBase_DB.UpdateMatchData(matchDate, 'AwayPlayerInfo/' + str(awayIndex) + '/Name',
                                                               awayPlayer)
                            awayIndex += 1

                        self.UpdateDetailVersion()
                        DevUtd_FireBase_DB.LoadFireBaseDB()
                        self.readMatchInfos()
                        self.initMatchInfoTable()
            else:
                QMessageBox.about(self, '경기 수정', '잘못된 인덱스 입니다.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DevToolApp()
    sys.exit(app.exec_())