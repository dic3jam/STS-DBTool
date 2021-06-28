import tkinter as Tk


class STSGui:
	def __init__(self, root):
		"""
		root - Tkinter object
		Builds the GUI 
		"""
		self.root = root
		root.title("STS-DBTool") 
		preSetFrame = self.makePreSetFrame(self.root)
		customQueryFrame = self.makeCustomQueryFrame(self.root)
		importStatusFrame = self.makeImportStatusFrame(self.root)
		preSetFrame.pack()
		customQueryFrame.pack()
		importStatusFrame.pack()

	def makePreSetFrame(self, root): 
		# TODO write makePreSetFrame
		# TODO write tests for makePreSetFrame
		"""
		Constructs the first frame of the GUI consisting of
		radio button selections for pre-set queries, an execute to 
		.csv button, and execute to excel button

		root - the root Tkinter object

		returns - Tkinter.Frame with items attached and packed
		"""		
		F = Tk.Frame(root)
		label = Tk.Label(F, text="frame1")
		label.pack()
		return F

	def makeCustomQueryFrame(self, root): 
		# TODO write makeCustomQueryFrame
		# TODO write tests for makeCustomQueryFrame
		"""
		Constructs the custom query section with a textbox input for 
		SQL, an eexcute to .csv button, and am execute to excel button

		root - the root Tkinter object

		returns - Tkinter.Frame with items attached and packed
		"""
		F = Tk.Frame(root)
		label = Tk.Label(F, text="frame2")
		label.pack()
		return F
	
	def makeImportStatusFrame(self, root): 
		# TODO write makeImportStatusFrame
		# TODO write tests for makeImportStatusFrame
		"""
		Constructs the frame with the import database button, 
		and the current status display

		root - the root Tkinter object

		returns - Tkinter.Frame with items attached and packed
		"""
		F = Tk.Frame(root)
		label = Tk.Label(F, text="frame3")
		label.pack()
		return F

	def updateStatus(self, statusCode):
		# TODO write updateStatus
		# TODO write tests for updateStatus
		"""
		Updates the status bar

		statusCode - string to display
		"""
		return self

	def attachQueryToButton(self, button, query):
		# TODO write attachQueryToButton
		# TODO write tests for attachQueryToButton
		"""
		Called from the DBTool class - used to attach a query
		from the pre-built queries dict (instance variable of query
		Runner class )
		"""
		return self

	def attachFunctionToButton(self, button, func):
		# TODO write attachFunctionToButton
		# TODO write tests for attachFunctionToButton
		"""
		Called from the DBTool class - used to attach
		a function to a STSGUI button
		"""
		return self

	def getInputQuery():
		# TODO write getInputQuery
		# TODO write tests for getInputQuery
		"""
		Returns the text currently in the input query field
		
		returns - String of the text
		"""
		return
	

if __name__ == "__main__":
	root = Tk.Tk()
	dbTool = STSGui(root)
	root.mainloop()