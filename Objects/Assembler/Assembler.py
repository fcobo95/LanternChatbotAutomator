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
        # Loads all the required data from the AppSettings.json file.
        app_setting_directory = '../../Data/AppSettings/AppSettings.json'
        csv_directory = '../../Data/CSVFiles/MainCSV.csv'
        self.readTheCSV = theCSV.ReaderCSV(csv_directory).final_csv_data
        self.readTheJSON = theJSON.ReaderJSON(app_setting_directory).final_json_data
        self.theUserName = self.readTheJSON['username']
        self.thePassword = self.readTheJSON['password']
        self.theVersion = self.readTheJSON['version']
        self.theWorkspaceID = self.readTheJSON['workspace_id']

        # Creates a new instance of the Conversation V1 object.
        self.theConversation = Conversation(username=self.theUserName, password=self.thePassword,
                                            version=self.theVersion)

        # We initialize all necessary objects to be able to assemble the initial workspace.
        self.workspace_id = self.theWorkspaceID
        self.workspaces = Workspace.Workspace(self.theUserName, self.thePassword, self.theVersion)
        self.dialog_nodes = Dialog.Dialog(self.theUserName, self.thePassword, self.theVersion)
        self.entities = Entity.Entity(self.theUserName, self.thePassword, self.theVersion)
        self.synonyms = Synonym.Synonym(self.theUserName, self.thePassword, self.theVersion)
        self.values = Value.Value(self.theUserName, self.thePassword, self.theVersion)
        self.intents = Intent.Intent(self.theUserName, self.thePassword, self.theVersion)
        self.examples = Example.Example(self.theUserName, self.thePassword, self.theVersion)

    def assemble_the_workspace(self):
        theIntents = self.readTheCSV['Intents']
        theExamples = self.readTheCSV['Examples']

        theWorkspaceIntents = theIntents
        theIntentExamples = theExamples

        theIntentsArray = []
        theExamplesArray = []
        theCounter = 0
        for intent in theWorkspaceIntents:

            theIntentsArray.append(intent)
            theClientExamples = self.readTheCSV['Examples']
            if theClientExamples.count() > 0:
                theCustomExamples = theClientExamples.at[theCounter]
                theCounter += 1
                each_custom_intent = str(theCustomExamples)
                if not each_custom_intent == "nan":
                    theQuestionsArray = each_custom_intent.split(";")
                    for each_example in theQuestionsArray:
                        theCustomExampleIntent = {
                            "text": each_example}
                        theExamplesArray.append(theCustomExampleIntent)
                        print(theExamplesArray)
                else:
                    print("There are NO client custom examples for this intent {}.".format(intent))
            else:
                print("Well, there are some that have, others don't.")

        # for each_val in theIntents:
        #     self.intents.create_intent(workspace_id=self.workspace_id, intent=each_val,
        #                                examples=theExamplesArray)
        #     theCounter += 1


theAssembler = Assembler()
theAssembler.assemble_the_workspace()
