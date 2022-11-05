import os
import sys
import requests
import csv
import hashlib as hb
import json
import shutil
from support.randomize_name import randomize

current_directory = os.getcwd()

def download_csv(csv_url, file_name):
	try:
		print("Downloading Data...")
		with requests.Session() as s:
			response = s.get(csv_url)
			# response = requests.get(csv_url)
		try:
			file = open(f"csvfiles/{file_name}.csv", 'w')
			try:
				file.write(response.content.decode('utf-8'))
			except:
				print("Something went wrong when writing to the file")
			finally:
				file.close()
		except:
			print("Something went wrong when opening file")
	except:
		print("An exception occured")


def csv_order_checker(csv_file):
	list_order = []
	checker = True

	for row in csv_file:
		for item in row:
			if "serial" and "name" in item.lower():
				for items in row:
					list_order.append(items)

	if len(list_order) != 7:
		print("\nExpected:\n ['Serial Number', 'Filename', 'Description', 'Gender', 'Attributes', 'UUID', 'HASH']")
		print(f"Got:\n {list_order}")
	else:
		if list_order[0] != "Serial Number":
			print(f"where Expected: 'Serial Number', Got: {list_order[0]}")
			checker = False
		if list_order[1] != "Filename":
			print(f"where Expected: 'Filename', Got: {list_order[1]}")
			checker = False
		if list_order[2] != "Description":
			print(f"where Expected: 'Description', Got: {list_order[2]}")
			checker = False
		if list_order[3] != "Gender":
			print(f"where Expected: 'Gender', Got: {list_order[3]}")
			checker = False
		if list_order[4] != "Attributes":
			print(f"where Expected: 'Attributes', Got: {list_order[4]}")
			checker = False
		if list_order[5] != "UUID":
			print(f"where Expected: 'UUID', Got: {list_order[5]}")
			checker = False
		if list_order[6] != "HASH":
			print(f"where Expected: 'HASH', Got: {list_order[6]}")
			checker = False
	
	print("\nExpected:\n ['Serial Number', 'Filename', 'Description', 'Gender', 'Attributes', 'UUID', 'HASH']")
	if checker:
		print(f"Got Right Format:\n {list_order}")
	else:
		print(f"Got Wrong Format:\n {list_order}")
	return checker

def cs_json_generator(file_path):
	# Initialize array for all nft items in their json
	people_information = []

	# Check if csv is in required format
	with open(file_path) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		checker_value = csv_order_checker(csv_reader)
		csv_file.close()
		if not checker_value:
			sys.exit()

	initial_csv_info_header = []
	initial_csv_info_data = []

	# go through csv file and generate json for all
	# nft item information
	with open(file_path) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if "Serial Number" in row or "Filename" in row:
				initial_csv_info_header.append(row)
				if "serial" in row[0].lower() and "name" in row[1].lower():
					pass
			else:
				initial_csv_info_data.append(row)
				if row[1] != "" and row[2] != "":
					people_information.append({
						"format": "CHIP-0007",
						"name": row[1],
						"description": row[2],
						"minting_tool": "SuperMinter/2.5.2",
						"sensitive_content": False,
						"series_number": row[0],
						"series_total": 1000,
						"attributes": [
							{
								"trait_type": "Species",
								"value": "Mouse"
							},
							{
								"trait_type": "Color",
								"value": "Yellow"
							},
							{
								"trait_type": "Friendship",
								"value": 50,
								"min_value": 0,
								"max_value": 255
							}
						],
						"collection": {
							"name": "Example Pokémon Collection",
							"id": row[5],
							"attributes": [
								{
									"type": "description",
									"value": "Example Pokémon Collection is the best Pokémon collection. Get yours today!"
								},
								{
									"type": "icon",
									"value": "https://examplepokemoncollection.com/image/icon.png"
								},
								{
									"type": "banner",
									"value": "https://examplepokemoncollection.com/image/banner.png"
								},
								{
									"type": "twitter",
									"value": "ExamplePokemonCollection"
								},
								{
									"type": "website",
									"value": "https://examplepokemoncollection.com/"
								}
							]
						},
						"data": {
							"example_data": ""
						}
					})
				line_count += 1
		csv_file.close()

	# count number of generated json files for nft items
	people_count = 0
	
	# initialize hash list for each hash
	hash_list = []

	path_2_check = f'{current_directory}/jsonfiles'
	if os.path.exists(path_2_check):
		pass
	else:
		os.makedirs(path_2_check)

	for people in people_information:
		json_formatted_str = json.dumps(people, indent=2)

		# Seperate generated nft in json format to 
		# different json files
		with open(f'{current_directory}/jsonfiles/chip-0007_compatible_json_{people_count}.json', 'w', encoding='utf-8') as new_file:
			new_file.write(json_formatted_str + '\n')
			new_file.close()

		# get hash of each generated nft json file
		# and append to list
		with open(f'{current_directory}/jsonfiles/chip-0007_compatible_json_{people_count}.json', mode='rb') as file:
			file_content = file.read()
			file.close()
		hash_ = hb.sha256(file_content).hexdigest()
		hash_list.append(hash_)

		people_count += 1

	# initialize csv list for nft items with
	# their hashes
	full_csv_list = []
	for i in range(len(initial_csv_info_data)):
		current_list = []
		current_list.append(initial_csv_info_data[i][0])
		current_list.append(initial_csv_info_data[i][1].replace(" ", ""))
		current_list.append(initial_csv_info_data[i][2])
		current_list.append(initial_csv_info_data[i][3])
		current_list.append("")
		current_list.append(initial_csv_info_data[i][5])
		current_list.append(hash_list[i])
		full_csv_list.append(current_list)

	csv_header = initial_csv_info_header[0]

	return csv_header, full_csv_list

def csv_output_generator(csv_header, json_format):
	jsonObject = json_format

	print("")
	filename = input("Enter name for output csv file. e.g preferredname.output.csv: ")
	with open(f'{current_directory}/output/{filename}.output.csv', 'w') as output_file:
		writer = csv.writer(output_file)

		# write the header
		writer.writerow(csv_header)

		# write the data
		writer.writerows(jsonObject)
	print(f"csv file created at 'output/{filename}.output.csv'")


def nft_csv_hash_generator():
	print("NFT CSV HASH Generator....")
	print("Author: Ukanah Dean")
	print("Github Repo: https://github.com/Harrylever/Chip-0007-maker.git/")
	print("See Readme File for usage or type 'help'\n")
	print("\t1. Choose CSV file from local storage")
	print("\t2. Download CSV file from online")

	option_ = str(input(":"))
	csv_new_name = randomize()
	if option_ == "1":
		csv_file_path = input("Enter csv file absolute path.\ne.g\t'C:/users/david/Desktop/NewFolder/data.csv'\n\t'/home/david/Desktop/NewFolder/data.csv'\n\n:")
		shutil.copy2(csv_file_path, f"{current_directory}/csvfiles/{csv_new_name}.csv")
	elif option_ == "2":
		url_path = input("Enter file url: ")
		download_csv(url_path, csv_new_name)
	else:
		print("Invalid response!")
		sys.exit()

	csv_header, full_csv_list = cs_json_generator(f"{current_directory}/csvfiles/{csv_new_name}.csv")
	
	# Generate Final CSV of all nfts with their Chip-0007
	# compatible json hash
	csv_output_generator(csv_header=csv_header, json_format=full_csv_list)


if __name__ == "__main__":
	nft_csv_hash_generator()