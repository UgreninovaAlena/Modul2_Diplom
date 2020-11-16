import json
import os
import shutil

import ForDatabase as db
import ForVK as vk


def find_max_size(photo_size_list):
    photo_size_max = 0
    result_data = {}
    for photo in photo_size_list:
        pixel_count = photo['height'] * photo['width']
        if pixel_count > photo_size_max:
            photo_size_max = pixel_count
            result_data = photo
    return result_data

def get_input_data(filename):
    with open(filename) as f:
        result = json.load(f)
        result['app_id'] = int(result['app_id'])
    return result

def working_with_rubbish_dir(command):
    if command == 'start':
        os.mkdir('rubbish/')
    else:
        shutil.rmtree('rubbish/')

def create_list_undefined_person(person_list):
    general_list = []
    general_list_1 = []

    for photo in photos:
        general_list.append(photo.link_photo)

    count_undef_photo = 3 - len(photos)
    while count_undef_photo > 0:
        general_list.append('https://sun9-39.userapi.com/ltx03LSdkFMbt7_HcV8kdCxmLpek4Lnc2qqm7w/2Pm8T6WbZ7Y.jpg')
        count_undef_photo = count_undef_photo - 1

    return general_list

def searh_undefined_for_vd_person(user, session):
    # db.BASE.metadata.create_all(db.engine)
    # session = db.session
    list_person_from_bd = session.query(db.DatingUser).all()

    users = session.query(db.Photos).all()
    print(users)

# class GetlinkForPhotos():
#     def __init__(self, list_photos_link, VKperson_id):
#         self.cuernt_index = 2
#         self.index = -1
#         self.list_photos_link = list_photos_link
#         self.result_list = list_photos_link[0:3]
#         self.VKperson_id = VKperson_id
#
#     def __iter__(self):
#         return self
#
#     def find_list (self):
#
#         if len(self.list_photos_link) < 3:
#             self.result_list = self.list_photos_link
#         else:
#             self.cuernt_index = self.cuernt_index + 1
#
#             while self.cuernt_index < len(self.list_photos_link):
#                 curent_elem = self.list_photos_link[self.cuernt_index]
#                 if curent_elem['likes']['count'] > self.result_list[0]['likes']['count']:
#                     self.result_list[0] = curent_elem
#                 else:
#                     if curent_elem['likes']['count'] > self.result_list[1]['likes']['count']:
#                         self.result_list[1] = curent_elem
#                     else:
#                         if curent_elem['likes']['count'] > self.result_list[2]['likes']['count']:
#                             self.result_list[2] = curent_elem
#
#                 self.cuernt_index = self.cuernt_index + 1
#
#     def __next__(self):
#         self.find_list()
#         self.index = self.index + 1
#
#         while self.index < len(self.result_list):
#             result_elem = {}
#             result_elem['id'] = self.result_list[self.index]['id']
#             result_elem['owner_id'] = self.result_list[self.index]['owner_id']
#             result_elem['link'] = find_max_size(self.result_list[self.index]['sizes'])
#             result_elem['likes'] = self.result_list[self.index]['likes']['count']
#             return result_elem
#
#         if self.index == 3:
#             raise StopIteration
#         raise StopIteration
