
# CHIP-0007-MAKER

A python program for generating Chip-0007 compatible json files from CSV files which also returns the hash of the json files appended to the CSV.




![App Screenshot](https://i.ibb.co/NFtt2jp/Screenshot-2022-11-05-17-43-23.png)


## Installation

Install packages with pip

```bash
  pip install -r requirements.txt
```

## Usage/Examples

For usage of the python script: Run 
```python
python main.py
```

Choose between and csv file on your local machine or one hosted online
> 1 - for local file <br>
2 - for hosted file

### CSV Sample ###
| Serial Number | Filename       | Description                                                                                 | Gender | Attributes | UUID                                 | HASH |
|---------------|----------------|---------------------------------------------------------------------------------------------|--------|------------|--------------------------------------|------|
| 21            | abdul-the-vibe | abdul the life of the party and can never be caught unfresh                                 | Male   | Null       | 770f817a-9d9a-4772-9a91-e66dd9d03470 |      |
| 22            | aminu-maikudi  | aminu is a wealthy man from a family with generational wealth. His exquisite taste shows it | Male   | Null       | 770f817a-9d9a-4772-9a91-e66dd9d03470 |      |
|               |                |                                                                                             |        |            |                                      |      |

Your CSV to be passed should sample the table above.
### Note: If you pass a local file, the absolute path of the file should be passed
e.g. <br> 'C:/users/david/Desktop/NewFolder/data.csv' <br> '/home/david/Desktop/NewFolder/data.csv' 
<br>
<br>
After that you would enter your preferred name for the final output.csv: Such as
___filename.output.csv___
<br>
```
e.g.
data.output.csv
nft_collection.output.csv
prada.output.csv
```
<br>

A simple CSV file meeting the sample csv conditions can be found [here](https://github.com/Harrylever/Chip-0007-maker/blob/main/test/nft_naming_2.csv "NFT NAMING.csv"). Edit it and use to generate others

## Documentation

[Documentation](https://github.com/Harrylever/Chip-0007-maker/blob/main/README.md)


## Authors

- [@Harrylever](https://www.github.com/Harrylever)

