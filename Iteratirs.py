import ForVK
from LibAdditionalFunction import find_max_size


# {'user_likes': 0, 'count': 179},
# {'user_likes': 0, 'count': 179}
# {'user_likes': 0, 'count': 1188}
# {'user_likes': 0, 'count': 104}
# {'user_likes': 0, 'count': 92}
# {'user_likes': 0, 'count': 133}
# {'user_likes': 0, 'count': 568}
#
# test_list = [{'album_id': -6, 'date': 1452257355, 'id': 397379003, 'owner_id': 331709599, 'has_tags': False, 'post_id': 8, 'sizes': [{'height': 93, 'url': 'https://sun9-49.userapi.com/c630331/v630331599/ba8e/Gdaq2I-tH6Y.jpg', 'type': 'm', 'width': 130}, {'height': 93, 'url': 'https://sun9-71.userapi.com/c630331/v630331599/ba90/d6otMwp0rwo.jpg', 'type': 'o', 'width': 130}, {'height': 143, 'url': 'https://sun9-21.userapi.com/c630331/v630331599/ba91/oOjuMoVkNxI.jpg', 'type': 'p', 'width': 200}, {'height': 229, 'url': 'https://sun9-16.userapi.com/c630331/v630331599/ba92/vBk-idyyk9I.jpg', 'type': 'q', 'width': 320}, {'height': 229, 'url': 'https://sun9-71.userapi.com/c630331/v630331599/ba93/TlgKBbXCAko.jpg', 'type': 'r', 'width': 320}, {'height': 54, 'url': 'https://sun9-28.userapi.com/c630331/v630331599/ba8d/D5IAStWo9qg.jpg', 'type': 's', 'width': 75}, {'height': 229, 'url': 'https://sun9-54.userapi.com/c630331/v630331599/ba8f/32feeBHiJ58.jpg', 'type': 'x', 'width': 320}], 'text': '', 'likes': {'user_likes': 0, 'count': 518}, 'reposts': {'count': 0}, 'comments': {'count': 0}, 'can_comment': 0, 'tags': {'count': 0}},
#              {'album_id': -6, 'date': 1491147790, 'id': 456239343, 'owner_id': 331709599, 'has_tags': False, 'post_id': 581, 'sizes': [{'height': 77, 'url': 'https://sun9-38.userapi.com/c637821/v637821599/397d8/QaRz_g9Nufw.jpg', 'type': 'm', 'width': 130}, {'height': 87, 'url': 'https://sun9-13.userapi.com/c637821/v637821599/397dc/D7d2cm2X3KI.jpg', 'type': 'o', 'width': 130}, {'height': 133, 'url': 'https://sun9-74.userapi.com/c637821/v637821599/397dd/C1xZOkawZuE.jpg', 'type': 'p', 'width': 200}, {'height': 213, 'url': 'https://sun9-63.userapi.com/c637821/v637821599/397de/EZGJPckbmvk.jpg', 'type': 'q', 'width': 320}, {'height': 340, 'url': 'https://sun9-9.userapi.com/c637821/v637821599/397df/JWJWNQAv1Sc.jpg', 'type': 'r', 'width': 510}, {'height': 44, 'url': 'https://sun9-37.userapi.com/c637821/v637821599/397d7/u9qvKn4Ji5M.jpg', 'type': 's', 'width': 75}, {'height': 360, 'url': 'https://sun9-39.userapi.com/c637821/v637821599/397d9/9oH4-zfM40M.jpg', 'type': 'x', 'width': 604}, {'height': 481, 'url': 'https://sun9-73.userapi.com/c637821/v637821599/397da/pJ5nzivrXXQ.jpg', 'type': 'y', 'width': 807}, {'height': 516, 'url': 'https://sun9-24.userapi.com/c637821/v637821599/397db/pCVVAw4LNrg.jpg', 'type': 'z', 'width': 866}], 'text': '', 'likes': {'user_likes': 0, 'count': 179}, 'reposts': {'count': 1}, 'comments': {'count': 0}, 'can_comment': 0, 'tags': {'count': 0}},
#              {'album_id': -6, 'date': 1491466385, 'id': 456239382, 'owner_id': 331709599, 'has_tags': False, 'post_id': 592, 'sizes': [{'height': 130, 'url': 'https://sun9-10.userapi.com/c637822/v637822599/43709/CGh5fmmO7v0.jpg', 'type': 'm', 'width': 86}, {'height': 196, 'url': 'https://sun9-76.userapi.com/c637822/v637822599/4370e/RHOqM44WH3c.jpg', 'type': 'o', 'width': 130}, {'height': 302, 'url': 'https://sun9-8.userapi.com/c637822/v637822599/4370f/jpZdc5HpAA8.jpg', 'type': 'p', 'width': 200}, {'height': 483, 'url': 'https://sun9-55.userapi.com/c637822/v637822599/43710/q3Fw2_YsVKo.jpg', 'type': 'q', 'width': 320}, {'height': 770, 'url': 'https://sun9-74.userapi.com/c637822/v637822599/43711/Hoc2bSaI0-Q.jpg', 'type': 'r', 'width': 510}, {'height': 75, 'url': 'https://sun9-67.userapi.com/c637822/v637822599/43708/uqisWMTXrS4.jpg', 'type': 's', 'width': 50}, {'height': 2160, 'url': 'https://sun9-34.userapi.com/c637822/v637822599/4370d/AZ0QHbYzC2I.jpg', 'type': 'w', 'width': 1431}, {'height': 604, 'url': 'https://sun9-18.userapi.com/c637822/v637822599/4370a/qqaE8OcaL4M.jpg', 'type': 'x', 'width': 400}, {'height': 807, 'url': 'https://sun9-28.userapi.com/c637822/v637822599/4370b/zGpkU7PM0yg.jpg', 'type': 'y', 'width': 534}, {'height': 1080, 'url': 'https://sun9-59.userapi.com/c637822/v637822599/4370c/71wEHsxOrWg.jpg', 'type': 'z', 'width': 715}], 'text': '', 'likes': {'user_likes': 0, 'count': 1188}, 'reposts': {'count': 1}, 'comments': {'count': 0}, 'can_comment': 0, 'tags': {'count': 0}},
#              {'album_id': -6, 'date': 1507064769, 'id': 456240418, 'owner_id': 331709599, 'has_tags': False, 'post_id': 1291, 'sizes': [{'height': 130, 'url': 'https://sun9-39.userapi.com/c639431/v639431365/4b238/63aoKhBsVuk.jpg', 'type': 'm', 'width': 97}, {'height': 173, 'url': 'https://sun9-7.userapi.com/c639431/v639431365/4b23d/c0mfmj3y1mE.jpg', 'type': 'o', 'width': 130}, {'height': 267, 'url': 'https://sun9-73.userapi.com/c639431/v639431365/4b23e/as03H2kwKUw.jpg', 'type': 'p', 'width': 200}, {'height': 427, 'url': 'https://sun9-52.userapi.com/c639431/v639431365/4b23f/RhaaCG7exEs.jpg', 'type': 'q', 'width': 320}, {'height': 680, 'url': 'https://sun9-47.userapi.com/c639431/v639431365/4b240/ywfXXbU82Fw.jpg', 'type': 'r', 'width': 510}, {'height': 75, 'url': 'https://sun9-66.userapi.com/c639431/v639431365/4b237/-SGDVpc48Q4.jpg', 'type': 's', 'width': 56}, {'height': 1600, 'url': 'https://sun9-60.userapi.com/c639431/v639431365/4b23c/Khs1vrT142o.jpg', 'type': 'w', 'width': 1200}, {'height': 604, 'url': 'https://sun9-46.userapi.com/c639431/v639431365/4b239/EkaYGOUxOSI.jpg', 'type': 'x', 'width': 453}, {'height': 807, 'url': 'https://sun9-15.userapi.com/c639431/v639431365/4b23a/8q7QEhUaUOI.jpg', 'type': 'y', 'width': 605}, {'height': 1080, 'url': 'https://sun9-37.userapi.com/c639431/v639431365/4b23b/uhVurOtLF8M.jpg', 'type': 'z', 'width': 810}], 'text': '', 'likes': {'user_likes': 0, 'count': 104}, 'reposts': {'count': 0}, 'comments': {'count': 3}, 'can_comment': 0, 'tags': {'count': 0}},
#              {'album_id': -6, 'date': 1513191343, 'id': 456240832, 'owner_id': 331709599, 'has_tags': False, 'post_id': 1468, 'sizes': [{'height': 94, 'url': 'https://sun9-3.userapi.com/c840732/v840732579/30a95/NVatTeaCkxw.jpg', 'type': 'm', 'width': 130}, {'height': 94, 'url': 'https://sun9-66.userapi.com/c840732/v840732579/30a9a/6IbQ7vOIsLo.jpg', 'type': 'o', 'width': 130}, {'height': 145, 'url': 'https://sun9-46.userapi.com/c840732/v840732579/30a9b/j-iGN_8cm4k.jpg', 'type': 'p', 'width': 200}, {'height': 232, 'url': 'https://sun9-72.userapi.com/c840732/v840732579/30a9c/nVYGJE3Pq5c.jpg', 'type': 'q', 'width': 320}, {'height': 369, 'url': 'https://sun9-71.userapi.com/c840732/v840732579/30a9d/mwlDM5OVRT4.jpg', 'type': 'r', 'width': 510}, {'height': 54, 'url': 'https://sun9-45.userapi.com/c840732/v840732579/30a94/SebJZlecg1A.jpg', 'type': 's', 'width': 75}, {'height': 1853, 'url': 'https://sun9-64.userapi.com/c840732/v840732579/30a99/ONhOHs7L5VY.jpg', 'type': 'w', 'width': 2560}, {'height': 437, 'url': 'https://sun9-46.userapi.com/c840732/v840732579/30a96/sk2oyA4lKJo.jpg', 'type': 'x', 'width': 604}, {'height': 584, 'url': 'https://sun9-54.userapi.com/c840732/v840732579/30a97/mrvRP-WtcZk.jpg', 'type': 'y', 'width': 807}, {'height': 926, 'url': 'https://sun9-24.userapi.com/c840732/v840732579/30a98/aTgJ_8zvQIE.jpg', 'type': 'z', 'width': 1280}], 'text': '', 'likes': {'user_likes': 0, 'count': 92}, 'reposts': {'count': 0}, 'comments': {'count': 7}, 'can_comment': 0, 'tags': {'count': 0}},
#              {'album_id': -6, 'date': 1514363640, 'id': 456240882, 'owner_id': 331709599, 'has_tags': False, 'post_id': 1498, 'sizes': [{'height': 130, 'url': 'https://sun9-14.userapi.com/c824202/v824202805/66890/1TuVsMynn1c.jpg', 'type': 'm', 'width': 97}, {'height': 174, 'url': 'https://sun9-49.userapi.com/c824202/v824202805/66892/733JPUs8qdc.jpg', 'type': 'o', 'width': 130}, {'height': 267, 'url': 'https://sun9-75.userapi.com/c824202/v824202805/66893/Qv9tTKkCqFE.jpg', 'type': 'p', 'width': 200}, {'height': 428, 'url': 'https://sun9-68.userapi.com/c824202/v824202805/66894/qttSdm-IZ9k.jpg', 'type': 'q', 'width': 320}, {'height': 600, 'url': 'https://sun9-34.userapi.com/c824202/v824202805/66895/v3dQGzVCg_M.jpg', 'type': 'r', 'width': 449}, {'height': 75, 'url': 'https://sun9-73.userapi.com/c824202/v824202805/6688f/RhyqfqnmZr0.jpg', 'type': 's', 'width': 56}, {'height': 600, 'url': 'https://sun9-38.userapi.com/c824202/v824202805/66891/aY5r6em9Npk.jpg', 'type': 'x', 'width': 449}], 'text': '', 'likes': {'user_likes': 0, 'count': 133}, 'reposts': {'count': 0}, 'comments': {'count': 1}, 'can_comment': 0, 'tags': {'count': 0}},
#              {'album_id': -6, 'date': 1493624272, 'id': 456239583, 'owner_id': 331709599, 'has_tags': False, 'post_id': 682, 'sizes': [{'height': 94, 'url': 'https://sun3-11.userapi.com/c604824/v604824599/3f23d/Q3fVMxcUaVY.jpg', 'type': 'm', 'width': 130}, {'height': 94, 'url': 'https://sun3-13.userapi.com/c604824/v604824599/3f241/NKmX4FinwTY.jpg', 'type': 'o', 'width': 130}, {'height': 145, 'url': 'https://sun3-10.userapi.com/c604824/v604824599/3f242/rQbzl8kCiKs.jpg', 'type': 'p', 'width': 200}, {'height': 232, 'url': 'https://sun3-12.userapi.com/c604824/v604824599/3f243/8rmXc_5zlUg.jpg', 'type': 'q', 'width': 320}, {'height': 369, 'url': 'https://sun3-12.userapi.com/c604824/v604824599/3f244/yBHV_GXikQU.jpg', 'type': 'r', 'width': 510}, {'height': 54, 'url': 'https://sun3-11.userapi.com/c604824/v604824599/3f23c/VdU3tGBbS0w.jpg', 'type': 's', 'width': 75}, {'height': 437, 'url': 'https://sun3-10.userapi.com/c604824/v604824599/3f23e/0smOUSDDZ3g.jpg', 'type': 'x', 'width': 604}, {'height': 584, 'url': 'https://sun3-11.userapi.com/c604824/v604824599/3f23f/JbXjZ3mwDU4.jpg', 'type': 'y', 'width': 807}, {'height': 926, 'url': 'https://sun3-11.userapi.com/c604824/v604824599/3f240/NEDBXFwxV7Y.jpg', 'type': 'z', 'width': 1280}], 'text': '', 'likes': {'user_likes': 0, 'count': 568}, 'reposts': {'count': 2}, 'comments': {'count': 1}, 'can_comment': 0, 'tags': {'count': 0}}]

