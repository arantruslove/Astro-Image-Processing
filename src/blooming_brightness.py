from modules.crop import centre_crop as crop
from modules.max_value import max_value

crop(1469,336,11,10,"../figures/fits/final_cropped.fits","../figures/blooming/non1.fits")
crop(1668,159,9,7,"../figures/fits/final_cropped.fits","../figures/blooming/non2.fits")
crop(1643,448,13,14,"../figures/fits/final_cropped.fits","../figures/blooming/yes1.fits")
crop(1959,1298,16,44,"../figures/fits/final_cropped.fits","../figures/blooming/yes2.fits")
crop(1801,1434,11,9,"../figures/fits/final_cropped.fits","../figures/blooming/non3.fits")
crop(2003,2180,16,40,"../figures/fits/final_cropped.fits","../figures/blooming/non4.fits")
crop(2005,3630,20,72,"../figures/fits/final_cropped.fits","../figures/blooming/yes3.fits")
crop(2149,3718,8,8,"../figures/fits/final_cropped.fits","../figures/blooming/non5.fits")
crop(2131,3168,4,5,"../figures/fits/final_cropped.fits","../figures/blooming/non6.fits")
crop(1307,3101,168,286,"../figures/fits/final_cropped.fits","../figures/blooming/yes4.fits")
crop(1288,2850,10,16,"../figures/fits/final_cropped.fits","../figures/blooming/yes5.fits")
crop(1327,3903,12,30,"../figures/fits/final_cropped.fits","../figures/blooming/yes6.fits")
crop(1236,4200,8,8,"../figures/fits/final_cropped.fits","../figures/blooming/yes7.fits")
crop(1183,4268,11,8,"../figures/fits/final_cropped.fits","../figures/blooming/yes8.fits")
crop(429,3967,23,23,"../figures/fits/final_cropped.fits","../figures/blooming/yes9.fits")
crop(448,4186,8,5,"../figures/fits/final_cropped.fits","../figures/blooming/non7.fits")
crop(645,3189,23,190,"../figures/fits/final_cropped.fits","../figures/blooming/yes10.fits")
crop(766,3244,6,6,"../figures/fits/final_cropped.fits","../figures/blooming/non8.fits")
crop(726,3076,6,8,"../figures/fits/final_cropped.fits","../figures/blooming/non9.fits")
crop(842,2645,20,103,"../figures/fits/final_cropped.fits","../figures/blooming/yes11.fits")
crop(772,2158,20,109,"../figures/fits/final_cropped.fits","../figures/blooming/yes12.fits")
crop(574,2133,8,8,"../figures/fits/final_cropped.fits","../figures/blooming/non10.fits")
crop(317,2171,5,9,"../figures/fits/final_cropped.fits","../figures/blooming/yes13.fits")
crop(232,2300,5,7,"../figures/fits/final_cropped.fits","../figures/blooming/non11.fits")
crop(547,1808,20,20,"../figures/fits/final_cropped.fits","../figures/blooming/non12.fits")
crop(837,1524,20,20,"../figures/fits/final_cropped.fits","../figures/blooming/non13.fits")
crop(506,1366,20,20,"../figures/fits/final_cropped.fits","../figures/blooming/non14.fits")

files_non = ["../figures/blooming/non1.fits","../figures/blooming/non2.fits",
             "../figures/blooming/non3.fits","../figures/blooming/non4.fits",
             "../figures/blooming/non5.fits","../figures/blooming/non6.fits",
             "../figures/blooming/non7.fits","../figures/blooming/non8.fits",
             "../figures/blooming/non9.fits","../figures/blooming/non10.fits",
             "../figures/blooming/non11.fits","../figures/blooming/non12.fits",
             "../figures/blooming/non13.fits","../figures/blooming/non14.fits"]
files_yes = ["../figures/blooming/yes1.fits","../figures/blooming/yes2.fits",
             "../figures/blooming/yes3.fits","../figures/blooming/yes4.fits",
             "../figures/blooming/yes5.fits","../figures/blooming/yes6.fits",
             "../figures/blooming/yes7.fits","../figures/blooming/yes8.fits",
             "../figures/blooming/yes9.fits","../figures/blooming/yes10.fits",
             "../figures/blooming/yes11.fits","../figures/blooming/yes12.fits",
             "../figures/blooming/yes13.fits"]

max_yes = []
max_non = []
for file in files_non:
    max_non.append(max_value(file))
for file in files_yes:
    max_yes.append(max_value(file))
print(max_yes)
print(max_non)