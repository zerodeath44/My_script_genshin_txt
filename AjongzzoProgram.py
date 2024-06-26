import json
'''
Created by (JONGZZO)
FB: https://www.facebook.com/Jongzo?mibextid=ZbWKwL
Redit:https://www.reddit.com/u/Any-Kangaroo3831?utm_medium=android_app&utm_source=share

1 Here is the shortened source code. cannot handle exceptions. If you get an exception. Message me on Reddit

2. The file you want to convert (.json) must be in the same directory as the source file (.py).

3. If the json file is not in the same directory as the file py, please provide the full path. '/' -> '//'

Ex: //storage//emulated//0//Download//Senbonzakura.genshinsheet.json
'''
ListNote = [15, 16, 17, 18, 19, 20, 21, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7]
Listtembo = ['', ' l', ' j', ' h', ' g', ' g l', ' f', ' f l', ' d', ' d l', ' d j', ' d h', ' s', ' s l', ' s j', ' s h', ' a']

def ReadJson(file):
    Data = json.load(file)
    if type(Data) == list: Data = Data[0]
    if Data['type'] != 'composed': 
        print('Only "Composed" type is supported')
        return None, None, None
    else:
        Name = Data['name']
        Bpm = Data['bpm']//4
        Columns = Data['columns']
        Script = ""
        
        count = 1
        for col in Columns:
            if col[1] == []: count += 1
            else:
                while count>16:
                    Script += Listtembo[16]
                    count -= 16
                Script += Listtembo[count]
                count = 1
                for note in col[1]:
                    Script += ' ' + str(ListNote[note[0]])
    return Name, Bpm, Script

print("Enter the path to the Json file")
path = input('>>>')
with open(path, 'r') as fileInp:
    Name, Bpm, Script = ReadJson(fileInp)
    path = path.split('.')
    with open(path[0]+'.txt', 'w') as fileOut:
        fileOut.write(str(Name) + ' BPM:' + str(Bpm) +' ||' + Script)
        print('---> Done')