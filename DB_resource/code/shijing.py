# -*- coding: utf-8 -*-

"""
Author:by 王林清 on 2021/11/15 15:54
FileName:shijing.py in shiyizhonghua_resource
Tools:PyCharm python3.8.4
"""

from util import *

if __name__ == '__main__':
    author = {
        'name': '佚名',
        'time': '西周初-春秋中',
        'desc': '《诗经》，是中国古代诗歌开端，最早的一部诗歌总集，收集了西周初年至春秋中叶'
                '（前11世纪至前6世纪）的诗歌，共311篇，其中6篇为笙诗，即只有标题，没有内容，'
                '称为笙诗六篇（《南陔》《白华》《华黍》《由庚》《崇丘》《由仪》），反映了周'
                '初至周晚期约五百年间的社会面貌。《诗经》的作者佚名，绝大部分已经无法考证，'
                '传为尹吉甫采集、孔子编订。《诗经》在先秦时期称为《诗》，或取其整数称'
                '《诗三百》。西汉时被尊为儒家经典，始称《诗经》，并沿用至今。诗经在内容上'
                '分为《风》《雅》《颂》三个部分。《风》是周代各地的歌谣；《雅》是周人的正声'
                '雅乐，又分《小雅》和《大雅》；《颂》是周王庭和贵族宗庙祭祀的乐歌，又分为'
                '《周颂》《鲁颂》和《商颂》。孔子曾概括《诗经》宗旨为“无邪”，并教育弟子读'
                '《诗经》以作为立言、立行的标准。先秦诸子中，引用《诗经》者颇多，如孟子、'
                '荀子、墨子、庄子、韩非子等人在说理论证时，多引述《诗经》中的句子以增强说服'
                '力。至汉武帝时，《诗经》被儒家奉为经典，成为《六经》及《五经》之一。《诗经》'
                '内容丰富，反映了劳动与爱情、战争与徭役、压迫与反抗、风俗与婚姻、祭祖与宴会，'
                '甚至天象、地貌、动物、植物等方方面面，是周代社会生活的一面镜子。'
    }

    datas = []

    data = get_json(r'./../data/shijing/shijing.json')
    for dic in data:
        time = get_time_str()
        datas.append({
            'title': f"{dic['chapter']}·{dic['section']}·{dic['title']}",
            'author': author,
            'type': '诗经',
            'content': dic['content'],
            'create_time': time,
            'update_time': time,
            'valid_delete': True
        })

    save_split_json('shijing', datas)
