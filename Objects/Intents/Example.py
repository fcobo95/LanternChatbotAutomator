from watson_developer_cloud import ConversationV1 as Conversation
import json


class Example:
    """
       DOCSTRING
       """

    def __init__(self, username=None, password=None, version=None):
        self.conversation = Conversation(
            username=username,
            password=password,
            version=version
        )

    def get_all_examples(self, workspace_id=None, intent=None, page_limit=None, include_count=False, sort=None,
                         cursor=None):
        response = self.conversation.list_examples(
            workspace_id=workspace_id,
            intent=intent,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor
        )
        print(json.dumps(response, indent=2))

    def create_example(self, workspace_id, intent, text):
        response = self.conversation.create_example(
            workspace_id=workspace_id,
            intent=intent,
            text=text
        )
        print(json.dumps(response, indent=2))

    def delete_example(self, workspace_id, intent, text):
        self.conversation.delete_example(
            workspace_id=workspace_id,
            intent=intent,
            text=text
        )
        print("[!]Deleted text {} in intent {}".format(text, intent))

    def get_example(self, workspace_id, intent, text):
        response = self.conversation.get_example(
            workspace_id=workspace_id,
            intent=intent,
            text=text
        )
        print(json.dumps(response, indent=2))

    def update_example(self, workspace_id, intent, text, new_text):
        response = self.conversation.update_example(
            workspace_id=workspace_id,
            intent=intent,
            text=text,
            new_text=new_text
        )
        print(json.dumps(response, indent=2))
