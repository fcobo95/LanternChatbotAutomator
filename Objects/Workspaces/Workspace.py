from watson_developer_cloud import ConversationV1 as Conversation
import json


class Workspace:
    """
    DOCSTRING
    """

    def __init__(self, username=None, password=None, version=None):
        self.conversation = Conversation(
            username=username,
            password=password,
            version=version
        )

    def list_all_workspaces(self, page_limit=None, include_count=None, sort=None, cursor=None):
        response = self.conversation.list_workspaces(
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor
        )
        print(json.dumps(response, indent=2))

    def create_workspace(self, name, description=None, language=None, intents=None, entities=None, dialog_nodes=None,
                         counterexamples=None, metadata=None, learning_opt_out=None):
        response = self.conversation.create_workspace(
            name=name,
            description=description,
            language=language,
            intents=intents,
            entities=entities,
            dialog_nodes=dialog_nodes,
            counterexamples=counterexamples,
            metadata=metadata,
            learning_opt_out=learning_opt_out
        )
        print(json.dumps(response, indent=2))

    def delete_workspace(self, workspace_id=None):
        self.conversation.delete_workspace(
            workspace_id=workspace_id
        )
        print("Deleted workspace {}".format(workspace_id))

    def get_workspace(self, workspace_id=None, export=False):
        response = self.conversation.get_workspace(
            workspace_id=workspace_id,
            export=export
        )
        print(json.dumps(response, indent=2))

    def update_workspace(self, workspace_id=None, name=None, description=None, language=None, intents=None,
                         entities=None, dialog_nodes=None, counterexamples=None, metadata=None, learning_opt_out=None):
        response = self.conversation.update_workspace(
            workspace_id=workspace_id,
            name=name,
            description=description,
            language=language,
            intents=intents,
            entities=entities,
            dialog_nodes=dialog_nodes,
            counterexamples=counterexamples,
            metadata=metadata,
            learning_opt_out=learning_opt_out
        )
        print(json.dumps(response, indent=2))
