from watson_developer_cloud import ConversationV1 as Conversation
import json


class Value:
    """
    DOCSTRING
    """

    def __init__(self, username=None, password=None, version=None):
        self.conversation = Conversation(
            username=username,
            password=password,
            version=version
        )

    def get_all_values(self, workspace_id, entity, export, page_limit, include_count, sort, cursor):
        response = self.conversation.list_values(
            workspace_id=workspace_id,
            entity=entity,
            export=export,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor
        )
        print(json.dumps(response, indent=2))

    def create_value(self, workspace_id, entity, value, metadata, synonyms, patterns, value_type):
        response = self.conversation.create_value(
            workspace_id=workspace_id,
            entity=entity,
            value=value,
            metadata=metadata,
            synonyms=synonyms,
            patterns=patterns,
            value_type=value_type
        )
        print(json.dumps(response, indent=2))

    def delete_value(self, workspace_id, entity, value):
        self.conversation.delete_value(
            workspace_id=workspace_id,
            entity=entity,
            value=value
        )

    def get_value(self, workspace_id, entity, value, export):
        response = self.conversation.get_value(
            workspace_id=workspace_id,
            entity=entity,
            value=value,
            export=export
        )
        print(json.dumps(response, indent=2))

    def update_value(self, workspace_id, entity, value, new_value, new_metadata, new_type, new_synonym, new_pattern):
        response = self.conversation.update_value(
            workspace_id=workspace_id,
            entity=entity,
            value=value,
            new_value=new_value,
            new_metadata=new_metadata,
            new_type=new_type,
            new_synonyms=new_synonym,
            new_patterns=new_pattern
        )
        print(json.dumps(response, indent=2))
