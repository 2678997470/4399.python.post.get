import requests
import hashlib
uid = ""
print("4399游戏存档获取 调用了requests库 与hashlib 接口源萌新 技术指导萌新")
for i in range(210000000):
    pd = input('是否更换uid  y or n')
    if "y" == pd:
        username = input("请输入账号(不输入账号即可输入uid)：")
        if "" == username:
            print('请输入uid')
            uid = input(":")
        else:
            print('获取uid中')
            uid = requests.get("http://cz.4399.com/get_role_info.php?ac=cuid&uname=" + username)
            uid = uid.text
    else:
        if uid == "":
            username = input("uid为空 请输入账号或UID ：")
            if "" == username:
                print('请输入uid')
                uid = input(":")
            else:
                print('获取uid中')
                uid = requests.get("http://cz.4399.com/get_role_info.php?ac=cuid&uname=" + username)
                uid = uid.text
        print(uid)
        print(
            "西游大战僵尸2：21366’\r\n’超合金战记3：18385’\r\n’西游战记3：26403’\r\n’武将风云录1：29249’\r\n’武将风云录2：31999’\r\n’武将风云录3：49278’\r\n’爆枪英雄1：27788’\r\n’爆枪英雄2：51229’\r\n’西游灭妖传：41191’\r\n’造梦西游3:15389’\r\n’造梦西游2:：11634’\r\n’造梦西游1:10418’\r\n’萌战前线：54881’\r\n’火线风暴：28337’\r\n’机甲小子：25235’\r\n’机甲小子2:41113’\r\n’彩虹王国：22580’\r\n’梦幻三国：15899’\r\n’三国小镇：14728’\r\n’勇士的信仰：16523’\r\n’国王的勇士5:38964国王的勇士6：51855’\r\n’快打僵尸：49245’\r\n’魔城奇兵：40523’\r\n’封神太:1：16364’\r\n’封神太子2：19596’\r\n’封神太子外传2：25039’\r\n’伟大航线：19296’\r\n’造梦江湖1：23042’\r\n’造梦江湖2:21992")
        gameid = "1000" + input("请输入游戏id")
        # ---------------------gamekey获取------------------------------------------
        gamekey = gameid + "LPislKLodlLKKOSNlSDOAADLKADJAOADALAklsd" + gameid
        ssr = gamekey
        # 创建md5对象
        hl = hashlib.md5()  # 第一次加密
        hl.update(ssr.encode("utf-8"))
        ssr = hl.hexdigest()  # 第二次加密
        hl = hashlib.md5()
        hl.update(ssr.encode("utf-8"))
        gamekey = hl.hexdigest()  # 4     1            16     12
        print(gamekey[4:20])
        gamekey = gamekey[4:20]  # daac   c3127a8e0c278090  8e4ea2e76184         5, 16
        for i in range(9):
            # print(i)
            index = str(i)
            print("游戏id" + gameid + "游戏存档位置" + index)
            # ---------------------生成verify------------------------------------------
            verify = "SDALPlsldlnSLWPElsdslSE" + index + gamekey + uid + gameid + "PKslsO"
            ssr = verify
            # 创建md5对象
            hl = hashlib.md5()  # 第一次加密
            # 更新hash对象的值，如果不使用update方法也可以直接md5构造函数内填写
            # md5_obj=hashlib.md5("123456".encode("utf-8")) 效果一样
            hl.update(ssr.encode("utf-8"))
            ssr = hl.hexdigest()  # 第二次加密
            hl = hashlib.md5()
            hl.update(ssr.encode("utf-8"))
            ssr = hl.hexdigest()  # 第3次加密
            hl = hashlib.md5()
            hl.update(ssr.encode("utf-8"))
            verify = hl.hexdigest()
            # ------------------------------存档获取------------------------------------
            # print("游戏的verify：" + verify)
            molianps = {
                "uid": uid,
                "gameid": gameid,
                "gamekey": gamekey,
                "index": index,
                "session": "",
                "verify": verify
            }
            # print(molianps)
            获取 = "https://save.api.4399.com/ranging.php/?ac=get"
            cd获取 = requests.post(获取, molianps)
            if cd获取.text != "":
                print(cd获取.json())