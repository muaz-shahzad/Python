import re

pattern = r"[A-Z]+he"

text = '''
A bicycle, also called a pedal cycle, bike, push-bike or cycle, is a human-powered or motor-powered assisted, pedal-driven, single-track vehicle, having two wheels attached to a frame, one behind the other. A bicycle rider is called a cyclist, or bicyclist.
Bicycles were introduced in the 19th century in Europe. By the early 21st century there were more than 1 billion.[1][2][3] These numbers far exceed the number of cars, both in total and ranked by the number of individual models produced.[4][5][6] They are the principal means of transportation in many regions. They also provide a popular form of recreation, and have been adapted for use as children's toys, general fitness, military and police applications, courier services, bicycle racing, and bicycle stunts.
The basic shape and configuration of a typical upright or "safety bicycle", has changed little since the first chain-driven model was developed around 1885.[7][8][9] However, many details have been improved, especially since the advent of modern materials and computer-aided design. These have allowed for a proliferation of specialized designs for many types of cycling. In the 21st century electric bicycles have become popular.
The bicycle's invention has had an enormous effect on society, both in terms of culture and of advancing modern industrial methods. Several components that played a key role in the development of the automobile were initially invented for use in the bicycle, including ball bearings, pneumatic tires, chain-driven sprockets and tension-spoked wheels.[10]
'''

match = re.search(pattern,text) #find first occurence

matches = re.finditer(pattern,text)

for matche in matches:
    print("\n")
    print(matche)
    print(matche.span())
    print(type(matche.span()))
    # print(matche.span()[0])
    # print(matche.span()[1])
    print(text[matche.span()[0]:matche.span()[1]])