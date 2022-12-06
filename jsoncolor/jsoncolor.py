from __future__ import print_function
from pygments import highlight, lexers, formatters
import sys
import json
import argparse
import clipboard

def jprint(data, sort=True, indent = 4):
	if sort == None: sort = True
	data = json.dumps(data, sort_keys=sort, indent = indent)
	if sys.version_info.major == 3:
		colorful_json = highlight(bytes(data, encoding='UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
	else:
		colorful_json = highlight(unicode(data, 'UTF-8'), lexers.JsonLexer(), formatter.TerminalFormatter())
	print(colorful_json)

def usage(text = None):
	parser = argparse.ArgumentParser(prog="jprint")
	parser.add_argument('TEXT', action = 'store', help = 'Text print to or type "c" to get text from clipboard')
	parser.add_argument('-s', '--sort', action = 'store_true', help = 'Sort output (default)')
	parser.add_argument('-ns', '--no-sort', action = 'store_false', help = 'Don\'t Sort output')
	parser.add_argument('-i', '--indent', help = 'Indent size, defalt = 4', action = 'store', default = 4, type = int)
	if len(sys.argv) == 1:
		if text:
			jprint(text)
		else:
			parser.print_help()
	else:
		args = parser.parse_args()
		data = args.TEXT
		if args.TEXT == 'c':
			data = clipboard.paste()
		if text: data = text
		if args.sort: sort = True
		if args.no_sort: sort = False
		jprint(data, sort, args.indent)

if __name__ == '__main__':
	data_test = [{'Status:': {'value': [' Ongoing'], 'links': [], 'time': []}}, {'Network:': {'value': [' Bilibili'], 'links': [{'name': 'Bilibili', 'link': 'https://anichin.vip/network/bilibili/'}], 'time': []}}, {'Studio:': {'value': [' Pb Animation Co. Ltd.'], 'links': [{'name': 'Pb Animation Co. Ltd.', 'link': 'https://anichin.vip/studio/pb-animation-co-ltd/'}], 'time': []}}, {'Tanggal rilis:': {'value': [' Oct 02, 2022'], 'links': [], 'time': []}}, {'Durasi:': {'value': [' 20 min per ep'], 'links': [], 'time': []}}, {'Season:': {'value': [' Fall 2022'], 'links': [{'name': 'Fall 2022', 'link': 'https://anichin.vip/season/fall-2022/'}], 'time': []}}, {'Negara:': {'value': [' China'], 'links': [{'name': 'China', 'link': 'https://anichin.vip/country/china/'}], 'time': []}}, {'Tipe:': {'value': [' Donghua'], 'links': [], 'time': []}}, {'Episode:': {'value': [' 12'], 'links': [], 'time': []}}, {'Diterjemahkan oleh:': {'value': [' Dongdong'], 'links': [], 'time': []}}, {'Diposting oleh:': {'value': [' Dongdong'], 'links': [], 'time': []}}, {'Ditambahkan:': {'value': [' September 30, 2022'], 'links': [], 'time': [{'name': 'September 30, 2022', 'time': '2022-09-30T21:52:13+07:00'}]}}, {'Terakhir diedit:': {'value': [' December 4, 2022'], 'links': [], 'time': [{'name': 'December 4, 2022', 'time': '2022-12-04T14:28:09+07:00'}]}}]
	usage(data_test)
