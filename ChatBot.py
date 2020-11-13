from pprint import pprint
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import ForVK as mVK
from LibAdditionalFunction import get_input_data, working_with_rubbish_dir, create_list_photos_to_send


class BOT():
    AOuthData = get_input_data("Data.txt")
    message_dict = {'for_start': 'Я буду отправлять тебе фото людей, которые возможно заинтересуют тебя, а ты будешь отвечать мне, нравится тебе предложеный человек, или нет.\nЕсли ты готов, напиши мне в чате "start":)\nЕсли захочешь закончить диалог, напиши мне в чате "by"',
                    'input_age': 'Ведите возрастной промежуток для поиска в виде "[22-33]"',
                    'input_token': 'Ведите ваш токен в формате "token=XXXXXX...XXX":',
                    'start_search': 'Отлично! Для начала поиска введите "search":',
                    'for_one_VKPerson': 'Если вам нравится кондидат, введите "+", иначе введите "-":',
                    'send_set': 'Я нашла несколько хороших вариантов для тебя:)\nВведите "go" для продолжения',
                    'person_missed': 'Вы не сделали выбор:( \nНаверняка это нехороший человек! Отмеу его как неинтересного',
                    'person_interest_not': f'Пропускаем, не для нас :(',
                    'person_interest': f'Отличный выбор! Добавляем в рекомендации :)',
                    'all_person_is_viewed': 'Вау! Ты просмотрели всех возможных кондидатов!\n Заходи ко мне позже, и я поищу для тебя еще :)'
                    }

    token = input('Token: ')

    def __init__(self):
        self.vk = vk_api.VkApi(token=self.AOuthData['m_token'])
        self.longpoll = VkLongPoll(self.vk)
        self.status_bot = 'started'

    def write_msg(self, user_id, message, attachment = None):
        if attachment == None:
            self.vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})
        else:
            self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), "attachment": attachment})

    # def create_list_photos_to_send(self, photos):
    #     general_list = []
    #
    #     for photo in photos:
    #         general_list.append(photo.link_photo)
    #
    #     count_undef_photo = 3 - len(photos)
    #     while count_undef_photo > 0:
    #         general_list.append('https://sun9-39.userapi.com/ltx03LSdkFMbt7_HcV8kdCxmLpek4Lnc2qqm7w/2Pm8T6WbZ7Y.jpg')
    #         count_undef_photo = count_undef_photo - 1
    #
    #     return general_list

    def send_set(self, event_user_id, person):
        photolist_for_send = create_list_photos_to_send(person.list_photos)

        for x in range(3):
            self.write_msg(event_user_id, '', photolist_for_send[x - 1])
        self.write_msg(event_user_id, f'{person.first_name} {person.last_name} \n{self.message_dict["for_one_VKPerson"]}')

    def chat(self):
        # working_with_rubbish_dir('start')
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:

                if event.to_me:
                    request = event.text.replace(' ', '').lower()

                    if request == "by" or self.status_bot == 'stoped':
                        self.write_msg(event.user_id, "Пока((")

                    elif request == "hi":
                        self.write_msg(event.user_id, f"{self.message_dict['for_start']}, {event.user_id}")
                                # Я буду отправлять тебе фото людей, которые возможно заинтересуют тебя, а ты будешь отвечать мне,
                                # нравится тебе предложеный человек, или нет. Если ты готов, напиши мне в чате "Старт"

                    elif request == "start":
                        self.write_msg(event.user_id, self.message_dict['input_token'])
                                # 'input_token': 'Ведите ваш токен в формате "token=XXXXXX...XXX":'}

                    elif request.find('token=') != -1:
                        self.token = request[6:]
                        self.write_msg(event.user_id, self.message_dict['input_age'])
                                # 'input_age': 'Ведите возрастной промежуток для поиска в виде "[22-33]:"'

                    elif request.find('[') != -1 and request.find('-') != -1 and request.find(']') != -1:
                        char = request.find('-')
                        self.age_from = int(request[1:char])
                        self.age_to = int(request[char+1:len(request)-1])
                        self.write_msg(event.user_id, self.message_dict['start_search'])
                                # 'start_search': 'Отлично! Для начала поиска введите "search"

                    elif request == "search":
                        self.user = mVK.User(event.user_id, self.token, self.age_from, self.age_to)
                        result = self.user.get_infouser()

                        if result.error == 1:
                            self.write_msg(event.user_id, result.massage)
                            self.status_bot = 'stoped'
                        else:
                            VKpersons = mVK.VKperson()
                            result = VKpersons.get_people(self.user, 3, self.AOuthData, self.token)

                            if result.error == 1:
                                self.write_msg(event.user_id, result.massage)
                                self.status_bot = 'stoped'
                            else:

                                for person in self.user.VKperson_list:
                                    photos = mVK.Photo()
                                    result = photos.get_photoslink(person, self.token)
                                    result.print_result()

                                self.current_person_index = -1
                                self.write_msg(event.user_id, self.message_dict['send_set'])

                    elif request == "go":
                        # if self.current_person_index == 0:
                        #     if self.user.VKperson_list[self.current_person_index].interest == None:
                        #         self.user.VKperson_list[self.current_person_index].interest = False
                        #         self.write_msg(event.user_id, self.message_dict['person_missed'])
                        #                 # 'person_missed': 'Вы не сделали выбор:( Наверняка это нехороший человек! Отмеу его как неинтересного'
                        self.current_person_index = self.current_person_index + 1
                        self.send_set(event.user_id, self.user.VKperson_list[self.current_person_index])

                    elif request == "+":
                        if self.current_person_index == len(self.user.VKperson_list)-1:
                            self.write_msg(event.user_id, self.message_dict['all_person_is_viewed'])
                                    # 'all_person_is_viewed': 'Вау! Ты просмотрели всех возможных кондидатов! Заходи ко мне позже, и я поищу для тебя еще :)'
                            self.status_bot = 'stoped'
                        else:
                            self.user.VKperson_list[self.current_person_index].interest = True
                            self.write_msg(event.user_id, self.message_dict['person_interest'])
                                    # 'person_interest': f'Отличный выбор! Добавляем в рекомендации :)'

                            self.current_person_index = self.current_person_index + 1
                            self.send_set(event.user_id, self.user.VKperson_list[self.current_person_index])

                    elif request == "-":
                        if self.current_person_index == len(self.user.VKperson_list)-1:
                            self.write_msg(event.user_id, self.message_dict['all_person_is_viewed'])
                                    # 'all_person_is_viewed': 'Вау! Ты просмотрели всех возможных кондидатов! Заходи ко мне позже, и я поищу для тебя еще :)'
                            self.status_bot = 'stoped'
                        else:
                            self.user.VKperson_list[self.current_person_index].interest = False
                            self.write_msg(event.user_id, self.message_dict['person_interest_not'])
                                    # 'person_interest_not': f'Пропускаем, не для нас :('

                            self.current_person_index = self.current_person_index + 1
                            self.send_set(event.user_id, self.user.VKperson_list[self.current_person_index])

                    else:
                        self.write_msg(event.user_id, "Я тебя не понимаю :(\n Попробуй, пожалуйта, еще раз")


a = BOT()
a.chat()
