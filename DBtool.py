from STSGui import STSGui
#from Status import Status 
#from queryRunner import queryRunner
#from dbImporter import dbImporter
import tkinter as Tk


class DBTool:
	def __init__(self):
		"""
		Constructs the helper classes for running the 
		DBTool
		"""
		self.gui = STSGui()
		#self.status = Status()
		#self.qr = queryRunner()
		#self.dbi = dbImporter()
		#attach queryrunner functions to buttons in gui

	def updateStatus(self, statusCode):
		"""
		Get a status from Status and send to the STSGUI
		status field to display

		statusCode - the index of the status to display

		Updates the status bar of the GUI
		"""
		return 

	def runPreSetQuery(self, preSet, exec):
		"""
		Call on the preset queries dictionary and 
		execute a query

		preSet - the preset query number
		exec - boolean true if open in excel, false if 
		save to .csv

		return - boolean indicating success	
		"""
		# calls sendToCSV or 
		return 

	def runInputQuery(self, query, exec):
		# TODO understand pyodc.cursor exceptions for invalid queries	
		"""
		Execute the current sql statement
		to check that the query is valid

		query - the inputted query
		exec - boolean true if open in excel, false if 
		save to .csv

		return - boolean indicating success	
		"""
		return

	def openInExcel(filename):
		"""
		Once a csv has been outputted from one of the
		query running functions, takes the filename and
		opens the output in excel
		"""	
		return






if __name__ == "__main__":
	root = Tk.Tk()
	dbTool = STSGui(root)
	root.mainloop()

