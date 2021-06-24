import STSGui
import Status 
import queryRunner
import dbImporter

class DBtool:

	def __init__(self):
		self.status = Status()
		self.Qr = queryRunner()
		self.dbi = dbImporter()
		self.gui = STSGui()

if __name__ == "__main__":
	DBtool()
