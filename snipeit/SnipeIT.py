from Accessories import Accessories
from Assets import Assets
from Categories import Categories
from Companies import Companies
from Components import Components
from Consumables import Consumables
from Departments import Departments
from Fields import Fields
from Licenses import Licenses
from Locations import Locations
from Maintenances import Maintenances
from Manufacturers import Manufacturers
from Models import Models
from Reports import Reports
from StatusLabels import StatusLabels
from Users import Users

class SnipeIT():
    def __init__(self, server, token):
        self.server = server
        self.token = token
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.token
        }

        self.accessories = Accessories(self.server, self.headers)
        self.assets = Assets(self.server, self.headers)
        self.categories = Categories(self.server, self.headers)
        self.companies = Companies(self.server, self.headers)
        self.components = Components(self.server, self.headers)
        self.consumables = Consumables(self.server, self.headers)
        self.departments = Departments(self.server, self.headers)
        self.fields = Fields(self.server, self.headers)
        self.licenses = Licenses(self.server, self.headers)
        self.locations = Locations(self.server, self.headers)
        self.maintenances = Maintenances(self.server, self.headers)
        self.manufacturers = Manufacturers(self.server, self.headers)
        self.models = Models(self.server, self.headers)
        self.reports = Reports(self.server, self.headers)
        self.status_labels = StatusLabels(self.server, self.headers)
        self.users = Users(self.server, self.headers)
        