class GetlinkForPhotos():
    def __init__(self, list_photos_link, VKperson_id):
        self.cuernt_index = 2
        self.index = -1
        self.list_photos_link = list_photos_link
        self.result_list = list_photos_link[0:3]
        self.VKperson_id = VKperson_id

    def __iter__(self):
        return self

    def find_list (self):

        if len(self.list_photos_link) < 3:
            self.result_list = self.list_photos_link
        else:
            self.cuernt_index = self.cuernt_index + 1

            while self.cuernt_index < len(self.list_photos_link):
                curent_elem = self.list_photos_link[self.cuernt_index]
                if curent_elem['likes']['count'] > self.result_list[0]['likes']['count']:
                    self.result_list[0] = curent_elem
                else:
                    if curent_elem['likes']['count'] > self.result_list[1]['likes']['count']:
                        self.result_list[1] = curent_elem
                    else:
                        if curent_elem['likes']['count'] > self.result_list[2]['likes']['count']:
                            self.result_list[2] = curent_elem

                self.cuernt_index = self.cuernt_index + 1

    def __next__(self):
        self.find_list()
        self.index = self.index + 1

        while self.index < len(self.result_list):
            result_elem = {}
            result_elem['id'] = self.result_list[self.index]['id']
            result_elem['owner_id'] = self.result_list[self.index]['owner_id']
            result_elem['link'] = find_max_size(self.result_list[self.index]['sizes'])
            result_elem['likes'] = self.result_list[self.index]['likes']['count']
            return result_elem

        if self.index == 3:
            raise StopIteration
        raise StopIteration


class ListIteration():
    def __init__(self, list):
        self.list = list
        self.curent_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.curent_index < len(self.list) -1:
            self.curent_index = self.curent_index+1

            return self.list[self.curent_index]

        raise StopIteration


# list = [0,1,2,3,4,5,6,7,8,9,10]
# for x in ListIteration(list):
#     print(x)

