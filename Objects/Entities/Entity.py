from watson_developer_cloud import ConversationV1 as Conversation
import json


class Entity:
    """
    DOCSTRING
    """

    def __init__(self, username=None, password=None, version=None):
        self.conversation = Conversation(
            username=username,
            password=password,
            version=version
        )

    def get_all_entities(self, workspace_id=None, export=None, page_limit=None, include_count=None, sort=None,
                         cursor=None):
        response = self.conversation.list_entities(
            workspace_id=workspace_id,
            export=export,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor
        )
        print(json.dumps(response, indent=2))

    def create_entity(self, workspace_id=None, entity=None, description=None, metadata=None, values=None,
                      fuzzy_match=False):
        response = self.conversation.create_entity(
            workspace_id=workspace_id,
            entity=entity,
            description=description,
            metadata=metadata,
            values=values,
            fuzzy_match=fuzzy_match
        )
        print(json.dumps(response, indent=2))

    def delete_entity(self, workspace_id=None, entity=None):
        self.conversation.delete_entity(
            workspace_id=workspace_id,
            entity=entity
        )
        print("[!]Deleted Entity {}[!]".format(entity))

    def get_entity(self, workspace_id=None, entity=None, export=None):
        response = self.conversation.get_entity(
            workspace_id=workspace_id,
            entity=entity,
            export=export
        )
        print(json.dumps(response, indent=2))

    def update_entity(self, workspace_id=None, entity=None, new_entity=None, new_description=None, new_metadata=None,
                      new_fuzzy_match=None, new_value=None):
        response = self.conversation.update_entity(
            workspace_id=workspace_id,
            entity=entity,
            new_entity=new_entity,
            new_description=new_description,
            new_metadata=new_metadata,
            new_fuzzy_match=new_fuzzy_match,
            new_values=new_value
        )
        print(json.dumps(response, indent=2))
