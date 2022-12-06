from __future__ import print_function
from pygments import highlight, lexers, formatters
import sys
import json

def jprint(data, sort=True, indent = 4):
	data = json.dumps(data, sort_keys=sort, indent = indent)
	if sys.version_info.major == 3:
		colorful_json = highlight(bytes(data, encoding='UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
	else:
		colorful_json = highlight(unicode(data, 'UTF-8'), lexers.JsonLexer(), formatter.TerminalFormatter())
	print(colorful_json)

if __name__ == '__main__':
	data_test = [{'Status:': {'value': [' Ongoing'], 'links': [], 'time': []}}, {'Network:': {'value': [' Bilibili'], 'links': [{'name': 'Bilibili', 'link': 'https://anichin.vip/network/bilibili/'}], 'time': []}}, {'Studio:': {'value': [' Pb Animation Co. Ltd.'], 'links': [{'name': 'Pb Animation Co. Ltd.', 'link': 'https://anichin.vip/studio/pb-animation-co-ltd/'}], 'time': []}}, {'Tanggal rilis:': {'value': [' Oct 02, 2022'], 'links': [], 'time': []}}, {'Durasi:': {'value': [' 20 min per ep'], 'links': [], 'time': []}}, {'Season:': {'value': [' Fall 2022'], 'links': [{'name': 'Fall 2022', 'link': 'https://anichin.vip/season/fall-2022/'}], 'time': []}}, {'Negara:': {'value': [' China'], 'links': [{'name': 'China', 'link': 'https://anichin.vip/country/china/'}], 'time': []}}, {'Tipe:': {'value': [' Donghua'], 'links': [], 'time': []}}, {'Episode:': {'value': [' 12'], 'links': [], 'time': []}}, {'Diterjemahkan oleh:': {'value': [' Dongdong'], 'links': [], 'time': []}}, {'Diposting oleh:': {'value': [' Dongdong'], 'links': [], 'time': []}}, {'Ditambahkan:': {'value': [' September 30, 2022'], 'links': [], 'time': [{'name': 'September 30, 2022', 'time': '2022-09-30T21:52:13+07:00'}]}}, {'Terakhir diedit:': {'value': [' December 4, 2022'], 'links': [], 'time': [{'name': 'December 4, 2022', 'time': '2022-12-04T14:28:09+07:00'}]}}]
	jprint(data_test)
