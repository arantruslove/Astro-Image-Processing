from modules.background import background

background_dict = {}

background_dict["Region 1"] = background(87,104,452,512)  
background_dict["Region 2"] = background(2077,508,2271,940)
background_dict["Region 3"] =background(127,3059,307,3316)
background_dict["Region 4"] = background(1035,1817,1215,2086)
background_dict["Region 5"]  =background(1327,2107,1474,2314)
background_dict["Region 6"]  = background(2046,1131,2145,1268)
background_dict["Region 7"] = background(2080,1999,2248,2105)
background_dict["Region 8"] = background(1569,3339,1730,3542)
background_dict["Region 9"]=background(2125,2541,2238,2822)
background_dict["Region 10"]= background(1823,3829,2106,3882)
background_dict["Region 11"] = background(485,3936,883,4011)
background_dict["Region 12"]=background(650,4238,1116,4329)

print(background_dict)