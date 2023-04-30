from Graph_Equations import * 
def getimage():
 	imagepixels , image=openimage("gaunter_o_dimm.jpg")
 	return imagepixels 
 	
def main():
 	pixels=getimage()
 	showimage(pixels)
 	
main()