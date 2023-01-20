import json
import uuid
import os

name = input("(No Spaces) Skin pack name: ")
if not os.path.exists(name):
  os.makedirs(name+"/"+name+"/texts")
manifest = {
  "format_version":1,
  "header":
  {
    "name":name,
    "uuid":f"{uuid.uuid4()}",
    "version":
    [
      1,0,0
    ]
  },
  "modules":[
    {
      "type":"skin_pack",
      "uuid":f"{uuid.uuid4()}",
      "version":
      [
        1,0,0
      ]
    }
  ]
}
json_object = json.dumps(manifest, indent=4)
with open(name+"/"+name+"/manifest.json", "w") as file:
	file.write(json_object)
### ^ MANIFEST ^ ###

skins = {
  "skins":
  [
  ],
  "serialize_name":name,
  "localization_name":name
}

answer = int(input("amount of skins: "))
i = 0
while i < answer:
  i = i+1
  skins["skins"].append({
        "localization_name":"skin"+str(i),
        "geometry":"geometry.humonoid.custom",
        "texture":input(f"[Skin#{str(i)}] Skin file name: "),
      })
  while True:
    cape = input("Will this skin have a cape (y/n): ")
    if cape == "y":
      skins["skins"][i-1].update({"cape":input("Cape file name: "), "type":"free"})
      break
    else:
      if cape == "n":
        break
      else: 
        print("Please type 'y' for yes,\nand 'n' for no.")
    skins["skins"][i-1].update({"type":"free"})
json_object = json.dumps(skins, indent=4)
with open(name+"/"+name+"/skins.json", "w") as file:
	file.write(json_object)
### ^ SKINS ^ ###

en_US = f"skinpack.{name}="+input("Enter main skin pack name: ")
i = 0
while i < answer:
  i = i+1
  en_US = en_US + "\n"+"skin."+name+".skin"+str(i)+"="+input(f"Name of Skin#{str(i)}: ")
with open(name+"/"+name+"/texts/en_US.lang", "w") as file:
	file.write(en_US)
### ^ EN_US ^ ###

input(f"Make sure to drop your skin .png files in the main folder before continuing! ({name}/{name}/) Press Enter to continue. ")

import zipfile

zip_name = name + '.zip'

with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
  for folder_name, subfolders, filenames in os.walk(name):
    for filename in filenames:
      file_path = os.path.join(folder_name, filename)
      zip_ref.write(file_path, arcname=os.path.relpath(file_path, name))
zip_ref.close()

file = name+'.zip'
base = os.path.splitext(file)[0]
os.rename(file, base + '.mcpack')
### ^ CREATE ARCHIVE ^ ###