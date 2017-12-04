from watson_developer_cloud import ConversationV1 as Conversation
from Objects.Workspaces import Workspace
from Objects.DialogNodes import Dialog
from Objects.Entities import Entity, Synonym, Value
from Objects.Intents import Intent, Example
from Objects.Readers import ReaderCSV as theCSV
from Objects.Readers import ReaderJSON as theJSON

import json


class Assembler:
    """
    DOCSTRINGS
    """

    def __init__(self):
        app_setting_directory = '../../Data/AppSettings/AppSettings.json'
        csv_directory = '../../Data/CSVFiles/MainCSV.csv'
        self.readTheCSV = theCSV.ReaderCSV(csv_directory).final_csv_data
        self.readTheJSON = theJSON.ReaderJSON(app_setting_directory).final_json_data
        self.conversation = Conversation(
            username=self.readTheJSON['username'],
            password=self.readTheJSON['password'],
            version=self.readTheJSON['version']
        )
        self.workspace_id = self.readTheJSON['workspace_id']
        self.workspaces = Workspace.Workspace(username=self.readTheJSON['username'],
                                              password=self.readTheJSON['password'],
                                              version=self.readTheJSON['version'])
        self.dialog_nodes = Dialog.Dialog(username=self.readTheJSON['username'], password=self.readTheJSON['password'],
                                          version=self.readTheJSON['version'])
        self.entities = Entity.Entity(username=self.readTheJSON['username'], password=self.readTheJSON['password'],
                                      version=self.readTheJSON['version'])
        self.synonyms = Synonym.Synonym(username=self.readTheJSON['username'], password=self.readTheJSON['password'],
                                        version=self.readTheJSON['version'])
        self.values = Value.Value(username=self.readTheJSON['username'], password=self.readTheJSON['password'],
                                  version=self.readTheJSON['version'])
        self.intents = Intent.Intent(username=self.readTheJSON['username'], password=self.readTheJSON['password'],
                                     version=self.readTheJSON['version'])
        self.examples = Example.Example(username=self.readTheJSON['username'], password=self.readTheJSON['password'],
                                        version=self.readTheJSON['version'])

    def assemble_the_workspace(self):
        intents = self.intents.create_intent()
        print(json.dumps(intents, indent=2))

        entities = self.intents.create_intent()
        print(json.dumps(entities, indent=2))

        dialog_nodes = self.dialog_nodes.create_dialog_node()
        print(json.dumps(dialog_nodes, indent=2))


# theAssembler = Assembler()
# username = theAssembler.readTheJSON['username']
# password = theAssembler.readTheJSON['password']
# version = theAssembler.readTheJSON['version']
# workspace_id = theAssembler.readTheJSON['workspace_id']
# csv_workspace_id = theAssembler.readTheCSV['WorkspaceName'].at[0]
# print(username)
# print(password)
# print(version)
# print(workspace_id)
# print(csv_workspace_id)
