from watson_developer_cloud import ConversationV1 as Conversation
import json


class Dialog:
    """
    DOCSTRING
    """

    def __init__(self, username=None, password=None, version=None):
        self.conversation = Conversation(
            username=username,
            password=password,
            version=version
        )

    def get_all_nodes(self, workspace_id=None, dialog_node=None):
        response = self.conversation.get_dialog_node(
            workspace_id=workspace_id,
            dialog_node=dialog_node
        )
        print(json.dumps(response, indent=2))

    def create_dialog_node(self, workspace_id=None, dialog_node=None, description=None, conditions=None, parent=None,
                           previous_sibling=None, output=None, context=None, metadata=None, next_step=None,
                           actions=None, title=None, node_type=None, event_name=None, variable=None):
        response = self.conversation.create_dialog_node(
            workspace_id=workspace_id,
            dialog_node=dialog_node,
            description=description,
            conditions=conditions,
            parent=parent,
            previous_sibling=previous_sibling,
            output=output,
            context=context,
            metadata=metadata,
            next_step=next_step,
            actions=actions,
            title=title,
            node_type=node_type,
            event_name=event_name,
            variable=variable
        )
        print(json.dumps(response, indent=2))

    def delete_dialog_node(self, workspace_id=None, dialog_node=None):
        self.conversation.delete_dialog_node(
            workspace_id=workspace_id,
            dialog_node=dialog_node
        )
        print("Deleted node {}".format(dialog_node))

    def get_dialog_node(self, workspace_id=None, dialog_node=None):
        response = self.conversation.get_dialog_node(
            workspace_id=workspace_id,
            dialog_node=dialog_node
        )
        print(json.dumps(response, indent=2))

    def update_dialog_node(self, workspace_id=None, dialog_node=None, new_dialog_node=None, new_description=None,
                           new_conditions=None, new_parent=None, new_previous_sibling=None, new_output=None,
                           new_context=None, new_metadata=None, new_next_step=None, new_title=None, new_type=None,
                           new_event_name=None, new_variable=None, new_actions=None):
        response = self.conversation.update_dialog_node(
            workspace_id=workspace_id,
            dialog_node=dialog_node,
            new_dialog_node=new_dialog_node,
            new_description=new_description,
            new_conditions=new_conditions,
            new_parent=new_parent,
            new_previous_sibling=new_previous_sibling,
            new_output=new_output,
            new_context=new_context,
            new_metadata=new_metadata,
            new_next_step=new_next_step,
            new_title=new_title,
            new_type=new_type,
            new_event_name=new_event_name,
            new_variable=new_variable,
            new_actions=new_actions
        )
        print(json.dumps(response, indent=2))
