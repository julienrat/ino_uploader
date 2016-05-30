#!/usr/bin/python2
# coding: utf-8 
import pygtk

pygtk.require("2.0")

import gtk
import sys
import os
from os.path import basename



class HelloWorld:

    def __init__(self):
        self.path = "/dev/"
        self.dirs = os.listdir( self.path )
        self.port = ["","","","",""]
        mainWindow = gtk.Window()

        mainWindow.set_title("  Upload Arduino  ")

        mainWindow.connect("destroy", self.on_mainWindow_destroy)


        self.myLabel = gtk.Label("    Televersez le programme a Arduino    ")


        myButton = gtk.Button("Televerser")

        myButton.connect("clicked", self.on_myButton_clicked)
        
        
        self.combo=gtk.combo_box_new_text()
        i=-1
        for file in self.dirs:
			if(file.find("ttyACM")==0 or file.find("ttyUSB")==0 ):
				i+=1
				self.port[i]=file
				self.combo.append_text(self.port[i])
        if (i==-1):
            self.myLabel.set_text("Arduino non detecte!")
        
        self.combo.set_active(0)
        vBox = gtk.VBox()

        vBox.pack_start(self.myLabel)
        vBox.pack_start(self.combo)

        vBox.pack_start(myButton)
        


        mainWindow.add(vBox)

        mainWindow.show_all()


    def on_mainWindow_destroy(self, widget):

        gtk.main_quit()


    def on_myButton_clicked(self, widget):

        
        modele = self.combo.get_model()
        index = self.combo.get_active()
        if (index != -1) :
			self.myLabel.set_text("Envoyé !")
			print("/dev/"+self.port[index])
			#print(os.path.dirname(os.path.realpath(str(sys.argv[1]))))
			chemin_sketch=str(sys.argv[1])[0:len(str(sys.argv[1]))-4]
			print(chemin_sketch)
			print(basename(chemin_sketch))
			os.system('mkdir '+ chemin_sketch)
			os.system('mv '+str(sys.argv[1])+' '+ chemin_sketch)
			
			#print (str(sys.argv[1]))
			os.system('arduino --upload --port /dev/'+self.port[index]+'  '+chemin_sketch+"/"+basename(chemin_sketch)+'.ino')
		
			
        


if __name__ == "__main__":

    HelloWorld()

    gtk.main()

