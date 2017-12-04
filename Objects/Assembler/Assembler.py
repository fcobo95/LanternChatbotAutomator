from watson_developer_cloud import ConversationV1 as Conversation
from Objects.Workspaces import Workspace
from Objects.DialogNodes import Dialog
from Objects.Entities import Entity, Synonym, Value
from Objects.Intents import Intent, Example
import json


class Assembler:
    """
    DOCSTRING
    """

    def __init__(self, workspace_id=None, username=None, password=None, version=None):
        self.conversation = Conversation(
            username=username,
            password=password,
            version=version
        )
        self.workspace_id = workspace_id
        self.workspaces = Workspace.Workspace(username=username, password=password, version=version)
        self.dialog_nodes = Dialog.Dialog(username=username, password=password, version=version)
        self.entities = Entity.Entity(username=username, password=password, version=version)
        self.synonyms = Synonym.Synonym(username=username, password=password, version=version)
        self.values = Value.Value(username=username, password=password, version=version)
        self.intents = Intent.Intent(username=username, password=password, version=version)
        self.examples = Example.Example(username=username, password=password, version=version)

    def assemble_the_workspace(self):
        intents = self.intents.create_intent()
        print(json.dumps(intents, indent=2))

        entities = self.intents.create_intent()
        print(json.dumps(entities, indent=2))

        dialog_nodes = self.dialog_nodes.create_dialog_node()
        print(json.dumps(dialog_nodes, indent=2))
