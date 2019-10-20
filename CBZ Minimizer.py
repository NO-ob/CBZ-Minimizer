import sys, os

res = input("Resize Percentage: ")
for x in sys.argv[1:]:
	os.system("mkdir tmp")
	os.system("unzip \"" + x +"\" -d tmp")	
	os.system("mogrify -verbose -resize "+res+ "% tmp/*")	
	os.system("zip -r \"" + x.split(".")[0]+"\"_min.cbz tmp/")
	os.system("rm tmp/*")

os.system("rm -rf tmp/")